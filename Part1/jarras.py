# ==================== Operadores ====================
# Llenar jarra de 8 litros con la bomba
def LlenarJarra8Bomba(estado_actual):
    print("Llenar jarra de 8 litros con la bomba")
    (x,y,z) = estado_actual
    if z < 8:
        estado_nuevo = (x,y,8)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual

# Llenar jarra de 5 litros con la bomba
def LlenarJarra5Bomba(estado_actual):
    print("Llenar jarra de 5 litros con la bomba")
    (x,y,z) = estado_actual
    if y < 5:
        estado_nuevo = (x,5,z)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# Llenar jarra de 3 litros con la bomba
def LlenarJarra3Bomba(estado_actual):
    print("Llenar jarra de 3 litros con la bomba")
    (x,y,z) = estado_actual
    if x < 3:
        estado_nuevo = (3,y,z)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual

# Vaciar jarra de 8 litros en el suelo
def VaciarJarra8Suelo(estado_actual):
    print("Vaciar jarra de 8 litros en el suelo")
    (x,y,z) = estado_actual
    if z > 0 and z <= 8:
        estado_nuevo = (x,y,0)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# Vaciar jarra de 5 litros en el suelo
def VaciarJarra5Suelo(estado_actual):
    print("Vaciar jarra de 5 litros en el suelo")
    (x,y,z) = estado_actual
    if y > 0 and y <= 5:
        estado_nuevo = (x,0,z)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# Vaciar jarra de 3 litros en el suelo
def VaciarJarra3Suelo(estado_actual):
    print("Vaciar jarra de 3 litros en el suelo")
    (x,y,z) = estado_actual
    if y > 0 and y <= 3:
        estado_nuevo = (0,y,z)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# Llenar jarra de 8 litros con jarra de 5 litros
def LlenarJarra8ConJarra5(estado_actual):
    print("Llenar jarra de 8 litros con jarra de 5 litros")
    (x,y,z) = estado_actual
    if z < 8 and y > 0 and (z+y) >= 8:
        estado_nuevo = (x,z+y-8,8)
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# Llenar jarra de 8 litros con jarra de 3 litros
def LlenarJarra8ConJarra3(estado_actual):
    print("Llenar jarra de 8 litros con jarra de 3 litros")
    (x,y,z) = estado_actual
    if z < 8 and x > 0 and (z+x) >= 8:
        estado_nuevo = (z+x-8,y,8)
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# Llenar jarra de 5 litros con jarra de 8 litros
def LlenarJarra5ConJarra8(estado_actual):
    print("Llenar jarra de 5 litros con jarra de 8 litros")
    (x,y,z) = estado_actual
    if y < 5 and z > 0 and (y+z) >= 5:
        estado_nuevo = (x,5,z+y-5)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# Llenar jarra de 5 litros con jarra de 3 litros
def LlenarJarra5ConJarra3(estado_actual):
    print("Llenar jarra de 5 litros con jarra de 3 litros")
    (x,y,z) = estado_actual
    if y < 5 and x > 0 and (y+x) >= 5:
        estado_nuevo = (x+y-5,5,z)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# Llenar jarra de 3 litros con jarra de 8 litros
def LlenarJarra3ConJarra8(estado_actual):
    print("Llenar jarra de 3 litros con jarra de 8 litros")
    (x,y,z) = estado_actual
    if x < 3 and z > 0 and (x+z) >= 3:
        estado_nuevo = (3,y,x+z-3)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# Llenar jarra de 3 litros con jarra de 5 litros
def LlenarJarra3ConJarra5(estado_actual):
    print("Llenar jarra de 3 litros con jarra de 5 litros")
    (x,y,z) = estado_actual
    if x < 3 and y > 0 and (x+y) >= 3:
        estado_nuevo = (3,x+y-3,z)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# Vaciar jarra de 8 litros en jarra de 5 litros
def VaciarJarra8EnJarra5(estado_actual):
    print("Vaciar jarra de 8 litros en jarra de 5 litros")
    (x,y,z) = estado_actual
    if z > 0 and (y+z) <= 5:
        estado_nuevo = (x,y+z,0)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# Vaciar jarra de 8 litros en jarra de 3 litros
def VaciarJarra8EnJarra3(estado_actual):
    print("Vaciar jarra de 8 litros en jarra de 3 litros")
    (x,y,z) = estado_actual
    if z > 0 and (x+z) <= 3:
        estado_nuevo = (x+z,y,0)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# Vaciar jarra de 5 litros en jarra de 8 litros
def VaciarJarra5EnJarra8(estado_actual):
    print("Vaciar jarra de 5 litros en jarra de 8 litros")
    (x,y,z) = estado_actual
    if y > 0 and (z+y) <= 8:
        estado_nuevo = (x,0,z+y)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# Vaciar jarra de 5 litros en jarra de 3 litros
def VaciarJarra5EnJarra3(estado_actual):
    print("Vaciar jarra de 5 litros en jarra de 3 litros")
    (x,y,z) = estado_actual
    if y > 0 and (x+y) <= 3:
        estado_nuevo = (x+y,0,z)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# Vaciar jarra de 3 litros en jarra de 8 litros
def VaciarJarra3EnJarra8(estado_actual):
    print("Vaciar jarra de 3 litros en jarra de 8 litros")
    (x,y,z) = estado_actual
    if x > 0 and (x+z) <= 8:
        estado_nuevo = (0,y,x+z)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# Vaciar jarra de 3 litros en jarra de 5 litros
def VaciarJarra3EnJarra5(estado_actual):
    print("Vaciar jarra de 3 litros en jarra de 5 litros")
    (x,y,z) = estado_actual
    if x > 0 and (x+y) <= 5:
        estado_nuevo = (0,x+y,z)
        global pasos
        pasos += 1
        return estado_nuevo
    else:
        print("No se puede aplicar operador")
        return estado_actual
        
# =================== Menu ======================
def print_menu():
    print("------------------------------------------")
    print("1. Llenar jarra de 8 litros con la bomba")
    print("2. Llenar jarra de 5 litros con la bomba")
    print("3. Llenar jarra de 3 litros con la bomba")
    print("4. Vaciar jarra de 8 litros en el suelo")
    print("5. Vaciar jarra de 5 litros en el suelo")
    print("6. Vaciar jarra de 3 litros en el suelo")
    print("7. Llenar jarra de 8 litros con jarra de 5 litros")
    print("8. Llenar jarra de 8 litros con jarra de 3 litros")
    print("9. Llenar jarra de 5 litros con jarra de 8 litros")
    print("10. Llenar jarra de 5 litros con jarra de 3 litros")
    print("11. Llenar jarra de 3 litros con jarra de 8 litros")
    print("12. Llenar jarra de 3 litros con jarra de 5 litros")
    print("13. Vaciar jarra de 8 litros en jarra de 5 litros")
    print("14. Vaciar jarra de 8 litros en jarra de 3 litros")
    print("15. Vaciar jarra de 5 litros en jarra de 8 litros")
    print("16. Vaciar jarra de 5 litros en jarra de 3 litros")
    print("17. Vaciar jarra de 3 litros en jarra de 8 litros")
    print("18. Vaciar jarra de 3 litros en jarra de 5 litros")
    print("19. Empezar de nuevo")
    print("------------------------------------------")
    
    
# =================== Principal ======================

estado_inicial = (0,0,0)
estado_actual = estado_inicial
pasos = 0
while True:          
    print_menu()
    opcion = int(input("Seleccione un operador [1-19]: "))
     
    if opcion == 1:     
        estado_actual = LlenarJarra8Bomba(estado_actual)
        
    elif opcion == 2:
        estado_actual = LlenarJarra5Bomba(estado_actual)

    elif opcion == 3:
        estado_actual = LlenarJarra3Bomba(estado_actual)

    elif opcion == 4:
        estado_actual = VaciarJarra8Suelo(estado_actual)

    elif opcion == 5:
        estado_actual = VaciarJarra5Suelo(estado_actual)

    elif opcion == 6:
        estado_actual = VaciarJarra3Suelo(estado_actual)

    elif opcion == 7:
        estado_actual = LlenarJarra8ConJarra5(estado_actual)

    elif opcion == 8:
        estado_actual = LlenarJarra8ConJarra3(estado_actual)

    elif opcion == 9:
        estado_actual = LlenarJarra5ConJarra8(estado_actual)

    elif opcion == 10:
        estado_actual = LlenarJarra5ConJarra3(estado_actual)

    elif opcion == 11:
        estado_actual = LlenarJarra3ConJarra8(estado_actual)

    elif opcion == 12:
        estado_actual = LlenarJarra3ConJarra5(estado_actual)

    elif opcion == 13:
        estado_actual = VaciarJarra8EnJarra5(estado_actual)

    elif opcion == 14:
        estado_actual = VaciarJarra8EnJarra3(estado_actual)

    elif opcion == 15:
        estado_actual = VaciarJarra5EnJarra8(estado_actual)

    elif opcion == 16:
        estado_actual = VaciarJarra5EnJarra3(estado_actual)

    elif opcion == 17:
        estado_actual = VaciarJarra3EnJarra8(estado_actual)

    elif opcion == 18:
        estado_actual = VaciarJarra3EnJarra5(estado_actual)

    elif opcion == 19:
        print("Reiniciando juego...")
        estado_actual = estado_inicial
        pasos = 0
    else:
        input("Por favor seleccione una opciones del 1-19: ")
    
    print(estado_actual)
    (x,y,z) = estado_actual
    if y == 4 or z == 4:
        print("Lo lograste en {} pasos".format(pasos))
        break