
def main():
    #Escribe tu código debajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    
    if edad >= 18:
        identificacion=str(input("¿Tienes identificación oficial? (s/n): "))
        if identificacion == "s":
            print("Trámite de licencia concedido")
        elif identificacion=="n":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
            
    elif 0 < identificacion < 18 :
        print("No cumples requisitos")

    else :
        print("Respuesta incorrecta") 


if __name__ == '__main__':
    main()
