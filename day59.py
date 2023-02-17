
def greet(tx):
    def mfx():
        print("Good Morning")
        tx()
        print("Thanks for using this function.")
    return mfx

@greet
def mellow():
    print("Mellow world")
def hello():
    print("Hello world")

hello()
mellow()