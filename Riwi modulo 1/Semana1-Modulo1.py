""" inicializamos un bucle while el cual se iterara hasta que una de las condiciones se cumplan, definiremos una lista en la cual
alojaremos los productos que podra elegir el usuario. Mostramos al usuario la lista de productos disponibles y pedimos que ingrese por
teclado el producto que desea, despues se valida que el producto si se encuentre en el inventario, si el producto esta 
la validacion termina, de lo contrario se seguira solicitando por consola que ingrese in producto que este en el inventario"""

while True:
    products = ["arroz", "leche", "huevos"]
    nameProduct = input("Bienvenido esta es la lista que tenemos en inventario:\n \nArroz \nleche \nHuevos \n \nPorfavor elige el producto que deseas: ").strip().lower()
    if nameProduct in products:
        break
    else :
        print("Error, debes de elegir un producto")

""" inicializamos un bucle while el cual se iterara hasta que una de las condiciones se cumplan, pedimos que ingrese por
teclado el valor por unidad del producto, el dato se ingresa como texto para validar que el programa no continue si el usuari
no ingresa ningun valor y preciona la tecla Enter, posterior a esto convertimos el valor en un flotapedimos que ingrese por
tecladopedimos que ingrese por
tecladonte y verificamos que el numero
sea mayor a cero"""

while True:
    priceUnit = (input("Porfavor ingresa en valor unitario: ")).strip()
    try:
        priceUnit2 = float(priceUnit)
        if priceUnit2 > 0:
            break
        else:
            print("El numero debe de ser mayor a cero ")
    except ValueError: 
           print("Solo puedes ingresar valores numericos")


""" inicializamos un bucle while el cual se iterara hasta que una de las condiciones se cumplan, pedimos que ingrese por
teclado el descuento que se aplicara al total de la compra, verificamos si el valor ingresado es mayor a cero para continuar
y aplicar el descuento"""

while True:
    discount = input("Porfavor ingresa el descuento que se aplicara a la compra: ")
    if discount == "":
        discount2 = 0
        break
    elif discount.isdigit():
        discount2 = int(discount)
        if discount2 > 0:
         break
        elif discount2 == 0:
            print("La compra no tiene descuento")
            break
    else: 
        print("ingresa un valor numerico")

""" inicializamos un bucle while el cual se iterara hasta que una de las condiciones se cumplan, pedimos que ingrese por
teclado cuantos productos desea comprar, despues de esto procedemos a verificar que el valor ingresado sea un valor numerico mayor a cero
si cumple con la condicion la validacion terminara de lo contrario se seguira solicitando al usuario que ingrese un valor valido """

while True:
    quantity = input("Porfavor ingresa la cantidad que deseas llevar: ")
    if quantity == "":
        print("Debes de elegir una cantidad")
    elif quantity.isdigit():
        quantity2 = int(quantity)
        if quantity2 > 0:
            break
        else: 
            print("El numero debe ser mayor a cero")
    else:
        print("Solo valores numericos")

""" definimos una funcion la cual recibira como parametros el precio, la cantidad y el descuento y devolvera el valor total
de la factura con el descuento aplicado """
def descuento(param = 0, param2 = 0, param3 = 0):
    total = param * param2
    total *= 1 - param3 / 100
    total = round(total,2)
    return total

total = descuento(priceUnit2, quantity2, discount2)
print(f"----FACTURA DE VENTA----\n {nameProduct}: {total}")
