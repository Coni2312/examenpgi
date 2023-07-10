from os import system
system("cls")

ubicaciones_platinum =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

ubicaciones_gold =[21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 48, 50]

ubicaciones_silver = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
71, 72, 73, 74, 75, 76, 77,78, 79, 80,
81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

reserva = [None]*100

rut_reservador = [None]*100


def pausa():
    input("presione una tecla para salir...")
    system("cls")
    return

def precios_asientos():
    print("\nLOS VALORES SON: ")
    print("1. Platinum: $120.000 (asientos del 1 al 20)")
    print("2. Gold: $80.000 (asientos del 21 al 50)")
    print("3. Silver: $80.000 (asientos del 51 al 100)")

def comprar_entradas():             
    while True:
        ubicacion = int(input("¿cuantas entradas desea comprar?: "))
        for i in range(ubicacion):            
            num_entradas = int(input("¿que asiento desea comprar?: "))         
        if num_entradas > 0 and num_entradas <= 100 and ubicaciones_platinum[(int(num_entradas))-1] != "x":
            ubicaciones_platinum.remove(num_entradas)
            ubicaciones_platinum.insert((ubicacion - 1), "x")
            reserva.insert((num_entradas - 1), reserva)
            rut_reservador[num_entradas-1] = int(input("ingrese rut de la persona que compra: "))
            print("la entrada numero: ",num_entradas, "por el cliente: ", rut_reservador, "ha sido exitosa")
            break
        
                

def mostrar_ubicaciones_disponibles(rut_reservador, ubicacion):
    print("Las entradas reservadas son las siguientes: ", rut_reservador, ubicacion)      




                        
                   
        
print("**************** CONCIERTO MICHAEL JAM ****************")

print("""
1. Comprar entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir""")

op = str(input("Seleccione una opcion: "))

match op:
    case "1": 
        print("************* ESCENARIO ************* ")
        entradas_disponibles1 = " | ".join(str(n)for n in ubicaciones_platinum)
        entradas_disponibles2 = " | ".join(str(n)for n in ubicaciones_gold)
        entradas_disponibles3 = " | ".join(str(n)for n in ubicaciones_silver)
        
        print(entradas_disponibles1)
        print(entradas_disponibles2)
        print(entradas_disponibles3)

        precios_asientos()

        print("\nminimo entradas a comprar:1, maximo entradas a comprar: 3")

        comprar_entradas()
        pausa()

    case "2":
        print("Las ubicaciones disponibles son:")
        mostrar_ubicaciones_disponibles()
        

    case "3":
        print

    case "4":
        print

    case "5":
        print 


    case other:
        print("opcion no valida... ")











