#sistema de venta de zapatillas



inventario = {
    "001": {"modelo": "Air Max","precio": 89990, "stock":15},
    "002": {"modelo": "classic","precio": 49990, "stock":50},
    "003": {"modelo": "runner","precio": 69990, "stock":20},
    "004": {"modelo": "basquet","precio": 79990, "stock":5}

}

#Funcion para mostrar el inventario disponible 

def mostrar_inventario():
    print("\n=====INVENTARIO DE ZAPATILLAS======")
    print("codigo | modelo | precio | stock")
    print("-----------------------------------")
   

   #CICLO FOR PARA ITERAR CADA ITEM DEL INVENTARIO
    for codigo,datos in inventario .items():
     print(f"{codigo}   |{datos["modelo"]:8} | ${datos["precio"] } | {datos["stock"]}")
          
def procesar_venta():
   
   mostrar_inventario()
   #preguntar el codigo de producto a vender 

   codigo = input("\n ingrese el codigo de la zapatiila: ")

   if codigo not in inventario: 
       print("Error: el codigo ingresado no existe.")
       return
   
    
    #solicitar la cantidad numerica de zapatillas 
   try:
      cantidad= int(input("ingrese la cantidad de zapatillas a vender: "))
   except ValueError:
      print("Error debe ingresar un numero valido.")
      return   
   

   # validar que exista suficiente stock 


   if cantidad <=0:
      print("Error: la cantidad debe ser mayor a 0.")
      return
   elif cantidad > inventario[codigo]["stock"]:
       print("Error: no hay stock disponible.")
       return
   


   #calcular el valor de la venta 
   precio_unitario = inventario[codigo]["precio"]
   total = precio_unitario * cantidad 
   
   #actualizar el stock del diccionario inventario 
   inventario[codigo]["stock"] -= cantidad


   #generar boleta de compra 

   print("\n----Boleta electronica----")
   print(f"producto : {inventario[codigo]["modelo"]}") 
   print(f"Precio unitario: ${precio_unitario}")
   print(f"cantidad {cantidad}")
   print(f"total a pafar: ${total}")
   print("-----------------------------") 
   print("Gracias por su compra.")
procesar_venta()      