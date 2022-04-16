# Encryptor and decryptor
import sys
# Try import the cryptography module
try:
    from cryptography.fernet import Fernet
except ImportError:
    print("Cryptography module not found, try: pip3 install cryptography")
    sys.exit()

def boot():
    # Read arguments from command line, format:
    # python3 generation_one.py <options>
    # Options:
    # -kg: key generator
    # -k <key>: key
    # -e: encrypt
    # -d: decrypt
    # -m <message>: message
    # -h: help
    # -v: version

    # Check if there are enough arguments
    if len(sys.argv) < 2:
        print("Not enough arguments, try -h for help")
        sys.exit()

    # Check if '-h' is in the arguments
    if '-h' in sys.argv:
        print("Usage: python3 cryptor.py <options>")
        print("Options:")
        print("-kg: key generator")
        print("-k <key>: key")
        print("-e: encrypt")
        print("-d: decrypt")
        print("-m <message>: message")
        print("-h: help")
        print("-v: version")
        sys.exit()

    # Check if '-v' is in the arguments
    if '-v' in sys.argv:
        print("Version 1.0")
        sys.exit()

    # Start all variables with False
    key_generator = False
    encrypt = False
    decrypt = False
    message = ""
    key = ""

    # Check if '-kg' is in the arguments
    try:
        if "-kg" in sys.argv:
            key_generator = True
    except:
        pass

    # Check if '-k' is in the arguments
    try:
        if "-k" in sys.argv:
            key = sys.argv[sys.argv.index("-k") + 1]
    except:
        pass

    # Check if '-e' is in the arguments
    try:
        if "-e" in sys.argv:
            encrypt = True
    except:
        pass

    # Check if '-d' is in the arguments
    try:
        if "-d" in sys.argv:
            decrypt = True
    except:
        pass

    # Check if '-m' is in the arguments
    try:
        if "-m" in sys.argv:
            message = sys.argv[sys.argv.index("-m") + 1]
    except:
        pass

    # Check if '-kg' and '-k' are in the arguments
    if not key_generator and key == "":
        print("No key specified, try -h for help")
        sys.exit()

    # Check if '-k' is not empty
    if not key == "":
        key_generator = False

    # Check if '-e' and '-d' are in the arguments
    if not encrypt and not decrypt:
        print("No action specified, try -h for help")
        sys.exit()

    # Check if '-m' is in the arguments
    if message == "":
        print("No message specified, try -h for help")
        sys.exit()

    # Return all variables
    return key_generator, key, encrypt, decrypt, message

def key_generator():
    # Generate a key
    key = Fernet.generate_key()
    # Return the key
    return key

def encoder(message):
    # Encode the message
    try:
        return message.encode()
    except AttributeError:
        return message

def decoder(message):
    # Decode the message
    try:
        return message.decode()
    except AttributeError:
        return message

def encrypt(message, key):
    # Encrypt the message
    f = Fernet(key)
    return f.encrypt(encoder(message))

def decrypt(message, key):
    # Decrypt the message
    f = Fernet(key)
    return decoder(f.decrypt(message))

def start():
    key_required, key, encrypt_required, decrypt_required, message = boot()
    action = ""

    # Check if key key_required is True
    if key_required:
        # Generate a key
        key = key_generator()
    
    # Encode the key
    key = encoder(key)

    # Check if encrypt_required is True
    if encrypt_required:
        # Encrypt the message
        message = decoder(message)
        message = encrypt(message, key)
        action = "encrypt"

    # Check if decrypt_required is True
    if decrypt_required:
        # Decrypt the message
        message = encoder(message)
        message = decrypt(message, key)
        action = "decrypt"

    # Decode all
    key = decoder(key)
    message = decoder(message)

    # Print the message
    print('Key: ' + key)
    print('Message: ' + message)
    print('Action: ' + action)

# Start the program
start()