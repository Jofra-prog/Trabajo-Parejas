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
