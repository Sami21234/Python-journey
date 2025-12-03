
# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up! 

dict1 = {
    "Pani": "Water",
    "Chawal":"Rice",
    "Daal":"Pulse",
    "Kitaab":"Book",
    "Tarbooj":"Watermelon",
    "Kursi":"Chair"
}

word = input("Enter the word you want meaning of: ")
print(dict1[word])