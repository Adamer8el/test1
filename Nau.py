def menu():
    print("w- Moure amunt")
    print("a- Moure equerre")
    print("d- Moure dreta")
    print("s- Moure avall")    
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
            pasX=posX+1
        elif op=='a':
            #restar 1 a la variable posX
            pasX=posX-1
        elif op=='w':
            #sumar 1 a la variable posY
            pasX=posY+1
        elif op=='s':
            #restar 1 a la variable posY
            pasX=-1
        elif op=='0':
            sortir=True
            print("Has sortit de la nau")
        
        print(f"La nau està a la posició ({posX},{posY})")
        
if __name__ == "__main__":
    main()
