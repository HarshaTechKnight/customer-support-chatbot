import tkinter as tk
from tkinter import scrolledtext, ttk
from transformers import pipeline
import threading

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Customer Support Chatbot")
        self.root.geometry("800x600")
        
        # Initialize chatbot (use a smaller model if DialoGPT fails)
        try:
            self.chatbot = pipeline("text-generation", model="microsoft/DialoGPT-small")
        except:
            self.chatbot = pipeline("text-generation", model="distilgpt2")
        
        # Create GUI elements
        self.create_widgets()
    
    def create_widgets(self):
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, width=70, height=25
        )
        self.chat_display.pack(pady=10)
        self.chat_display.config(state=tk.DISABLED)
        
        # User input
        self.user_input = tk.Entry(self.root, width=60)
        self.user_input.pack(pady=5)
        self.user_input.bind("<Return>", self.send_message)
        
        # Send button
        self.send_btn = ttk.Button(
            self.root, text="Send", command=self.send_message
        )
        self.send_btn.pack(pady=5)
        
        # Status bar
        self.status = tk.Label(
            self.root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W
        )
        self.status.pack(fill=tk.X)
        
        # Add welcome message
        self.update_chat("Bot", "Hello! I'm your customer support assistant. How can I help you today?")
    
    def send_message(self, event=None):
        user_text = self.user_input.get()
        if not user_text.strip():
            return
            
        self.update_chat("You", user_text)
        self.user_input.delete(0, tk.END)
        
        # Disable UI while processing
        self.user_input.config(state=tk.DISABLED)
        self.send_btn.config(state=tk.DISABLED)
        self.status.config(text="Bot is thinking...")
        
        # Process in background to prevent UI freeze
        threading.Thread(
            target=self.get_bot_response,
            args=(user_text,),
            daemon=True
        ).start()
    
    def get_bot_response(self, user_text):
        try:
            response = self.chatbot(
                user_text,
                max_length=100,
                do_sample=True,
                top_p=0.95,
                top_k=50
            )[0]['generated_text']
            
            # Clean up response
            response = response.replace(user_text, "").strip()
            response = response.split("\n")[0]  # Take first line only
        except Exception as e:
            response = f"Sorry, I encountered an error: {str(e)}"
        
        # Update UI in main thread
        self.root.after(0, lambda: self.update_after_response(response))
    
    def update_after_response(self, response):
        self.update_chat("Bot", response)
        self.user_input.config(state=tk.NORMAL)
        self.send_btn.config(state=tk.NORMAL)
        self.status.config(text="Ready")
        self.user_input.focus()
    
    def update_chat(self, sender, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()