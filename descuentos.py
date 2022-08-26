def run():
    #pass
    menu = """
    Este programa le ayudará a conocer cuanto descuento puede aplicar en sus compras:
    
    1 a 250 unidades (0% de descuento)
    251 a 500 unidades (5% de descuento)
    501 a 1000 unidades (10% de descuento)
    1001 unidades o más (15% de descuento)

    Costo unitario $35.28
    """
    print(menu)
    cantidad = int(input("¿Cuantas unidades desea adquirir?: "))
    if cantidad >= 1001:
        print("La cantidad a pagar por " + str(cantidad) + " unidades es de $ " + str((cantidad*35.28)*0.15))
    elif cantidad >=501<=1000:
        print("La cantidad a pagar por " + str(cantidad) + " unidades es de $ " + str(cantidad*35.28))


if __name__ == "__main__":
    run()