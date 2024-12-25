from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
import os

# Generate RSA Keys
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    # Save keys to files
    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )
    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )
    print("Keys generated and saved!")

# Load RSA Keys
def load_keys():
    with open("private_key.pem", "rb") as priv_file:
        private_key = serialization.load_pem_private_key(
            priv_file.read(),
            password=None,
        )
    with open("public_key.pem", "rb") as pub_file:
        public_key = serialization.load_pem_public_key(pub_file.read())
    return private_key, public_key

# Encrypt Diary Entry
def encrypt_entry(entry, public_key):
    ciphertext = public_key.encrypt(
        entry.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

# Decrypt Diary Entry
def decrypt_entry(ciphertext, private_key):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

# Save Encrypted Entry to File
def save_entry(ciphertext, filename="diary.txt"):
    with open(filename, "ab") as file:
        file.write(ciphertext + b"\n")
    print("Entry saved!")

# Read and Decrypt Entries
def read_entries(filename="diary.txt"):
    private_key, _ = load_keys()
    if not os.path.exists(filename):
        print("No entries found!")
        return
    with open(filename, "rb") as file:
        entries = file.readlines()
    for idx, ciphertext in enumerate(entries, 1):
        plaintext = decrypt_entry(ciphertext.strip(), private_key)
        print(f"Entry {idx}: {plaintext}")

# Main Program
if __name__ == "__main__":
    print("Encrypted Diary")
    print("1. Generate RSA Keys")
    print("2. Add Diary Entry")
    print("3. View Diary Entries")
    choice = input("Choose an option: ")

    if choice == "1":
        generate_keys()
    elif choice == "2":
        _, public_key = load_keys()
        entry = input("Write your diary entry: ")
        encrypted_entry = encrypt_entry(entry, public_key)
        save_entry(encrypted_entry)
    elif choice == "3":
        read_entries()
    else:
        print("Invalid choice!")
