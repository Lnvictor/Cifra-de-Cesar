from Biblioteca import *

escolha = RecebeModo()
chave = RecebeChave()

MensagemTraduzida = GeraMensagemTraduzida(escolha,input(str("Insira a mensagem:\n")),chave)
print(MensagemTraduzida)