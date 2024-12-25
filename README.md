# Encrypted-Diary

🛡️ Encrypted Diary
Encrypted Diary is a secure, RSA-encrypted digital diary built with Python. It ensures your private thoughts remain confidential by encrypting entries with public-key cryptography. Only you, with the private key, can decrypt and access the entries.

🔑 Features
RSA Encryption: Encrypt diary entries using a public key.
Private Key Decryption: Only the private key can decrypt and reveal entries.
Persistent Storage: Encrypted entries are saved in a text file for future access.
Simple Menu: Easily generate keys, add entries, and view them securely.
🚀 How to Use
Clone the Repository:

bash
Kopier kode
git clone https://github.com/<your-username>/encrypted-diary.git
cd encrypted-diary
Install Dependencies:

bash
Kopier kode
pip install cryptography
Run the Program:

bash
Kopier kode
python encrypted_diary.py
Choose an Option:

1: Generate RSA keys (public and private keys will be saved as public_key.pem and private_key.pem).
2: Add a new diary entry (encrypted and stored in diary.txt).
3: View your encrypted diary entries (decrypted using your private key).
🧰 Requirements
Python 3.7+
cryptography library
📂 File Structure
encrypted_diary.py: Main program file.
private_key.pem: Your private key (keep this safe!).
public_key.pem: Public key for encrypting entries.
diary.txt: File where encrypted entries are stored.
⚙️ Future Enhancements
Password protection for the private key.
Add timestamps to entries.
GUI for easier interaction.
Search and filter functionality for diary entries.
🤝 Contributions
Feel free to fork the repository, submit issues, or open pull requests to improve the project.
