import queue
from threading import Timer


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

class Productos:
    def __init__(self, id, producto, precio, stock):
        self.id=id
        self.producto=producto
        self.precio=precio
        self.stock=stock
class Pizza(Productos):
    def __init__(self,id, producto, precio, stock):
        super(Pizza, self).__init__(id, producto, precio, stock)
class Bebidas(Productos):
    def __init__(self,id, producto, precio, stock):
        super(Bebidas, self).__init__(id, producto, precio, stock)
class Complementos(Productos):
    def __init__(self,id, producto, precio, stock):
        super(Complementos, self).__init__(id, producto, precio, stock)
class ListaClientes:
    def __init__(self):
        self.pila_clientes=[]
    def agregar_clientes(self,clientes):
        self.pila_clientes.append(clientes)
    def lista_vacia(self):
        vacia=len(self.pila_clientes)
        if vacia==0:
            return 0
    def mostrar(self):
        print(self.pila_clientes)

class ModificacionPizza:
    def __init__(self):
        self.pila_pizza=[]
    def agregar_pizza(self, pizzas):
        self.pila_pizza.append(pizzas)
class ModificacionBebida:
    def __init__(self):
        self.pila_bebida=[]
    def agregar_bebida(self, bebidas):
        self.pila_bebida.append(bebidas)
class ModificacionComplemento:
    def __init__(self):
        self.pila_complemento=[]
    def agregar_complemento(self, complementos):
        self.pila_complemento.append(complementos)

class Colas:
    def __init__(self):
        self.cola_pendiente = queue.Queue()
        self.cola_preparacion = queue.Queue()
        self.cola_listo_servir = queue.Queue()
    def agregar_cola_pendiente(self,pedidos):
        self.cola_pendiente.put(pedidos)
    def agregar_cola_preparacion(self):
        if not self.cola_pendiente.empty():
            pedido_preparar = self.cola_pendiente.get()
            self.cola_preparacion.put(pedido_preparar)
        else:
            print("No hay pedidos pendientes")
    def agregar_cola_listo(self):
        if not self.cola_preparacion.empty():
            a=self.cola_preparacion.get()
            self.cola_listo_servir.put(a)
            print("El producto esta listo")


modi_pizza=ModificacionPizza()
modi_bebida=ModificacionBebida()
modi_complemento=ModificacionComplemento()
agre_cliente=ListaClientes()

pizza=Pizza(1,"Orilla Queso",45,5)
modi_pizza.agregar_pizza(pizza)
pizza=Pizza(2,"5 carnes",45,5)
modi_pizza.agregar_pizza(pizza)
pizza=Pizza(3,"Hawaiana",45,5)
modi_pizza.agregar_pizza(pizza)
pizza=Pizza(4,"Peperoni",45,5)
modi_pizza.agregar_pizza(pizza)
pizza=Pizza(5,"Vegetariano",45,5)
modi_pizza.agregar_pizza(pizza)
pizza=Pizza(6,"Jamon",45,5)
modi_pizza.agregar_pizza(pizza)
pizza=Pizza(7,"Queso",45,5)
modi_pizza.agregar_pizza(pizza)

bebida=Bebidas(1,"Coca Cola",5,5)
modi_bebida.agregar_bebida(bebida)
bebida=Bebidas(2,"Sprite",5,5)
modi_bebida.agregar_bebida(bebida)
bebida=Bebidas(3,"Fanta",5,5)
modi_bebida.agregar_bebida(bebida)
bebida=Bebidas(4,"Powerade",5,5)
modi_bebida.agregar_bebida(bebida)
bebida=Bebidas(5,"Te Lipton",5,5)
modi_bebida.agregar_bebida(bebida)

complemento=Complementos(1,"Parmesan Bites",20,5)
modi_complemento.agregar_complemento(complemento)
complemento=Complementos(2,"Chessy Bread",20,5)
modi_complemento.agregar_complemento(complemento)


colas=Colas()
timer=RepeatTimer(22,colas.agregar_cola_listo)
timer.start()

id_pizza=7
id_bebida=5
id_complemento=2

hay_name=0
hay_nit=0


while True:
    Salir_Usuario=False
    Salir_Administrador=False
    usuario=input("Ingresar como: \n1. Administrador\n2. Usuario\n3. Salir programa\nIngrese opcion: ")
    if usuario=="1":
        contrasena=input("Ingrese la contraseña: ")
        if contrasena=="1234":
            print("Usted a ingresado como administrador")
            while not Salir_Administrador:
                print("1. Agregar productos\n2. Modificar productos\n3. Ver clientes guardos\n4. Salir")
                opcion=input("Que desea escoger: ")
                if opcion=="1":
                    seguir_agregando=False
                    while not seguir_agregando:
                        print("Opciones a agregar:\n1. Pizza\n2. Bebidas\n3. Complementos")
                        opcion_agregar=input("Que desea agregar: ")
                        if opcion_agregar=="1":
                            id_pizza=id_pizza+1
                            produc=input("Que clase de pizza quiere agregar: ")
                            exepcion=False
                            while not exepcion:
                                try:
                                    preci=int(input("Que precio va a tener la pizza: "))
                                except ValueError:
                                    print("Solo pueden ir numeros en este apartado")
                                else:
                                    exepcion=True
                            exepcion = False
                            while not exepcion:
                                try:
                                    cantidad = int(input("Que cantidad tendra: "))
                                except ValueError:
                                    print("Solo pueden ir numeros en este apartado")
                                else:
                                    exepcion = True
                            pizza=Pizza(id_pizza,produc,preci,cantidad)
                            modi_pizza.agregar_pizza(pizza)
                            print("Se ha guardado exitosamente la pizza")
                        elif opcion_agregar=="2":
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
                        elif opcion_agregar=="3":
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
                        else:
                            print("Opcion invalida")
                        desea_seguir_agregando=input("1. Si\n2. No\nDesea seguir agregando productos: ")
                        while desea_seguir_agregando!="1" and desea_seguir_agregando!="2":
                            desea_seguir_agregando = input("Opcion invalida\n1. Si\n2. No\n Desea seguir agregando productos: ")
                        if desea_seguir_agregando=="2":
                            seguir_agregando=True
                    else:
                        print("Opcion no valida")
                elif opcion=="2":
                    print("1. Pizzas\n2. Bebidas\n3. Complementos")
                    modificar=input("Que desea modificar: ")
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
                        for pizza in  modi_pizza.pila_pizza:
                            if pizza_modificar==pizza.id:
                                exepcion=False
                                while not exepcion:
                                    try:
                                        pizza.precio=float(input("Que precio desea ponerle: "))
                                    except ValueError:
                                        print("Solo se permiten numeros")
                                    else:
                                        exepcion=True
                                exepcion = False
                                while not exepcion:
                                    try:
                                        pizza.stock=int(input("Cuanto stock hay: "))
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
                elif opcion=="3":
                    numeros_clientes=agre_cliente.lista_vacia()
                    if numeros_clientes==0:
                        print("No hay clientes aun")
                    else:
                        agre_cliente.mostrar()
                elif opcion=="4":
                    print("Saliendo al menu principal...")
                    Salir_Administrador=True
                else:
                    print("Opcion no valida")
        else:
            print("Contraseña incorrecta")


    elif usuario=="2":
        while not Salir_Usuario:
            print("--Interfaz--")
            print("1. Mostar el menu\n2. Comprar\n3. Pedidos\n4. Salir ")
            opcion=input("Que desea escoger: ")
            if opcion=="1":
                print("1. Pizzas: ")
                for pizza in modi_pizza.pila_pizza:
                    print(f"    {pizza.id}. {pizza.producto}   Precio: {pizza.precio}   Stock: {pizza.stock}")
                print("2. Bebidas: ")
                for bebida in modi_bebida.pila_bebida:
                    print(f"    {bebida.id}. {bebida.producto}   Precio: {bebida.precio}   Stock: {bebida.stock}")
                print("3. Complementos: ")
                for complemento in modi_complemento.pila_complemento:
                    print(f"    {complemento.id}. {complemento.producto}   Precio: {complemento.precio}   Stock: {complemento.stock}")
            elif opcion=="2":
                Seguir_comprando = False
                compra_factura=[]
                total=0
                while not Seguir_comprando:
                    hay_compra = 0
                    print("1. Pizzas\n2. Bebidas\n3. Complementos")
                    compra=input("Que desea agregar a la compra: ")
                    if compra=="1":
                        for pizza in  modi_pizza.pila_pizza:
                            print(f"{pizza.id}. Producto: {pizza.producto}")
                        exepcion=False
                        while not exepcion:
                            try:
                                pizza_comprar=int(input("Que pizza quiere comprar: "))
                            except ValueError:
                                print("Opcion invalida, solo se permien numeros")
                            else:
                                exepcion=True
                        for pizza in  modi_pizza.pila_pizza:
                            if pizza_comprar==pizza.id:
                                pizza.stock=pizza.stock-1
                                pedido=pizza.producto,pizza.precio
                                print(pedido)
                                total=total+pizza.precio
                                compra_factura.append(pedido)
                                colas.agregar_cola_pendiente(pedido)
                    elif compra=="2":
                        for bebida in  modi_bebida.pila_bebida:
                            print(f"{bebida.id}. Producto: {bebida.producto}")
                        exepcion = False
                        while not exepcion:
                            try:
                                bebida_comprar = int(input("Que bebida quiere comprar: "))
                            except ValueError:
                                print("Opcion invalida, solo se permien numeros")
                            else:
                                exepcion = True
                        for bebida in  modi_bebida.pila_bebida:
                            if bebida_comprar==bebida.id:
                                bebida.stock=bebida.stock-1
                                pedido=bebida.producto,bebida.precio
                                print(pedido)
                                total = total + bebida.precio
                                compra_factura.append(pedido)
                                colas.agregar_cola_pendiente(pedido)
                    elif compra=="3":
                        for complemento in  modi_complemento.pila_complemento:
                            print(f"{complemento.id}. Producto: {complemento.producto}")
                        exepcion = False
                        while not exepcion:
                            try:
                                complemento_comprar = int(input("Que complemento quiere comprar: "))
                            except ValueError:
                                print("Opcion invalida, solo se permien numeros")
                            else:
                                exepcion = True
                        for complemento in  modi_complemento.pila_complemento:
                            if complemento_comprar==complemento.id:
                                complemento.stock=complemento.stock-1
                                pedido=complemento.producto,complemento.precio
                                print(pedido)
                                total = total + complemento.precio
                                compra_factura.append(pedido)
                                colas.agregar_cola_pendiente(pedido)
                    else:
                        print("Opcion invalida")
                        hay_compra = 1
                    seguir_comprando=input("1. Si\n2. No\nDesea seguir comprando algun pedido: ")
                    while seguir_comprando!="1" and seguir_comprando !="2":
                        print("Opcion invalida")
                        seguir_comprando = input("1. Si\n2. No\nDesea seguir comprando algun pedido: ")
                    if seguir_comprando=="2":
                        Seguir_comprando=True
                        if hay_compra==0:
                            cf_nit = input('1.- NIT \n 2.- C/F \n Por favor, ingrese una opcion: ')
                            if cf_nit == '1':
                                nit = input('Ingrese el NIT: ')
                                hay_nit=1
                                modo = input('1.- Pago con tarjeta \n 2.- Pago en efectivo \n Por favor, elija su forma de pago: ')
                                if modo == '1':
                                    name = input('Ingrese nombre para realizar la factura: ')
                                    hay_name=1
                                    iva = (total*0.12)+total
                                    print(f'Factura \n Nombre: {name} \n Numero de identificacion tributaria (NIT): {nit} \n '
                                          f'{compra_factura} \n Subtotal a pagar: {total} \n Total a pagar (con IVA incluido): '
                                          f'{iva} \n Pago con tarjeta')
                                elif modo == '2':
                                    name = input('Ingrese nombre para realizar la factura: ')
                                    iva = (total * 0.12)+total
                                    print(f'Factura \n Nombre: {name} \n Numero de identificacion tributaria (NIT): {nit} \n '
                                          f'{compra_factura} \n Subtotal a pagar: {total} \n Total a pagar (con IVA incluido): '
                                          f'{iva} \n Pago con efectivo')
                            elif cf_nit == '2':
                                modo = input('1.- Pago con tarjeta \n 2.- Pago en efectivo \n Por favor, elija su forma de pago: ')
                                if modo == '1':
                                    iva = (total * 0.12)+total
                                    print(f'{compra_factura} \n Subtotal a pagar: {total} \n Total a pagar (con IVA incluido): '
                                          f'{iva} \n Pago con tarjeta')
                                elif modo == '2':
                                    iva = (total * 0.12)+total
                                    print(f'{compra_factura} \n Subtotal a pagar: {total} \n Total a pagar (con IVA incluido): '
                                          f'{iva} \n Pago con efectivo')
                            if hay_nit==1 and hay_name==1:
                                cliente=nit,name
                                agre_cliente.agregar_clientes(cliente)


            elif opcion=="3":
                print("Pedidos pendientes")
                pedido_pendiente=list(colas.cola_pendiente.queue)
                for i, pedido in enumerate(pedido_pendiente):
                    print(f"    {i+1}. {pedido[0]} Q{pedido[1]}")
                print("Pedidos en preparacion")
                pedido_preparacion=list(colas.cola_preparacion.queue)
                for i, pedido in enumerate(pedido_preparacion):
                    print(f"    {i+1}. {pedido[0]} Q{pedido[1]}")
                print("Pedidos listos")
                pedido_listo=list(colas.cola_listo_servir.queue)
                for i, pedido in enumerate(pedido_listo):
                    print(f"    {i+1}. {pedido[0]} Q{pedido[1]}")
                preparar=input("1. Si\n2. No\nDesea preparar algun pedido: ")
                if preparar=="1":
                    colas.agregar_cola_preparacion()
                elif preparar=="2":
                    print("No se prepararan pedidos")
                else:
                    print("Opcion invalida")

            elif opcion=="4":
                print("Saliendo al menu principal...")
                Salir_Usuario=True
            else:
                print("Opcion invalida")
    elif usuario=="3":
        break
    else:
        print("Opcion no valida\nUsuario no identificado")
print("Cerrando el programa...")
timer.cancel()

