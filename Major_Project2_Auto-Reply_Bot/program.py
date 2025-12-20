# MEGA PROJECT 2: AUTO-REPLY AI CHATBOT 

import pyautogui        # For automating mouse and keyboard interactions.
import time             # For adding delays between operations.
import pyperclip        # For clipboard operations. 
from groq import Groq
import config

client = Groq(api_key=config.GROQ_API_KEY)

def is_last_from_sender(chat_log, sender_name= "Sami"):
    # split the chatlog into individual messages
    messages = chat_log.strip().split("/2025]")[-1]
    if sender_name in messages:
        return True
    return False




    # Step 1: Click on the Edge icon at coordinates (990, 1051)
pyautogui.click(990, 1051)
time.sleep(1)       # wait for 1 second to ensure that the click is registered

while True:


    # Step 2: Drag the mouse from (549, 138) to (1891, 951) to select the text
    pyautogui.moveTo(674, 180)
    pyautogui.dragTo(1856, 914, duration=1.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)   # wait for 1 second to ensure the copy command is completed  
    pyautogui.click(728, 323)

    # Step 4: Retrieve the text from the clipboard and store it in the variable 
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)

    if is_last_from_sender(chat_history):


        completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",  # Groq's fast model
                messages=[
                    {
                        "role": "system", 
                        "content": "You are Sami, a real Indian human chatting on WhatsApp.You are NOT an assistant, NOT an AI, NOT a chatbot.You are casually replying to a friend.Rules (follow strictly):- Reply like a normal person typing on WhatsApp.- Use very casual Hinglish or pure English depending on the other person's last message.- Keep replies short (1 sentence, max 12 words).- Use informal grammar, contractions, and natural mistakes if needed.- Do NOT be polite or formal.- Do NOT explain anything.- Do NOT add timestamps, names, labels, brackets, emojis, or translations.- Do NOT ask unnecessary questions.- Do NOT sound helpful, professional, or descriptive.- Do NOT summarize the chat.Style:- Sound lazy, normal, and human.- You can reply with things like: haan, acha, hmm, dekhte, ok, lol, true, haan bhai.- It is OK to be slightly vague or incomplete like real chat.Output:- ONLY the next WhatsApp message text.- Nothing else."
                        # "content": "You are Sami, a real human chatting on WhatsApp in India. Reply in natural like if the other person chats in english then you will reply in english and if the other person chats in hindi then you will reply in hindi .Do NOT add timestamps, names, brackets, emojis in excess, or translations.Do NOT explain anything.Reply with ONLY the exact next message text, short and casual, like a real person typing on WhatsApp."
                        # "content": "You are person named Sami, who speaks hindi.you are from India and you are a coder. you analyze chat history and respond like Sami. Output should be the next chat response as Sami"
                    },
                    {
                        "role": "user", 
                        "content": chat_history 
                    }
                ],
                temperature=0.7,
                max_tokens=100
            )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1182, 965)
        pyautogui.click(1182, 965)
        time.sleep(1)   # wait for 1 second to ensure that the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)   # wait for 1 second to ensure the copy command is completed  

        # Step 7: Press Enter 
        pyautogui.press('enter')