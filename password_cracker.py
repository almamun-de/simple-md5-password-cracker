import hashlib

def crack_password(hash, dictionary_file):
    with open(dictionary_file, 'r') as file:
        for line in file:
            word = line.strip()
            if hashlib.md5(word.encode()).hexdigest() == hash:
                return word
    return None

if __name__ == "__main__":
    hashed_password = input("Enter the MD5 hashed password: ")
    dictionary = input("Enter the path to the dictionary file: ")

    result = crack_password(hashed_password, dictionary)

    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found")
