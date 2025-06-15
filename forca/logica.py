print("Inicio")

idade = int(input("Qual idade ?"))

if (idade < 16):
    print("Não vota")
elif (idade >= 16 and idade<18) or (idade>70):
    print("Opcional")
else :
    print("Obrigatório")