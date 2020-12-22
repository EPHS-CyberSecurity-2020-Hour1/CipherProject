def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    revAlphabet = "zyxwvutsrqponmlkjihgfedcba"


    # get a message from the user
    message = input("input a string: ")
    newMessage = ""
    for letter in message:
        pos = alphabet.find(letter)
        letter = revAlphabet[pos]
        newMessage += letter
    print(newMessage)

main()

