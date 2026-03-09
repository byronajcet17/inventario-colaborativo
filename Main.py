import Inventario
from Inventario import agregar_productos
menu = """
 ===========================================    
         Administrador de Colección
 ===========================================
1. Añadir un Producto
2. Eliminar productos
3. Ver productos
4. Salir
 ===========================================
 """   
while True:
 print(menu)
 opc = input ("Selecciona una opción: ")
 if opc == "1":
     agregar_productos()
     if opc == "2":
      if opc == "3":
       if opc == "4":
        print("Feliz día")
 break


