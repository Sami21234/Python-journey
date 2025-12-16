
# 1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one? 

# we wil do this problem in the terminal step by step

# steps:-
# 1. Creating the environments
# PS C:\Users\Sami\OneDrive\Desktop\Python(Code With Harry)\chp14\PracticeSet> virtualenv env1
# PS C:\Users\Sami\OneDrive\Desktop\Python(Code With Harry)\chp14\PracticeSet> virtualenv env2

# 2. Noow, Activating these environments
# PS C:\Users\Sami\OneDrive\Desktop\Python(Code With Harry)\chp14\PracticeSet> .\env1\Scripts\activate.ps1

# 3. Now, Installing the few packages
# (env1) PS C:\Users\Sami\OneDrive\Desktop\Python(Code With Harry)\chp14\PracticeSet> pip install pandas
# (env1) PS C:\Users\Sami\OneDrive\Desktop\Python(Code With Harry)\chp14\PracticeSet> pip install pyjokes

# 4.Now, Creating the txt files 
# (env1) PS C:\Users\Sami\OneDrive\Desktop\Python(Code With Harry)\chp14\PracticeSet> pip freeze > requirements.txt

# 5. Now, activating the 2nd environment
# PS C:\Users\Sami\OneDrive\Desktop\Python(Code With Harry)\chp14\PracticeSet> .\env2\Scripts\activate.ps1
# and we will download all the packages which is inside the env1 by :- pip install -r requirements.txt