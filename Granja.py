#Cuantos litros de leche se producen por semana en la granja
import math
def produccion_leche(V, K, X):
    produccion_leche_por_dia = (V * X) / K
    produccion_leche_por_semana = produccion_leche_por_dia * 7
    return produccion_leche_por_semana

# le pedimos los datos al usuario
V = int(input("Ingrese el número de vacas: "))
K = float(input("Ingrese la cantidad de metros cuadrados de pasto necesarios para producir 1 litro de leche: "))
X = float(input("Ingrese la cantidad de litros de leche que produce una vaca por día: "))

# resultado final
produccion_leche_semanal = produccion_leche(V, K, X)
print("La producción de leche semanal es de:", produccion_leche_semanal, "litros")


#Cuantos huevos producen

av = int(input("Ingrese la cantidad de aves que hay en la granja"))
d = int(input("Ingrese en la cantidad de dias en los que quiere saber la producción"))

ga = av/3
pmg = ga/2
smga = ga - pmg

hv = pmg*d/3
hv2 = smga*d/5

#math.trunc es para sacar la parte entera de ese numero y que no de todos los numeros despues del punto
print(f"la produccion de huevos en {d} dias es de\n {math.trunc(hv + hv2)}")