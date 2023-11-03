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

pizza=Pizza(1,"Orilla Queso","45",5)
modi_pizza.agregar_pizza(pizza)
pizza=Pizza(2,"5 carnes","45",5)
modi_pizza.agregar_pizza(pizza)
pizza=Pizza(3,"Hawaiana","45",5)
modi_pizza.agregar_pizza(pizza)
pizza=Pizza(4,"Peperoni","45",5)
modi_pizza.agregar_pizza(pizza)
pizza=Pizza(5,"Vegetariano","45",5)
modi_pizza.agregar_pizza(pizza)
pizza=Pizza(6,"Jamon","45",5)
modi_pizza.agregar_pizza(pizza)
pizza=Pizza(7,"Queso","45",5)
modi_pizza.agregar_pizza(pizza)

bebida=Bebidas(1,"Coca Cola","5",5)
modi_bebida.agregar_bebida(bebida)
bebida=Bebidas(2,"Sprite","5",5)
modi_bebida.agregar_bebida(bebida)
bebida=Bebidas(3,"Fanta","5",5)
modi_bebida.agregar_bebida(bebida)
bebida=Bebidas(4,"Powerade","5",5)
modi_bebida.agregar_bebida(bebida)
bebida=Bebidas(5,"Te Lipton","5",5)
modi_bebida.agregar_bebida(bebida)

complemento=Complementos(1,"Parmesan Bites","5",5)
modi_complemento.agregar_complemento(complemento)
complemento=Complementos(2,"Chessy Bread","5",5)
modi_complemento.agregar_complemento(complemento)


colas=Colas()
timer=RepeatTimer(22,colas.agregar_cola_listo)
timer.start()
while True:
    print("--Interfaz--")
    print("1. Mostar el menu\n2. Comprar\n3. Pedidos\n4. Salir")
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
        print("1. Pizzas\n2. Bebidas\n3. Complementos")
        compra=input("Que desea agregar a la compra: ")
        if compra=="1":
            for pizza in  modi_pizza.pila_pizza:
                print(f"{pizza.id}. Producto: {pizza.producto}")
            pizza_comprar=int(input("Que pizza quiere comprar: "))
            for pizza in  modi_pizza.pila_pizza:
                if pizza_comprar==pizza.id:
                    pizza.stock=pizza.stock-1
                    pedido=pizza.producto,pizza.precio
                    print(pedido)
                    colas.agregar_cola_pendiente(pedido)
        elif compra=="2":
            for bebida in  modi_bebida.pila_bebida:
                print(f"{bebida.id}. Producto: {bebida.producto}")
            bebida_comprar=int(input("Que pizza quiere comprar: "))
            for bebida in  modi_bebida.pila_bebida:
                if bebida_comprar==bebida.id:
                    bebida.stock=bebida.stock-1
                    pedido=bebida.producto,bebida.precio
                    print(pedido)
                    colas.agregar_cola_pendiente(pedido)
        elif compra=="3":
            for complemento in  modi_complemento.pila_complemento:
                print(f"{complemento.id}. Producto: {complemento.producto}")
            complemento_comprar=int(input("Que pizza quiere comprar: "))
            for complemento in  modi_complemento.pila_complemento:
                if complemento_comprar==complemento.id:
                    complemento.stock=complemento.stock-1
                    pedido=complemento.producto,complemento.precio
                    print(pedido)
                    colas.agregar_cola_pendiente(pedido)
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
        print("Cerrando el programa...")
        timer.cancel()
        break
    else:
        print("Opcion invalida")
