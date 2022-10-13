def menu():
    print("w- Moure dreta")
    print("a- Moure equerre")
    print("d- Moure amunt")
    print("s- Moure moure avall")    
    print("0- Sortir")

def main():

    menu()
    
    posX = 0
    posY = 0

    sortir=False
    while not sortir:
        op = input('Entra una opció')
        if op=='d':
            #sumar 1 a la variable posX
            pass
        elif op=='a':
            #restar 1 a la variable posX
            pass
        elif op=='w':
            #sumar 1 a la variable posY
            pass
        elif op=='s':
            #restar 1 a la variable posY
            pass
        elif op=='0':
            sortir=True
            print("Has sortit de la nau")
        
        print(f"La nau està a la posició ({posX},{posY})")
        
if __name__ == "__main__":
    main()
