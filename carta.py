#Menú de opciones

opcion=100

# Ciclo / Bucle / Loop / Iteración

print("         Menú a la carta ")
print("__________________________________")
print("1--> Calculcar la suma. ")
print("2--> Calculcar la resta. ")
print("3--> Calculcar la multiplicación. ")
print("4--> Calculcar la división. ")
print("0--> SALIR ")
print("__________________________________")

while(opcion!=0):
    opcion=int(input("Digia una opción: "))

    if(opcion==1):
        numero1=int(input("Digita un número: "))
        numero2=int(input("Digita otro número: "))
        print(f'{numero1}+{numero2}={(numero1+numero2)}')

    elif(opcion==2):
        numero1=int(input("Digita un número: "))
        numero2=int(input("Digita otro número: "))
        print(f'{numero1}-{numero2}={(numero1-numero2)}') 
    
    elif(opcion==3):
        numero1=int(input("Digita un número: "))
        numero2=int(input("Digita otro número: "))
        print(f'{numero1}*{numero2}={(numero1*numero2)}') 

    elif(opcion==4):
        numero1=int(input("Digita un número: "))
        numero2=int(input("Digita otro número: "))
        print(f'{numero1}/{numero2}={(numero1/numero2)}')     

    else:
        print("Digita una opción valida")