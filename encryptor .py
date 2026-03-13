from cryptography.fernet import Fernet

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    # This is the 'Key' opening the 'Padlock'
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

if __name__ == "__main__":
    # 1. Ask for the secret
    msg = input("Enter a secret message to hide: ")

    # 2. Encrypt it
    secret_box = encrypt_message(msg)
    print(f"\nEncrypted (Ciphertext): {secret_box.decode()}")

    # 3. Decrypt it back
    original_text = decrypt_message(secret_box)
    print(f"Decrypted (Back to normal): {original_text}")