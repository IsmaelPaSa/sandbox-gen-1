# Password generator
import sys
import random

def boot():
    # Read arguments from command line, format:
    # python3 generation_one.py <length> <options>
    # Options:
    # -l: lowercase
    # -u: uppercase
    # -n: numbers
    # -s: special characters
    # -h: help
    # -v: version

    # Check if there are enough arguments
    if len(sys.argv) < 2:
        print("Not enough arguments")
        sys.exit()
    # Check if '-h' is in the arguments
    if '-h' in sys.argv:
        print("Usage: python3 generation_one.py <length> <options>")
        print("Options:")
        print("-l: lowercase")
        print("-u: uppercase")
        print("-n: numbers")
        print("-s: special characters")
        print("-h: help")
        print("-v: version")
        sys.exit()

    # Check if '-v' is in the arguments
    if '-v' in sys.argv:
        print("Version 1.0")
        sys.exit()
    
    # Start all variables with False
    lowercase = False
    uppercase = False
    numbers = False
    special = False
    length = 0

    # Check if '-l' is in the arguments
    if '-l' in sys.argv:
        lowercase = True

    # Check if '-u' is in the arguments
    if '-u' in sys.argv:
        uppercase = True

    # Check if '-n' is in the arguments
    if '-n' in sys.argv:
        numbers = True

    # Check if '-s' is in the arguments
    if '-s' in sys.argv:
        special = True

    # Check if '-l' and '-u' are in the arguments
    if '-l' in sys.argv and '-u' in sys.argv:
        lowercase = True
        uppercase = True
    
    # Check the length of the password
    try:
        length = int(sys.argv[1])
    except ValueError:
        print("Length must be an integer")
        sys.exit()

    # Check if the length is between 1 and 128
    if length < 1 or length > 128:
        print("Length must be between 1 and 128")
        sys.exit()

    # Check if there are no options
    if not lowercase and not uppercase and not numbers and not special:
        print("You must choose at least one option")
        sys.exit()

    # Return all variables
    return lowercase, uppercase, numbers, special, length

def start():
    # Get all variables from boot()
    lowercase, uppercase, numbers, special, length = boot()

    # Create a list with all characters
    characters = []
    if lowercase:
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))
    if uppercase:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if numbers:
        characters.extend(list('0123456789'))
    if special:
        characters.extend(list('!@#$%^&*()_+-=[]{};\':"<>?,./'))

    # Create a password
    password = ''
    for i in range(length):
        password += characters[int(len(characters) * random.random())]

    # Print the password
    print(password)

    # Copy the password to the clipboard
    try:
        import pyperclip
        pyperclip.copy(password)
        print("Password copied to clipboard")
    except:
        print("Error: pyperclip not found")

start()