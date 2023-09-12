from cryptography.fernet import Fernet

# Gera a chave no arquivo chave.key
chave = Fernet.generate_key()
with open('chave.key', 'wb') as filekey:
    filekey.write(chave)
# ==== Parte responsavel por relacionar a chave com o text.txt ====
with open('chave.key', 'rb') as filekey:
    chave = filekey.read()
fernet = Fernet(chave)
# ==== Parte responsável por abrir o arquivo txt e ler o que tem dentro
with open('criptografado.txt', 'rb') as text:
    conteudo_text = text.read()
# ==== Parte responsável por trocar o texto principal por parte criptografada ====
criptografado = fernet.encrypt(conteudo_text)
with open('criptografado.txt', 'wb') as text_criptografado:
    text_criptografado.write(criptografado)





