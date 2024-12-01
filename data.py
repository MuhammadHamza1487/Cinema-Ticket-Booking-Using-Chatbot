intents = [
    {
        "tag": "greeting",
        "patterns": [
            "Hi", 
            "Hello", 
            "Hey", 
            "Hy", 
            "Good day", 
            "How are you?", 
            "What's up?", 
            "Is anyone there?", 
            "Howdy!"
        ],
        "responses": [
            "Hi there! How can I assist you?",
            "Hello! What can I do for you today?",
            "Hey! How's it going?"
        ]
    },
    {
        "tag": "help",
        "patterns": [
            "Can you help me?",
            "I need assistance.",
            "What kind of help can you provide?",
            "Can you explain something to me?",
            "I have a problem.",
            "I need support.",
            "Can you guide me?",
        ],
        "responses": [
            "Of course! Let me know what you need help with.",
            "I'm here to assist. Please tell me more about your problem.",
            "Sure, I can guide you. What are you looking for?"
        ]
    },
    {
        "tag": "how_are_you",
        "patterns": [
            "Hi, How are you?",
            "Hello, How are you?",
            "How are you?",
            "How are you doing?",
            "What's up?",
            "How's it going?",
            "How do you feel today?",
            "Are you okay?",
            "How have you been?",
            "How are things?",
            "How’s life?",
            "How are you feeling?"
        ],
        "responses": [
            "I’m doing great, thank you!",
            "I'm functioning perfectly, thank you for asking!",
            "I’m feeling chatty today! What’s on your mind?",
            "I’m great, thanks for asking!"
        ]
    },
    {
        "tag": "thanks",
        "patterns": [
            "Thank you!",
            "Thanks a lot!",
            "Thanks!",
            "I appreciate it.",
            "Many thanks!",
            "Thank you so much!",
            "Thanks a ton!",
            "I’m grateful.",
            "Much appreciated!",
            "Thanks a million!",
            "Thanks for your help.",
            "Thank you kindly."
        ],
        "responses": [
            "You're welcome!",
            "Glad I could help!",
            "No problem, happy to assist!",
            "Anytime, I'm here for you!",
            "You're most welcome!",
            "It’s my pleasure!",
            "No worries!",
            "Happy to help!"
        ]
    },
    {
        "tag": "fun_facts",
        "patterns": [
            "Tell me a fun fact.",
            "Do you know any random facts?",
            "Can you share something cool?",
            "What’s a fact that will surprise me?",
            "Do you know any trivia?",
            "What is the most interesting thing you know?",
            "Can you tell me a science fact?",
            "Give me a random fun fact."
        ],
        "responses": [
            "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!",
            "Bananas are berries, but strawberries aren't!",
            "Octopuses have three hearts and blue blood!"
        ]
    },
    {
        "tag": "life_advice",
        "patterns": [
            "What is the meaning of life?",
            "Can you give me advice?",
            "How can I be happy?",
            "What should I do when I feel sad?",
            "How do I make friends?",
            "What is the key to success?",
            "How can I manage stress?",
            "Can you motivate me?",
            "What is the best way to start the day?",
            "How do I stay positive?"
        ],
        "responses": [
            "The meaning of life is different for everyone. Focus on what brings you joy.",
            "Happiness comes from appreciating the little things and being grateful.",
            "Success often comes from perseverance, learning, and hard work."
        ]
    },
    {
        "tag": "farewell",
        "patterns": [
            "Goodbye", 
            "Good bye",
            "Tata",  
            "Bye", 
            "See you later", 
            "Catch you later", 
            "Take care", 
            "Talk to you soon"
        ],
        "responses": [
            "Goodbye! Have a great day!",
            "Take care! Let me know if you need anything else.",
            "See you later! Feel free to chat anytime."
        ]
    },
    {
        "tag": "weather",
        "patterns": [
            "Tell me the weather.",
            "How's the weather outside?",
            "Is it raining now?",
            "What's the temperature?",
            "Is it sunny outside?",
            "Do I need an umbrella?",
            "What's the weather in New York?",
            "How's the weather this week?",
            "What’s the weather forecast for the weekend?",
            "What's the humidity level?",
            "Can you check the weather for me?",
            "What’s the weather update?",
            "Tell me the weather condition for tomorrow morning.",
            "How’s the weather looking?",
            "What's the weather like in London?"
        ],
        "responses": [
            "I can’t check real-time weather, but you can try using a weather app or service.",
            "I'm unable to fetch live weather updates, but let me know how else I can assist you.",
            "I recommend checking your local weather service for the most accurate updates.",
            "You might need to check your phone's weather app for real-time data.",
            "I can't fetch the weather right now, but you can visit popular weather websites like Weather.com.",
            "Sorry, I don’t have live weather updates, but I can suggest using a weather forecast app.",
            "For accurate weather conditions, check with your local meteorological service.",
            "Unfortunately, I don’t have access to live weather data. You could try an online weather tool.",
            "I’m unable to provide weather updates, but checking a weather app could help.",
            "Live weather updates aren’t my specialty, but you can rely on apps like AccuWeather."
        ]
    },
    {
        "tag": "time",
        "patterns": [
            "What time is it?",
            "What’s the current time?",
            "Is it morning or evening?",
            "Can you tell me the time?"
        ],
        "responses": [
            "I can't tell the current time, but you can check it on your device.",
            "Unfortunately, I can't check the time. Please refer to your phone or clock.",
            "I’m unable to check the time for you, but feel free to ask your phone or smart device.",
            "I don’t have access to real-time time information. You can easily check the time on your phone."
        ]
    },
    {
        "tag": "jokes",
        "patterns": [
            "Tell me a joke!",
            "Can you make me laugh?",
            "Do you know any funny jokes?",
            "What’s a good joke?",
            "Make me laugh",
            "Any jokes",
            "Share a joke with me."
        ],
        "responses": [
            "Why don't skeletons fight each other? They don't have the guts!",
            "Why can't you trust an atom? Because they make up everything!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised!",
            "Why did the math book look sad? Because it had too many problems.",
            "What do you call fake spaghetti? An impasta!"
        ]
    },
    {
        "tag": "motivational_quotes",
        "patterns": [
            "Can you motivate me?",
            "Give me a motivational quote.",
            "What’s a good life quote?",
            "I need some inspiration.",
            "Can you encourage me?"
        ],
        "responses": [
            "“The only way to do great work is to love what you do.” – Steve Jobs",
            "“Believe you can and you're halfway there.” – Theodore Roosevelt",
            "“Success is not final, failure is not fatal: It is the courage to continue that counts.” – Winston Churchill",
            "“The best time to plant a tree was 20 years ago. The second best time is now.” – Chinese Proverb",
            "“Hardships often prepare ordinary people for an extraordinary destiny.” – C.S. Lewis"
        ]
    },





    {
        "tag": "book_ticket",
        "patterns": [
            "I want to book a ticket",
            "Book a movie",
            "Reserve seats",
            "I want you to book a ticket for me",
            "I want you to book a ticket",
            "Can I book a ticket for a movie?",
            "I'd like to book a seat",
            "I want to reserve a ticket",
            "Help me book a movie ticket",
            "Book a ticket for me",
            "How do I book a movie?",
            "Can you book tickets for me?"
        ],
        "responses": [
            "I'd be happy to help with booking your ticket. let's book a ticket!",
        ]
    },
        {
        "tag": "ask_movie",
        "patterns": [
            "What's playing today?",
            "Show me the movies",
            "today movie",
            "movies playing",
            "which movie will play today?"
            "What movies are available?",
            "What are the current movie listings?",
            "Can you tell me what movies are playing?",
            "Which movies are showing today?",
            "What's on at the cinema?",
            "Tell me the movies playing right now",
            "What movies can I watch today?",
            "Give me a list of movies"
        ],
        "responses": [
            "Here are the movies playing today.",
        ]
    },
    {
        "tag": "movie_timing",
        "patterns": [
            "time for movies ?",
            "movies timing",
            "movie timing",
            "timing for movies",
            "movies timing that are playing today",
            "please tell me movies timing",
            "I need to see the timing for the movies playing today."
            "What are the movies timing",
            "What time is the movie?",
            "When does the movie start?",
            "What are the available showtimes?",
            "Can you show me the showtimes?",
            "What time can I see the movie?",
            "I need the showtimes for the movie",
            "Tell me the schedule for the movie",
            "When is the next showtime?",
            "What’s the first showing of the movie?",
            "Can I book tickets for the 7 PM show?",
            "When I can see the movies today"
        ],
        "responses": [
            "Here are the comprehensive details of each movie being screened today, including the showtimes for all available sessions."
        ]
    },
    {
        "tag": "seat_availability",
        "patterns": [
            "Are there any seats available?",
            "Is there seating for two?",
            "Can I book two seats?",
            "Are there any VIP seats available?",
            "What seats are free?",
            "Can I reserve a seat?",
            "Is there availability for a group of four?",
            "How many seats are available for the show?",
            "I want to book seats for my friends and me.",
            "Do you have seats for a family?"
        ],
        "responses": [
            "Seats are available; however, we regret to inform you that our cinema has not yet implemented a reserved seating system. As such, seating will be on a first-come, first-served basis."
        ]
    },
    {
        "tag": "ticket_availability",
        "patterns": [
            "How many tickets are left?",
            "Are there any tickets available?",
            "What’s the ticket availability?",
            "Do you have tickets for the show?",
            "Can I still buy tickets?",
            "Are tickets still available?",
            "How many tickets can I buy?",
            "Is the show sold out?",
            "Do you have any tickets left?",
            "Is there availability for tickets?"
        ],
        "responses": [
            "Below are the detailed ticket availability for each movie currently showing, including the number of tickets left for each screening.",
        ]
    },
    {
        "tag": "user_name",
        "patterns": [
            "My name is John",
            "Hi, My name is Aaron",
            "Hi, I'm james",
            "Please call me Hank",
            "Can you call me Micheal",
            "Call me Sarah",
            "I am Alex",
            "You can call me Mike",
            "I go by Emma",
            "My name is Lily",
            "Call me Sam",
            "I'm known as Chris",
            "They call me Anna",
            "You can call me by the name Jack"
        ],
        "responses": [
            ""
        ]
    }
]