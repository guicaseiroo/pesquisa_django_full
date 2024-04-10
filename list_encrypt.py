from cryptography.fernet import Fernet
import os

FERNET_KEY = os.getenv('FERNET_KEY', 'odQvwmzW36jFf4TeaOnkv1tSpW-f61zUzB90-7dusTQ=')
cipher_suite = Fernet(FERNET_KEY)

def criptografar(email):
    if isinstance(email, str):
        email = email.encode('utf-8')  # Converte para bytes
    encrypted_email = cipher_suite.encrypt(email)
    return encrypted_email.decode('utf-8')  # Converte bytes para string para uso na URL


lista = [
    'caseiro.gui@tahto.com',
]

for i in lista:
    print(criptografar(i))

"""
if __name__ == "__main__":
    import sys
    emails = sys.argv[1:]  # Captura todos os argumentos após o nome do script
    if emails:
        for email in emails:
            print(f"Email Original: {email}")
            email_criptografado = criptografar(email)
            print(f"Email Criptografado: {email_criptografado}")
    else:
        print("Por favor, forneça pelo menos um email como argumento.")
"""