# import nltk
from nltk.tokenize import word_tokenize

# Download required NLTK resources
# nltk.download("punkt")

def set_username(user_input):
    # Tokenize the input ['my', 'name', 'is', 'aaron']
    tokens = word_tokenize(user_input.lower())
    name_keywords = {"name", "call", "known", "i", "am", "me", "'m"}
    user_name = None

    # Identify the name based on keywords and structure
    for i, token in enumerate(tokens):
        if token in name_keywords:
            # Check for "My name is [Name]" or similar
            if token == "name" and i + 2 < len(tokens) and tokens[i + 1] in {"is", "by"}:
                user_name = tokens[i + 2]
                break
            # Check for "Call me [Name]" or similar
            elif token == "call" and i + 1 < len(tokens) and tokens[i + 1] == "me":
                user_name = tokens[i + 2] if i + 2 < len(tokens) else None
                break
            # Check for "I am [Name]"
            elif token == "i" and i + 1 < len(tokens) and tokens[i + 1] in {"am", "'m"}:
                user_name = tokens[i + 2] if i + 2 < len(tokens) else None
                break
            # Check for "I'm [Name]" explicitly
            elif token == "i'm" and i + 1 < len(tokens):
                user_name = tokens[i + 1]
                break
            # Check for "known as [Name]"
            elif token == "known" and i + 1 < len(tokens) and tokens[i + 1] == "as":
                user_name = tokens[i + 2]
                break
            # Check for "They call me [Name]"
            elif token == "me" and i - 1 >= 0 and tokens[i - 1] == "call":
                user_name = tokens[i + 1] if i + 1 < len(tokens) else None
                break

    # Capitalize the name if found
    if user_name:
        user_name = user_name.capitalize()  

    return user_name
