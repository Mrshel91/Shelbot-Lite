import ollama
import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"

# Load memory
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        memory = json.load(f)
else:
    memory = []

print("🛠️  ShelBot Lite is now online!")
print("   Free local AI by Sheltech LLC")
print("   Type 'quit' or 'exit' to stop.\n")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ['quit', 'exit', 'bye']:
        print("ShelBot: See you later, Ryan! Keep building cool stuff 🚀")
        break
    
    if not user_input:
        continue

    # Add user message
    memory.append({"role": "user", "content": user_input})
    
    # Get response
    response = ollama.chat(
        model="llama3.2:3b",          # Change this if you want to use another model
        messages=memory
    )
    reply = response['message']['content']
    
    # Add reply to memory
    memory.append({"role": "assistant", "content": reply})
    
    # Trim old messages if memory gets too big
    if len(memory) > 50:
        memory = memory[-40:]
    
    # Save memory
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)
    
    print(f"ShelBot: {reply}\n")
