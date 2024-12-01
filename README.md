# Cinema Ticket Booking Chatbot  

An intelligent chatbot system that allows users to book movie tickets, inquire about movie timings, and check ticket availability through a conversational interface. Built using Python, this project leverages natural language processing (NLP) techniques and machine learning to provide an engaging and user-friendly experience.

---

## Features  
- **Intent Classification**: Identifies user intent such as greetings, ticket booking, or movie inquiries using a Logistic Regression model.  
- **Ticket Booking System**: Extracts movie names and ticket counts from user input and confirms bookings based on availability.  
- **Entity Extraction**: Recognizes user names, movie titles, and other contextual details for personalized interactions.  
- **Database Management**: Tracks movie details, ticket availability, and bookings using an Excel-based system.  

---

## 🛠️ Architecture  

### Functionality  
- **Intent Classification**: Classifies user queries into predefined tags (e.g., greetings, booking, movie inquiries).  
- **Dynamic Response Generation**: Generates responses based on intent and maintains conversational context.  
- **Personalized Interactions**: Extracts user details like names and integrates them into the chat flow.  

### Implementation  
1. **Model Training**:  
   - A `Logistic Regression` model is trained on a custom dataset of intents and patterns.  
   - Input text is vectorized using `TfidfVectorizer`.  
   - Training script: `Training.py`.  

2. **Chatbot Logic**:  
   - Processes user inputs in a conversational loop.  
   - Tracks incomplete booking contexts and prompts for missing details.  
   - Main logic: `app.py`.  

3. **Entity Recognition**:  
   - Extracts key details like user names, movie names, and ticket counts using tokenization and pattern matching.  
   - Code: `name_extraction.py`.  

4. **Database Management**:  
   - Manages movies, timings, and ticket availability using an Excel file (`movies.xlsx`).  
   - Stores booked tickets in an output file (`booked_tickets.xlsx`).  

---

## Project Structure  

```plaintext
├── data.py               # Intent patterns and responses
├── Training.py           # Model training and saving
├── app.py                # Chatbot interaction logic
├── name_extraction.py    # User name and entity extraction
├── input/
│   └── movies.xlsx       # Database of movie details
├── output/
│   └── booked_tickets.xlsx  # Booked tickets storage
└── README.md             # Project documentation
```

---

## ⚙️ Setup and Usage  

### Prerequisites  
- Python 3.8+  
- Required Python libraries: `nltk`, `pandas`, `joblib`, `scikit-learn`, `openpyxl`  

### Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/MuhammadHamza1487/Cinema-Ticket-Booking-Using-Chatbot
   cd Cinema-Ticket-Booking-Using-Chatbot
   ```
2. Install dependencies:  
   ```bash
   Install all libraries with 'pip install'
   ```

3. Download NLTK data:  
   ```python
   import nltk
   nltk.download('punkt')
   ```

### Running the Chatbot  
1. Train the model:  
   ```bash
   python training.py
   ```

2. Start the chatbot:  
   ```bash
   python app.py
   ```

---

## Example Interactions  

### Greeting  
**User**: Hi  
**Chatbot**: Hello! How can I assist you?  

### Booking Tickets  
**User**: I want to book tickets for Avatar.  
**Chatbot**: How many tickets would you like to book?  

---
