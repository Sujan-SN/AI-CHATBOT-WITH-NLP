import nltk

nltk.download('punkt')
nltk.download('stopwords')

print("NLTK setup complete!")

setup _nltk.py

import json
import random
import string
import tkinter as tk
from tkinter import scrolledtext

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

with open("intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)

stop_words = set(stopwords.words("english"))

patterns = []
tags = []
responses = {}

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])
    responses[intent["tag"]] = intent["responses"]

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

processed_patterns = [preprocess(pattern) for pattern in patterns]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(processed_patterns)

def get_response(user_input):
    user_input_processed = preprocess(user_input)
    user_vector = vectorizer.transform([user_input_processed])

    similarity = cosine_similarity(user_vector, X)
    best_match_index = similarity.argmax()
    best_score = similarity[0, best_match_index]

    if best_score > 0.3:
        tag = tags[best_match_index]
        return random.choice(responses[tag])
    else:
        return "Sorry, I didn't understand that. Please ask something else."

def send_message(event=None):
    user_input = entry_box.get().strip()

    if user_input == "":
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_input + "\n", "user")

    response = get_response(user_input)

    chat_area.insert(tk.END, "Bot: " + response + "\n\n", "bot")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    entry_box.delete(0, tk.END)

window = tk.Tk()
window.title("NLP Chatbot")
window.geometry("500x600")
window.configure(bg="#f0f0f0")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 12))
chat_area.config(state=tk.DISABLED, bg="white", fg="black")
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_area.tag_config("user", foreground="blue")
chat_area.tag_config("bot", foreground="green")

entry_box = tk.Entry(window, font=("Arial", 14))
entry_box.pack(padx=10, pady=10, fill=tk.X)
entry_box.bind("<Return>", send_message)

send_button = tk.Button(
    window,
    text="Send",
    font=("Arial", 12),
    command=send_message,
    bg="#4CAF50",
    fg="white"
)
send_button.pack(pady=5)

chat_area.config(state=tk.NORMAL)
chat_area.insert(tk.END, "Bot: Hello! I am your NLP chatbot.\n\n", "bot")
chat_area.config(state=tk.DISABLED)

window.mainloop()

{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
      "responses": ["Hello! How can I help you?", "Hi there! Ask me anything.", "Hey! Nice to chat with you."]
    },
    {
      "tag": "name",
      "patterns": ["what is your name", "who are you", "tell me your name"],
      "responses": ["I am an NLP chatbot created for a mini project.", "You can call me ChatBot."]
    },
    {
      "tag": "python",
      "patterns": ["what is python", "define python", "tell me about python"],
      "responses": ["Python is a high-level programming language used for AI, web development, and software applications."]
    },
    {
      "tag": "java",
      "patterns": ["what is java", "define java", "tell me about java"],
      "responses": ["Java is an object-oriented programming language widely used for mobile, web, and enterprise applications."]
    },
    {
      "tag": "nlp",
      "patterns": ["what is nlp", "define nlp", "tell me about natural language processing"],
      "responses": ["Natural Language Processing, or NLP, is a field of artificial intelligence that helps computers understand human language."]
    },
    {
      "tag": "thanks",
      "patterns": ["thank you", "thanks", "ok thanks"],
      "responses": ["You're welcome!", "Happy to help!", "Anytime!"]
    },
    {
      "tag": "bye",
      "patterns": ["bye", "goodbye", "see you"],
      "responses": ["Goodbye!", "See you soon!", "Bye! Have a great day."]
    }
  ]
} 



intents.json





chatbot.py
