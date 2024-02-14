import os

mensagens = []


nome = input("nome: ")

while True:

       #Limpando o terminal
        os.system('cls')

        if len ("mensagens") > 0:
            for m in mensagens:
                print(m["nome"] , "_" , m["texto"])

            print("_________________")
             #obtendo texto
            texto = input("mensagen: ")
            if texto == "fim":
                break
                #adicionando mensagens na lista
            mensagens.append({
                "nome":nome,
                "texto": texto
            })
