import simplecrypt
import pwinput 

def encrypt(plaintext, password):
    ciphertext = simplecrypt.encrypt(password, plaintext)
    return ciphertext

def decrypt(ciphertext, password):
    plaintext = simplecrypt.decrypt(password, ciphertext)
    return plaintext

USUARIO = input("Introduce tu Usuario: ")
PASWORD = pwinput.pwinput("Introduce tu Contraseña: ")

PASWORD_ENC = encrypt(PASWORD, 'password')
print("Encrypted Password:", PASWORD_ENC)

# Decrypt the password
decrypted_password = decrypt(PASWORD_ENC, 'password')
print("Decrypted Password:", decrypted_password)