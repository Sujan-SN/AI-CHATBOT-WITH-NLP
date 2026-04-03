# AI-CHATBOT-WITH-NLP

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: SUJAN S N

*INTERN ID*: CTIS6847

*DOMAIN*: Python Programming

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

## DESCRIPTION OF THE TASK

This project focuses on the development of a simple AI-based chatbot using Natural Language Processing (NLP) techniques in Python. The chatbot is designed to interact with users through a graphical user interface (GUI) and provide relevant responses based on user input. The system combines text preprocessing, machine learning techniques, and a structured intent-based dataset to simulate basic human conversation.

The chatbot is implemented using several Python libraries, including NLTK (Natural Language Toolkit), scikit-learn, and Tkinter. NLTK is used for text preprocessing tasks such as tokenization and stopword removal. These steps help in cleaning and standardizing user input by removing unnecessary words and punctuation. This improves the quality of the data fed into the machine learning model.

The core of the chatbot’s intelligence lies in the use of TF-IDF (Term Frequency-Inverse Document Frequency) vectorization and cosine similarity. The dataset, stored in a JSON file (intents.json), contains predefined intents, patterns, and responses. Each pattern represents a possible user query, and each intent is associated with multiple responses.

During execution, all patterns are preprocessed and converted into numerical vectors using TF-IDF vectorization. When a user enters a message, it undergoes the same preprocessing steps and is transformed into a vector. Cosine similarity is then used to compare this input vector with all stored pattern vectors. The chatbot identifies the most similar pattern and selects the corresponding intent. If the similarity score exceeds a predefined threshold (0.3 in this case), the bot responds with a randomly chosen reply from that intent. Otherwise, it returns a fallback message indicating that the input was not understood.

The graphical user interface is built using Tkinter, which provides a user-friendly environment for interaction. The interface includes a scrollable chat area, an input field, and a send button. Messages from the user and responses from the bot are displayed in different colors to enhance readability. The chatbot also supports pressing the Enter key to send messages, improving usability.

This project demonstrates the practical implementation of NLP concepts in a real-world application. Although the chatbot is simple and rule-based, it effectively showcases how machine learning techniques like TF-IDF and similarity matching can be used to build conversational systems.

However, the chatbot has certain limitations. It relies heavily on predefined patterns and cannot understand complex or unseen queries beyond its training data. Additionally, it lacks contextual understanding and cannot maintain conversation history. These limitations can be addressed in future improvements by integrating advanced deep learning models such as recurrent neural networks (RNNs) or transformer-based models.

In conclusion, this AI chatbot project provides a strong foundation for understanding NLP and conversational AI systems. It highlights key concepts such as text preprocessing, vectorization, and similarity measurement while offering a functional and interactive user experience.

## OUTPUT

