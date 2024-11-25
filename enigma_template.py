# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: roccowuzhurr
# created: 11.19.2024
# last update:  11.18.2024
import random

global f


# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    message = input("enter message: ")
    loop = True
    while loop:
        try:
            keyput = int(input("enter key: "))
        except TypeError:
            if keyput == "":
                keyput = random.randint(0, 26)
            else:
                print("don't do that")
        else:
            keyput = abs(keyput)
            loop = False
    key = (keyput % 26)
    message = message.lower()
    code_message = ""
    for x in range(len(message)):
        if 122 > ord(message[x]) > 97:
            if (ord(message[x]) + key) > 122:  # if the resulting letter is supposed to loop outside of the alphabet,
                code_message += chr((((ord(message[x]) + key) - 122) % 26) + 97)
                # take the number from the big letter, subtract the ascii out,
                # then modulo it by 26 to get rid of the excess, then add 97 to start it from the beginning
                # really weird
            else:
                code_message += chr(ord(message[x]) + key)
    print(f"{code_message}, key of {keyput}")
    print("would you like to save this to a file?")
    ans = input("y/n: ")
    if ans.lower() == "y":
        fname = input("name of file?")
        fname = fname.strip().lower()
        f = open(f"{fname}.txt", 'w')
        f.write(code_message)
        f.close()


# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    loop = True
    while loop:
        try:
            read_file = input("enter filename: ")
            f = open(f"{read_file}.txt", "r")
            message = (f.read())
        except:
            print("wow okay")
        else:
            loop = False
    loop = True
    while loop:
        try:
            keyput = int(input("enter key: "))
        except TypeError:
            if keyput == "":
                keyput = random.randint(0, 26)
            else:
                print("don't do that")
        else:
            keyput = abs(keyput)
            loop = False
    key = (keyput % 26)
    code_message = ""
    for x in range(len(message)):
        if 122 > ord(message[x]) > 97:
            if (ord(message[x]) + key) > 122:  # if the resulting letter is supposed to loop outside of the alphabet,
                code_message += chr((((ord(message[x]) + key) - 122) % 26) + 97)
                # take the number from the big letter, subtract the ascii out,
                # then modulo it by 26 to get rid of the excess, then add 97 to start it from the beginning
                # really weird
            else:
                code_message += chr(ord(message[x]) + key)
    print(f"{code_message}, key of {keyput}")
    print("would you like to save this to a new file?")
    f.close()
    ans = input("y/n: ")
    if ans.lower() == "y":
        fname = input("name of file?")
        fname = fname.strip().lower()
        f2 = open(f"{fname}.txt", 'w')
        f2.write(code_message)
        f2.close()
    else:
        print("would you like to overwrite current file?")
        ans = input("y/n: ")
        if ans.lower() == "y":
            f = open(f"{read_file}.txt", "w")
            f.write(code_message)
            f.close()

# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    loop = True
    while loop:
        try:
            read_file = input("enter filename: ")
            f = open(f"{read_file}.txt", "r")
            message = (f.read())
        except:
            print("wow okay")
        else:
            loop = False
    if input("do you know the key? y/n\n>") == "n":
        f.close()
        decode_unknown_key(read_file)
    else:
        loop = True
        keyput = ""
        while loop:
            try:
                keyput = int(input("enter key: "))
            except TypeError:
                if keyput == "":
                    keyput = random.randint(0, 26)
                else:
                    print("don't do that")
            else:
                keyput = abs(keyput)
                loop = False
        key = (keyput % 26)
        code_message = ""
        for x in range(len(message)):
            if 122 > ord(message[x]) > 97:
                if (ord(message[x]) - key) < 97:  # same as encoding, just subtract,
                    code_message += chr((((ord(message[x]) - key) - 122) % 26) + 97)

                else:
                    code_message += chr(ord(message[x]) - key)
        print(f"{code_message}, key of {keyput}")
        print("would you like to save this to a new file?")
        f.close()
        ans = input("y/n: ")
        if ans.lower() == "y":
            fname = input("name of file?")
            fname = fname.strip().lower()
            f2 = open(f"{fname}.txt", 'w')
            f2.write(code_message)
            f2.close()
        else:
            print("would you like to overwrite current file?")
            ans = input("y/n: ")
            if ans.lower() == "y":
                f = open(f"{read_file}.txt", "w")
                f.write(code_message)
                f.close()


# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):
    f = open(f"{filename}.txt", "r")
    message = f.read()
    f.close()
    code_message = ""
    for key in range(1, 26):
        for x in range(len(message)):
            if 122 > ord(message[x]) > 97:
                if (ord(message[x]) - key) < 97: # same as normal decoding the key, just looped
                    code_message += chr((((ord(message[x]) - key) - 122) % 26) + 97)
                else:
                    code_message += chr(ord(message[x]) - key)
        print(f"{code_message}, key of {key}")
        code_message = ""

# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye..........  . . . ")
            exit()
        else:
            print("Invalid choice. Please try again.")


# runs on program start
if __name__ == "__main__":
    main()
