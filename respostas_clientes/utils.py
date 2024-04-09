from cryptography.fernet import Fernet
from django.conf import settings


cipher_suite = Fernet(settings.FERNET_KEY.encode())

def encrypt_email(email):
    if isinstance(email, str):
        email = email.encode('utf-8')  # Converte para bytes
    encrypted_email = cipher_suite.encrypt(email)
    return encrypted_email.decode('utf-8')  # Converte bytes para string para uso na URL

def decrypt_email(encrypted_email):
    if isinstance(encrypted_email, str):
        encrypted_email = encrypted_email.encode('utf-8')  # Converte para bytes
    decrypted_email = cipher_suite.decrypt(encrypted_email)
    return decrypted_email.decode('utf-8')
