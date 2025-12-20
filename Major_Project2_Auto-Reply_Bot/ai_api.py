from groq import Groq
import config

client = Groq(api_key=config.GROQ_API_KEY)
command = '''

[10:59, 16/12/2025] 72 - محمد سمیع: Gaya bhai college
[11:04, 16/12/2025] Sadik (Theem): Nahi bhai ghar p hu
[13:17, 16/12/2025] 72 - محمد سمیع: Achha
[14:05, 17/12/2025] 72 - محمد سمیع: Gaya bhai college
[14:06, 17/12/2025] Sadik (Theem): Nahi bhai
[14:07, 17/12/2025] Sadik (Theem): Tu
[14:18, 17/12/2025] 72 - محمد سمیع: Nahi
[12:03, 19/12/2025] 72 - محمد سمیع: College gaya h bhai
[12:06, 19/12/2025] Sadik (Theem): Nahi bhai
[12:06, 19/12/2025] Sadik (Theem): Sabka Attendance laga diya sirf apna nahi lagya
[13:57, 19/12/2025] 72 - محمد سمیع: Are chod bhai dekhna time pass he to kara raha h
[14:07, 19/12/2025] Sadik (Theem): Ha wo toh hai

'''
completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Groq's fast model
        messages=[
            {
                "role": "system", 
                "content": "You are person named Jarvis, who speaks hindi as well as english. He  is from India and is a coder. you analyze chat history and respond like Jarvis."
            },
            {
                "role": "user", 
                "content": command
            }
        ],
        temperature=0.7,
        max_tokens=100
    )

print(completion.choices[0].message.content)