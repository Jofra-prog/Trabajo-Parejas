
manzanas = 2000
papayas = 6000
bananos = 300

op = int(input("Ingrese 1 para ingresar una nueva compra o 0 para cerrar el programa"))

while op == 1:
 
 print("Bienvenido a tiendas triple B (BUENO BONITO Y BARATO)")

 cm = float(input("ingrese la cantidad de manzanas que desea llevar"))
 cpa = float(input("ingrese la cantidad de papayas que desea llevar")) 
 cb = float(input("ingrese la cantidad de bananos que desea llevar"))

 def descuentos(c,p):
    if c < 6:
       return c*p
    elif 6 <= c < 11:
       return p*(c-c*0.05)
    elif 11 <= c < 21:
       return p*(c-c*0.1)
    else:
       return p*(c-c*0.2)

 def cantidad_de_descuento(p):
    if p < 6:
       return"ninguno"
    elif 6 <= p < 11:
       return"5%"
    elif 11 <= p < 21:
       return"10%"
    else:
       return"20%"
 
 
 print(f"el total de la compra es:\n {descuentos(cm,manzanas) + descuentos(cpa,papayas) + descuentos(cb,bananos)}")
 print (f"y los descuentos aplicados son:\n Manzanas: {cantidad_de_descuento(cm)}\n Papayas: {cantidad_de_descuento(cpa,)}\n Bananos: {cantidad_de_descuento(cb)}")
 
 op = int(input("Ingrese 1 para ingresar una nueva compra o 0 para cerrar el programa"))


#hdudidi

