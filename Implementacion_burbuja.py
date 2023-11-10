import queue
from threading import Timer


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


class Productos:
    def __init__(self, id, producto, precio, stock):
        self.id = id
        self.producto = producto
        self.precio = precio
        self.stock = stock

class Ofertas(Productos):
    def __init__(self, id, producto, precio, stock):
        super(Ofertas,self).__init__(id, producto, precio, stock)

class Pizza(Productos):
    def __init__(self, id, producto, precio, stock):
        super(Pizza, self).__init__(id, producto, precio, stock)


class Bebidas(Productos):
    def __init__(self, id, producto, precio, stock):
        super(Bebidas, self).__init__(id, producto, precio, stock)


class Complementos(Productos):
    def __init__(self, id, producto, precio, stock):
        super(Complementos, self).__init__(id, producto, precio, stock)


class ListaClientes:
    def __init__(self):
        self.pila_clientes = []

    def agregar_clientes(self, clientes):
        self.pila_clientes.append(clientes)

    def lista_vacia(self):
        vacia = len(self.pila_clientes)
        if vacia == 0:
            return 0

    def mostrar(self):
        print(self.pila_clientes)

class ModificacionOfertas:
    def __init__(self):
        self.pila_oferta=[]
    def agregar_oferta(self,ofertas):
        self.pila_oferta.append(ofertas)
class ModificacionPizza:
    def __init__(self):
        self.pila_pizza = []

    def agregar_pizza(self, pizzas):
        self.pila_pizza.append(pizzas)


class ModificacionBebida:
    def __init__(self):
        self.pila_bebida = []

    def agregar_bebida(self, bebidas):
        self.pila_bebida.append(bebidas)


class ModificacionComplemento:
    def __init__(self):
        self.pila_complemento = []

    def agregar_complemento(self, complementos):
        self.pila_complemento.append(complementos)


class Colas:
    def __init__(self):
        self.cola_pendiente = queue.Queue()
        self.cola_preparacion = queue.Queue()
        self.cola_listo_servir = queue.Queue()

    def agregar_cola_pendiente(self, pedidos):
        self.cola_pendiente.put(pedidos)

    def agregar_cola_preparacion(self):
        if not self.cola_pendiente.empty():
            pedido_preparar = self.cola_pendiente.get()
            self.cola_preparacion.put(pedido_preparar)
        else:
            print("No hay pedidos pendientes")

    def agregar_cola_listo(self):
        if not self.cola_preparacion.empty():
            a = self.cola_preparacion.get()
            self.cola_listo_servir.put(a)
            print("El producto esta listo")

def ordenamientoBurbuja(lista):
    n=len(lista)
    for i in range(n):
        for j in range(0,n-i-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]

modi_pizza = ModificacionPizza()
modi_bebida = ModificacionBebida()
modi_complemento = ModificacionComplemento()
modi_oferta=ModificacionOfertas()

agre_cliente = ListaClientes()

pizza = Pizza(1, "Orilla Queso", 45, 5)
modi_pizza.agregar_pizza(pizza)
pizza = Pizza(2, "5 Carnes", 45, 5)
modi_pizza.agregar_pizza(pizza)
pizza = Pizza(3, "Hawaiana", 45, 5)
modi_pizza.agregar_pizza(pizza)
pizza = Pizza(4, "Peperoni", 45, 5)
modi_pizza.agregar_pizza(pizza)
pizza = Pizza(5, "Vegetariano", 45, 5)
modi_pizza.agregar_pizza(pizza)
pizza = Pizza(6, "Jamon", 45, 5)
modi_pizza.agregar_pizza(pizza)
pizza = Pizza(7, "Queso", 45, 5)
modi_pizza.agregar_pizza(pizza)

bebida = Bebidas(1, "Coca Cola", 5, 5)
modi_bebida.agregar_bebida(bebida)
bebida = Bebidas(2, "Sprite", 5, 5)
modi_bebida.agregar_bebida(bebida)
bebida = Bebidas(3, "Fanta", 5, 5)
modi_bebida.agregar_bebida(bebida)
bebida = Bebidas(4, "Powerade", 5, 5)
modi_bebida.agregar_bebida(bebida)
bebida = Bebidas(5, "Te Lipton", 5, 5)
modi_bebida.agregar_bebida(bebida)

complemento = Complementos(1, "Parmesan Bites", 20, 5)
modi_complemento.agregar_complemento(complemento)
complemento = Complementos(2, "Chessy Bread", 20, 5)
modi_complemento.agregar_complemento(complemento)


colas = Colas()
timer = RepeatTimer(22, colas.agregar_cola_listo)
timer.start()

id_pizza = 7
id_bebida = 5
id_complemento = 2
id_oferta=0

hay_oferta=0
hay_name = 0
hay_nit = 0
hay_compra=0

while True:
    Salir_Usuario = False
    Salir_Administrador = False
    usuario = input("\033[1;34mIngresar como: \n  1. Administrador\n  2. Usuario\n  3. Salir programa\nIngrese opcion: ")
    if usuario == "1":
        contrasena = input("Ingrese la contraseña: \033[0;m")
        if contrasena == "1234":
            print("\033[1;33mUsted a ingresado como administrador")
            while not Salir_Administrador:
                print("1. Agregar productos\n2. Modificar productos\n3. Ver clientes guardos\n4. Salir")
                opcion = input("Que desea escoger: ")
                print("____________________________________________________________________________")
                if opcion == "1":
                    seguir_agregando = False
                    while not seguir_agregando:
                        print("Opciones a agregar:\n1. Pizza\n2. Bebidas\n3. Complementos\n4. Ofertas")
                        opcion_agregar = input("Que desea agregar: ")
                        if opcion_agregar == "1":
                            id_pizza = id_pizza + 1
                            produc = input("Que clase de pizza quiere agregar: ")
                            exepcion = False
                            while not exepcion:
                                try:
                                    preci = int(input("Que precio va a tener la pizza: "))
                                except ValueError:
                                    print("Solo pueden ir numeros en este apartado")
                                else:
                                    exepcion = True
                            exepcion = False
                            while not exepcion:
                                try:
                                    cantidad = int(input("Que cantidad tendra: "))
                                except ValueError:
                                    print("Solo pueden ir numeros en este apartado")
                                else:
                                    exepcion = True
                            pizza = Pizza(id_pizza, produc, preci, cantidad)
                            modi_pizza.agregar_pizza(pizza)
                            print("Se ha guardado exitosamente la pizza")
                        elif opcion_agregar == "2":
                            id_bebida = id_bebida + 1
                            produc = input("Que clase de bebida quiere agregar: ")
                            exepcion = False
                            while not exepcion:
                                try:
                                    preci = int(input("Que precio va a tener la bebida: "))
                                except ValueError:
                                    print("Solo pueden ir numeros en este apartado")
                                else:
                                    exepcion = True
                            exepcion = False
                            while not exepcion:
                                try:
                                    cantidad = int(input("Que cantidad tendra: "))
                                except ValueError:
                                    print("Solo pueden ir numeros en este apartado")
                                else:
                                    exepcion = True
                            bebida = Bebidas(id_bebida, produc, preci, cantidad)
                            modi_bebida.agregar_bebida(bebida)
                            print("Se ha guardado exitosamente la bebida")
                        elif opcion_agregar == "3":
                            id_complemento = id_complemento + 1
                            produc = input("Que clase de complemento quiere agregar: ")
                            exepcion = False
                            while not exepcion:
                                try:
                                    preci = int(input("Que precio va a tener el complemento: "))
                                except ValueError:
                                    print("Solo pueden ir numeros en este apartado")
                                else:
                                    exepcion = True
                            exepcion = False
                            while not exepcion:
                                try:
                                    cantidad = int(input("Que cantidad tendra: "))
                                except ValueError:
                                    print("Solo pueden ir numeros en este apartado")
                                else:
                                    exepcion = True
                            complemento = Complementos(id_complemento, produc, preci, cantidad)
                            modi_complemento.agregar_complemento(complemento)
                            print("Se ha guardado exitosamente el complemento")
                        elif opcion_agregar=="4":
                            id_oferta = id_oferta + 1
                            produc = input("Que clase de oferta quiere agregar: ")
                            exepcion = False
                            while not exepcion:
                                try:
                                    preci = int(input("Que precio va a tener la oferta: "))
                                except ValueError:
                                    print("Solo pueden ir numeros en este apartado")
                                else:
                                    exepcion = True
                            exepcion = False
                            while not exepcion:
                                try:
                                    cantidad = int(input("Que cantidad tendra: "))
                                except ValueError:
                                    print("Solo pueden ir numeros en este apartado")
                                else:
                                    exepcion = True
                            oferta = Ofertas(id_oferta, produc, preci, cantidad)
                            modi_oferta.agregar_oferta(oferta)
                            hay_oferta=1
                            print("Se ha guardado exitosamente la oferta")
                        else:
                            print("Opcion invalida")
                        desea_seguir_agregando = input("1. Si\n2. No\nDesea seguir agregando productos: ")
                        while desea_seguir_agregando != "1" and desea_seguir_agregando != "2":
                            desea_seguir_agregando = input(
                                "Opcion invalida\n1. Si\n2. No\n Desea seguir agregando productos: ")
                        print("____________________________________________________________________________")
                        if desea_seguir_agregando == "2":
                            seguir_agregando = True


                elif opcion == "2":
                    print("1. Pizzas\n2. Bebidas\n3. Complementos\n4. Ofertas")
                    modificar = input("Que desea modificar: ")
                    if modificar == "1":
                        for pizza in modi_pizza.pila_pizza:
                            print(f"{pizza.id}. Producto: {pizza.producto}")
                        exepcion = False
                        while not exepcion:
                            try:
                                pizza_modificar = int(input("Que pizza quiere modificar: "))
                            except ValueError:
                                print("Opcion invalida, solo se permien numeros")
                            else:
                                exepcion = True
                        for pizza in modi_pizza.pila_pizza:
                            if pizza_modificar == pizza.id:
                                Modificar_nombre=input("1. Si\n2. No\n Desea modificar el nombre de la pizza: ")
                                while Modificar_nombre!="1" and Modificar_nombre!="2":
                                    Modificar_nombre=input("Opcion invalida\n1. Si\n2. No\n Desea modifica el nombre de la pizza: ")
                                if Modificar_nombre=="1":
                                    pizza.producto=input("Que nombre le desea poner a la pizza: ")
                                exepcion = False
                                while not exepcion:
                                    try:
                                        pizza.precio = float(input("Que precio desea ponerle: "))
                                    except ValueError:
                                        print("Solo se permiten numeros")
                                    else:
                                        exepcion = True
                                exepcion = False
                                while not exepcion:
                                    try:
                                        pizza.stock = int(input("Cuanto stock hay: "))
                                    except ValueError:
                                        print("Solo se permiten numeros")
                                    else:
                                        exepcion = True
                    elif modificar == "2":
                        for bebida in modi_bebida.pila_bebida:
                            print(f"{bebida.id}. Producto: {bebida.producto}")
                        exepcion = False
                        while not exepcion:
                            try:
                                bebida_modificar = int(input("Que bebida quiere modificar: "))
                            except ValueError:
                                print("Opcion invalida, solo se permien numeros")
                            else:
                                exepcion = True
                        for bebida in modi_bebida.pila_bebida:
                            if bebida_modificar == bebida.id:
                                Modificar_nombre = input("1. Si\n2. No\n Desea modificar el nombre de la bebida: ")
                                while Modificar_nombre != "1" and Modificar_nombre != "2":
                                    Modificar_nombre = input(
                                        "Opcion invalida\n1. Si\n2. No\n Desea modificar el nombre de la bebida: ")
                                if Modificar_nombre == "1":
                                    bebida.producto = input("Que nombre le desea poner a la bebida: ")
                                exepcion = False
                                while not exepcion:
                                    try:
                                        bebida.precio = float(input("Que precio desea ponerle: "))
                                    except ValueError:
                                        print("Solo se permiten numeros")
                                    else:
                                        exepcion = True
                                exepcion = False
                                while not exepcion:
                                    try:
                                        bebida.stock = int(input("Cuanto stock hay: "))
                                    except ValueError:
                                        print("Solo se permiten numeros")
                                    else:
                                        exepcion = True
                    elif modificar == "3":
                        for complemento in modi_complemento.pila_complemento:
                            print(f"{complemento.id}. Producto: {complemento.producto}")
                        exepcion = False
                        while not exepcion:
                            try:
                                complemento_modificar = int(input("Que complemento quiere modificar: "))
                            except ValueError:
                                print("Opcion invalida, solo se permien numeros")
                            else:
                                exepcion = True
                        for complemento in modi_complemento.pila_complemento:
                            if complemento_modificar == complemento.id:
                                Modificar_nombre = input("1. Si\n2. No\n Desea modificar el nombre de la complemento: ")
                                while Modificar_nombre != "1" and Modificar_nombre != "2":
                                    Modificar_nombre = input(
                                        "Opcion invalida\n1. Si\n2. No\n Desea modificar el nombre de la complemento: ")
                                if Modificar_nombre == "1":
                                    complemento.producto = input("Que nombre le desea poner a la complemento: ")
                                exepcion = False
                                while not exepcion:
                                    try:
                                        complemento.precio = float(input("Que precio desea ponerle: "))
                                    except ValueError:
                                        print("Solo se permiten numeros")
                                    else:
                                        exepcion = True
                                exepcion = False
                                while not exepcion:
                                    try:
                                        complemento.stock = int(input("Cuanto stock hay: "))
                                    except ValueError:
                                        print("Solo se permiten numeros")
                                    else:
                                        exepcion = True
                    elif modificar == "4":
                        if hay_oferta==1:
                            for oferta in modi_oferta.pila_oferta:
                                print(f"{oferta.id}. Producto: {oferta.producto}")
                            exepcion = False
                            while not exepcion:
                                try:
                                    oferta_modificar = int(input("Que oferta quiere modificar: "))
                                except ValueError:
                                    print("Opcion invalida, solo se permien numeros")
                                else:
                                    exepcion = True
                            for oferta in modi_oferta.pila_oferta:
                                if oferta_modificar == oferta.id:
                                    Modificar_nombre = input("1. Si\n2. No\nDesea modificar el nombre de la oferta: ")
                                    while Modificar_nombre != "1" and Modificar_nombre != "2":
                                        Modificar_nombre = input(
                                            "Opcion invalida\n1. Si\n2. No\nDesea modificar el nombre de la oferta: ")
                                    if Modificar_nombre == "1":
                                        oferta.producto = input("Que nombre le desea poner a la oferta: ")
                                    exepcion = False
                                    while not exepcion:
                                        try:
                                            oferta.precio = float(input("Que precio desea ponerle: "))
                                        except ValueError:
                                            print("Solo se permiten numeros")
                                        else:
                                            exepcion = True
                                    exepcion = False
                                    while not exepcion:
                                        try:
                                            oferta.stock = int(input("Cuanto stock hay: "))
                                        except ValueError:
                                            print("Solo se permiten numeros")
                                        else:
                                            exepcion = True
                        else:
                            print("No hay ofertas disponibles aun")
                        print("____________________________________________________________________________")
                elif opcion == "3":
                    numeros_clientes = agre_cliente.lista_vacia()
                    if numeros_clientes == 0:
                        print("No hay clientes aun")
                    else:
                        agre_cliente.mostrar()
                    print("____________________________________________________________________________")
                elif opcion == "4":
                    print("Saliendo al menu principal...")
                    Salir_Administrador = True
                else:
                    print("Opcion no valida")
        else:
            print("Contraseña incorrecta")


    elif usuario == "2":
        print("\033[0;m")
        while not Salir_Usuario:
            print("\033[1;32m--Interfaz--")
            print("1. Mostar el menu\n2. Comprar\n3. Pedidos\n4. Salir ")
            opcion = input("Que desea escoger: ")
            print("____________________________________________________________________________")
            if opcion == "1":
                print("1. Pizzas: ")
                for pizza in modi_pizza.pila_pizza:
                    print(f"    {pizza.id}. {pizza.producto}   Precio: {pizza.precio}   Stock: {pizza.stock}")
                print("2. Bebidas: ")
                for bebida in modi_bebida.pila_bebida:
                    print(f"    {bebida.id}. {bebida.producto}   Precio: {bebida.precio}   Stock: {bebida.stock}")
                print("3. Complementos: ")
                for complemento in modi_complemento.pila_complemento:
                    print(
                        f"    {complemento.id}. {complemento.producto}   Precio: {complemento.precio}   Stock: {complemento.stock}")
                print("4. Ofertas: ")
                if hay_oferta==1:
                    for oferta in modi_oferta.pila_oferta:
                        print(f"{oferta.id}. {oferta.producto}   Precio: {oferta.precio}   Stock: {oferta.stock}")
                else:
                    print("No hay ofertas disponibles aun")
                print("____________________________________________________________________________")
            elif opcion == "2":
                Seguir_comprando = False
                compra_factura = []
                total = 0
                while not Seguir_comprando:
                    hay_compra = 0
                    print("1. Pizzas\n2. Bebidas\n3. Complementos\n4. Oferta")
                    compra = input("Que desea agregar a la compra: ")
                    if compra == "1":
                        for pizza in modi_pizza.pila_pizza:
                            print(f"{pizza.id}. Producto: {pizza.producto}")
                        exepcion = False
                        while not exepcion:
                            try:
                                pizza_comprar = int(input("Que pizza quiere comprar: "))
                            except ValueError:
                                print("Opcion invalida, solo se permien numeros")
                            else:
                                exepcion = True
                        for pizza in modi_pizza.pila_pizza:
                            if pizza_comprar == pizza.id:
                                if pizza.stock>0:
                                    pizza.stock = pizza.stock - 1
                                    pedido = pizza.precio,pizza.producto
                                    print(pedido)
                                    total = total + pizza.precio
                                    compra_factura.append(pedido)
                                    colas.agregar_cola_pendiente(pedido)
                                else:
                                    print("No hay este producto")
                    elif compra == "2":
                        for bebida in modi_bebida.pila_bebida:
                            print(f"{bebida.id}. Producto: {bebida.producto}")
                        exepcion = False
                        while not exepcion:
                            try:
                                bebida_comprar = int(input("Que bebida quiere comprar: "))
                            except ValueError:
                                print("Opcion invalida, solo se permien numeros")
                            else:
                                exepcion = True
                        for bebida in modi_bebida.pila_bebida:
                            if bebida_comprar == bebida.id:
                                if bebida.stock>0:
                                    bebida.stock = bebida.stock - 1
                                    pedido = bebida.precio,bebida.producto
                                    print(pedido)
                                    total = total + bebida.precio
                                    compra_factura.append(pedido)
                                    colas.agregar_cola_pendiente(pedido)
                                else:
                                    print("No hay estre producto")
                    elif compra == "3":
                        for complemento in modi_complemento.pila_complemento:
                            print(f"{complemento.id}. Producto: {complemento.producto}")
                        exepcion = False
                        while not exepcion:
                            try:
                                complemento_comprar = int(input("Que complemento quiere comprar: "))
                            except ValueError:
                                print("Opcion invalida, solo se permien numeros")
                            else:
                                exepcion = True
                        for complemento in modi_complemento.pila_complemento:
                            if complemento_comprar == complemento.id:
                                if complemento.stock>0:
                                    complemento.stock = complemento.stock - 1
                                    pedido = complemento.precio,complemento.producto
                                    print(pedido)
                                    total = total + complemento.precio
                                    compra_factura.append(pedido)
                                    colas.agregar_cola_pendiente(pedido)
                                else:
                                    print("No hay este producto")
                    elif compra == "4":
                        if hay_oferta==1:
                            for oferta in modi_oferta.pila_oferta:
                                print(f"{oferta.id}. Producto: {oferta.producto}")
                            exepcion = False
                            while not exepcion:
                                try:
                                    oferta_comprar = int(input("Que oferta quiere comprar: "))
                                except ValueError:
                                    print("Opcion invalida, solo se permien numeros")
                                else:
                                    exepcion = True
                            for oferta in modi_oferta.pila_oferta:
                                if oferta_comprar == oferta.id:
                                    if oferta.stock>0:
                                        oferta.stock = oferta.stock - 1
                                        pedido = oferta.precio,oferta.producto
                                        print(pedido)
                                        total = total + oferta.precio
                                        compra_factura.append(pedido)
                                        colas.agregar_cola_pendiente(pedido)
                                    else:
                                        print("No hay este producto")
                        else:
                            print("No hay ofertas ")
                            hay_compra=1
                    else:
                        print("Opcion invalida")
                        hay_compra = 1
                    seguir_comprando = input("1. Si\n2. No\nDesea seguir comprando algun pedido: ")
                    while seguir_comprando != "1" and seguir_comprando != "2":
                        print("Opcion invalida")
                        seguir_comprando = input("1. Si\n2. No\nDesea seguir comprando algun pedido: ")
                    print("____________________________________________________________________________")
                    if seguir_comprando == "2":
                        Seguir_comprando = True
                        if hay_compra == 0:
                            cf_nit = input('1.- NIT \n 2.- C/F \n Por favor, ingrese una opcion: ')
                            if cf_nit == '1':
                                nit = input('Ingrese el NIT: ')
                                hay_nit = 1
                                modo = input(
                                    '1.- Pago con tarjeta \n 2.- Pago en efectivo \n Por favor, elija su forma de pago: ')
                                if modo == '1':
                                    name = input('Ingrese nombre para realizar la factura: ')
                                    hay_name = 1
                                    iva = (total * 0.12) + total

                                    ordenamientoBurbuja(compra_factura)

                                    print(
                                        f'Factura \n Nombre: {name} \n Numero de identificacion tributaria (NIT): {nit} \n '
                                        f'{compra_factura} \n Subtotal a pagar: Q.{total} \n Total a pagar (con IVA incluido): '
                                        f'Q.{iva} \n Pago con tarjeta')
                                elif modo == '2':
                                    name = input('Ingrese nombre para realizar la factura: ')
                                    iva = (total * 0.12) + total
                                    print(
                                        f'Factura \n Nombre: {name} \n Numero de identificacion tributaria (NIT): {nit} \n '
                                        f'{compra_factura} \n Subtotal a pagar: Q.{total} \n Total a pagar (con IVA incluido): '
                                        f'Q.{iva} \n Pago con efectivo')
                            elif cf_nit == '2':
                                modo = input(
                                    '1.- Pago con tarjeta \n 2.- Pago en efectivo \n Por favor, elija su forma de pago: ')
                                if modo == '1':
                                    iva = (total * 0.12) + total
                                    print(
                                        f'{compra_factura} \n Subtotal a pagar: Q.{total} \n Total a pagar (con IVA incluido): '
                                        f'Q.{iva} \n Pago con tarjeta')
                                elif modo == '2':
                                    iva = (total * 0.12) + total
                                    print(
                                        f'{compra_factura} \n'
                                        f'Subtotal a pagar: Q.{total} \n Total a pagar (con IVA incluido): '
                                        f'Q.{iva} \n Pago con efectivo')
                            if hay_nit == 1 and hay_name == 1:
                                cliente = nit, name
                                agre_cliente.agregar_clientes(cliente)
                print("____________________________________________________________________________")

            elif opcion == "3":
                print("Pedidos pendientes")
                pedido_pendiente = list(colas.cola_pendiente.queue)
                for i, pedido in enumerate(pedido_pendiente):
                    print(f"    {i + 1}. {pedido[1]} Q{pedido[0]}")
                print("Pedidos en preparacion")
                pedido_preparacion = list(colas.cola_preparacion.queue)
                for i, pedido in enumerate(pedido_preparacion):
                    print(f"    {i + 1}. {pedido[1]} Q{pedido[0]}")
                print("Pedidos listos")
                pedido_listo = list(colas.cola_listo_servir.queue)
                for i, pedido in enumerate(pedido_listo):
                    print(f"    {i + 1}. {pedido[1]} Q{pedido[0]}")
                print("____________________________________________________________________________")
                preparar = input("1. Si\n2. No\nDesea preparar algun pedido: ")
                if preparar == "1":
                    colas.agregar_cola_preparacion()
                elif preparar == "2":
                    print("No se prepararan pedidos")
                else:
                    print("Opcion invalida")
                print("____________________________________________________________________________")
            elif opcion == "4":
                print("Saliendo al menu principal...")
                Salir_Usuario = True
            else:
                print("Opcion invalida")
        print("____________________________________________________________________________\033[0;m")
    elif usuario == "3":
        break
    else:
        print("\033[1;34m____________________________________________________________________________")
        print("Opcion no valida\nUsuario no identificado")
print("\033[1;31mCerrando el programa...")
timer.cancel()

