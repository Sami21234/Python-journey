def myFunc():
    print("Hello")

if __name__ == "__main__":
    print("we are directly running this code")
    myFunc()
    print(__name__)  # this prints __main__ cause the code is run from the same files itself and from the main file from importing part this will print as __module__
