TAM_MAX_CH = 26

def RecebeModo():
    contador = 0
    Escolha = str()

    while not Escolha in ["d", "c", "criptografar", "descriptografar"]:
        if contador > 0:
            print("Entrada Inválida!!")
        print("Você quer Criptografar ou descriptografar?")
        Escolha = input(str())
        Escolha = Escolha.lower()
        contador+=1

    return Escolha

def RecebeChave():
    global TAM_MAX_CH
    contador = 0

    while True:
        if contador > 0:
            print("Tamanho de chave Inválido!!")
        chave = int(input(f"Entre com o número da chave ({TAM_MAX_CH}): \n"))

        if 1 <= chave <=TAM_MAX_CH:
            return chave
        contador+=1

def GeraMensagemTraduzida(modo, mensagem, chave):

    mensagemTraduzida = str()

    if modo in ["c", "criptografar"]:
        for el in mensagem:
            if el.isupper():
                if el.isalpha() and ord(el) < 90:
                    mensagemTraduzida += chr(ord(el) + 3)
                elif el.isupper():
                    mensagemTraduzida += chr((90 - ord(el)) + 65)
            else:
                if el.isalpha() and ord(el) < 120:
                    mensagemTraduzida += chr(ord(el) + 3)
                elif el.islower():
                    mensagemTraduzida += chr((122 - ord(el)) + 97)


        return mensagemTraduzida

    if modo in ["d", "descriptografar"]:
        for el in mensagem:
            if el.isupper():
                if el.isalpha() and ord(el) > 3:
                    mensagemTraduzida += chr(ord(el) - 3)
                else:
                    mensagemTraduzida += chr(97 + 65 -ord(el))
            else:
                if el.isalpha() and ord(el) > 99:
                    mensagemTraduzida += chr(ord(el) - 3)
                else:
                    mensagemTraduzida += chr(119 + 97- ord(el))

        return mensagemTraduzida
