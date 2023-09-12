from cryptography.fernet import Fernet

# ==== Carregando a chave para dentro do código ====
with open('chave.key', 'rb') as filekey:
    chave = filekey.read()
fernet = Fernet(chave)
# ==== Lendo o arquivo criptografado ====
with open('criptografado.txt', 'rb') as arquivo_criptografado:
    criptografado = arquivo_criptografado.read()
# ==== Descriptografar a mensagem ====
# ---- A tag try e except serve para poder lidar com problemas no código
# ---- try o código que gera um exceção
# ---- Except código para lidar com a exceção
# ---- Essa parte do código "previne" um possivel erro e aplica a exceção
try:
    descriptografado = fernet.decrypt(criptografado)
except Exception as e:
    print("Erro durante a descriptografia:", str(e))
    descriptografado = b''
# ==== Escrever o resultado descriptografado em um novo arquivo ====
with open('descriptografado.txt', 'wb') as arquivo_descriptografado:
    arquivo_descriptografado.write(descriptografado)
