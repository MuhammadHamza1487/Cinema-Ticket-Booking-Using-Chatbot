import joblib
import random
import pandas as pd
from nltk.tokenize import word_tokenize
import os

from data import intents
import name_extraction

current_user_name = None

# Load the model and vectorizer
vectorizer, classifier = joblib.load('chatbot_model.pkl')

# Define the chatbot response function
def generate_response(user_input):
    transformed_input = vectorizer.transform([user_input])
    predicted_tag = classifier.predict(transformed_input)[0]
    for intent in intents:
        if intent['tag'] == predicted_tag:
            response = random.choice(intent['responses'])
            return response, predicted_tag

# Extract entities from user input
def extract_entities(user_input):
    tokens = word_tokenize(user_input.lower())
    extracted_data = {"movie": None, "tickets": None}

    # Extract number of tickets
    for token in tokens:
        if token.isdigit():
            extracted_data["tickets"] = int(token)
            break

    # Extract movie name
    movies_df = pd.read_excel('input/movies.xlsx')
    for movie in movies_df['Movie'].str.lower(): 
        if movie in user_input.lower():
            extracted_data["movie"] = movie
            break

    return extracted_data

# Book tickets function
def book_tickets(user_name):
    global current_user_name
    if not user_name:
        while not current_user_name:
            name_input = input('Please provide your first and last name for ticket booking: ')
            if len(name_input.split()) <= 2:
                current_user_name = name_input
            else:
                extracted_name = name_extraction.set_username(name_input)
                if extracted_name:
                    current_user_name = extracted_name
                else:
                    print("Sorry, I couldn't understand your name. Please try again.")

    movies_df = pd.read_excel('input/movies.xlsx')
    conversation_context = {"movie": None, "tickets": None}
    print("Bot: Please Provide No of tickets and movie name to book the ticket.")

    while True:
        user_input = input("You: ")
        extracted_data = extract_entities(user_input)

        # Update context with extracted data
        for key, value in extracted_data.items():
            if value:
                conversation_context[key] = value

        # Prompt for missing details
        if not conversation_context["movie"]:
            print("Bot: Which movie would you like to book tickets for? Please provide the exact movie name. Below is more information about the movies")
            display_movies()
        elif not conversation_context["tickets"]:
            print("Bot: How many tickets would you like to book?")
        else:
            selected_movie = conversation_context["movie"]
            ticket_count = conversation_context["tickets"]

            # Check availability and book tickets
            movie_row = movies_df[movies_df['Movie'].str.lower() == selected_movie]

            if not movie_row.empty and movie_row.iloc[0]['Tickets'] >= ticket_count:
                movies_df.loc[movie_row.index, 'Tickets'] -= ticket_count
                movies_df.to_excel('input/movies.xlsx', index=False)
                print(f"Bot: Congratulations {current_user_name}, your {ticket_count} tickets for '{selected_movie}' are booked! Enjoy the movie.")

                # Save booked tickets to output file
                booked_tickets_file = 'output/booked_tickets.xlsx'
                if os.path.exists(booked_tickets_file):
                    booked_tickets_df = pd.read_excel(booked_tickets_file)
                else:
                    booked_tickets_df = pd.DataFrame(columns=["User", "Movie", "Tickets"])

                new_entry = {
                    "User": current_user_name,
                    "Movie": selected_movie,
                    "Tickets": ticket_count
                }
                booked_tickets_df = pd.concat([booked_tickets_df, pd.DataFrame([new_entry])], ignore_index=True)
                booked_tickets_df.to_excel(booked_tickets_file, index=False)

                return current_user_name
            else:
                print("Bot: Sorry, not enough tickets are available. You can select another movie. Here's more information about the ticket availability.")
                display_ticket_availability()
                conversation_context["tickets"] = None


# Display available movies
def display_movies():
    movies_df = pd.read_excel('input/movies.xlsx')
    for idx, movie in enumerate(movies_df['Movie']):
        print(f"{idx+1}. {movie}")

# Display movie timings
def display_movie_timings():
    movies_df = pd.read_excel('input/movies.xlsx')
    for idx, row in movies_df.iterrows():
        print(f"{idx+1}. {row['Movie']}\t-\t{row['Start Time']} to {row['End Time']}")

# Display tickets availability
def display_ticket_availability():
    movies_df = pd.read_excel('input/movies.xlsx')
    for idx, row in movies_df.iterrows():
        print(f"{idx+1}. {row['Movie']}\t-\tTickets Left: {row['Tickets']}")

# Set user name
def set_user_name(user_input):
    name = name_extraction.set_username(user_input)
    if name:
        print(f"Nice to meet you, {name}!")
        return name
    else:
        print("Sorry, I couldn't understand your name. Please try again.")

# Chatbot interaction loop
def chatbot_interaction():
    global current_user_name
    print("CHATBOT")
    print("Welcome to the chatbot! Type 'exit' to quit.")

    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            print("Thanks for chatting! Goodbye.")
            break

        if user_input:
            response, tag = generate_response(user_input)
            print(f"Chatbot: {response}")

            if tag == 'book_ticket':
                current_user_name = book_tickets(current_user_name)

            elif tag == 'ask_movie':
                display_movies()

            elif tag == 'movie_timing':
                display_movie_timings()

            elif tag == 'ticket_availability':
                display_ticket_availability()

            elif tag == 'user_name':
                current_user_name = set_user_name(user_input)

# Start chatbot
if __name__ == "__main__":
    chatbot_interaction()
