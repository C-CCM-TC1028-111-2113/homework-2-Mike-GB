
def main():
    #Escribe tu código debajo de esta línea
    edad = int(input("Ingresa tu edad: "))

    if edad < 0:
        print("Respuesta incorrecta")
    if edad < 18:
        print("No cumples requisitos")
    if edad >= 18:
        identificacion = str(input("¿Tienes identificación oficial? (s/n): "  ))  
        if identificacion == "n":
          print ("No cumples requisitos")
        if identificacion == "s":
          print("Trámite de licencia concedido")
        if identificacion != "s" or "n":
          print("Respuesta incorrecta")


if __name__ == '__main__':
    main()
