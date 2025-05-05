pip install nltk

import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext

# Define chatbot responses using pairs
pairs = [
    [r"List A to Z", ["A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"]],
    [r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! How can I help?"]],
    [r"how are you?", ["I'm doing fine! How about you?"]],
    [r"I'm a (.*) your name?", ["I'm a chatbot, here to assist you."]],
    [r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! Take care!"]],
    [r"(.*)", ["I'm not sure how to respond to that. Could you rephrase?"]]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Send message function
def send_message():
    user_input = user_entry.get()
    chat_history.insert(tk.END, f"You: {user_input}\n")
    response = chatbot.respond(user_input)
    chat_history.insert(tk.END, f"Bot: {response}\n\n")
    user_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Simple Chatbot")

chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15)
chat_history.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=40)
user_entry.pack(padx=10, pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=5)

root.mainloop()
