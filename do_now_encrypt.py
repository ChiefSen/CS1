def sender(message, old_alphabet, new_alphabet):
    new_message = ''

    for m in message:
        for letter in old_alphabet:
            if m == letter:
                new_message += new_alphabet[old_alphabet.index(letter)]
    return new_message
    

def main():
    alphabet = list(" abcdefghijklmnopqrstuvwxyz")
    secret_alphabet = list(" #^6@!~$4-+>?/:;|%{[9)03&7,")

    message = str.lower(input("Enter message: "))
    encrypt = input("Encrypt or Decrypt? ")

    if encrypt == "encrypt":
        new_message = sender(message, alphabet, secret_alphabet)
            
    else:
        new_message = (message, secret_alphabet, alphabet)
    print(new_message)
main()

  
