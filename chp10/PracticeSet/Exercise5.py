
# 5. Repeat program 4 for a list of such words to be censored. 

words = ["Donkey","donkey", "name","Proffession"]
with open("donkey_4.txt","r") as f:
    content = f.read()
for word in words:
    content = content.replace(word,"#"*len(word))
# write method
with open("donkey_4.txt","w") as f:
    f.write(content)