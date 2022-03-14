opcion=0
print("        Menú         ")
print("_____________________")
print("1--> Recibir Votos. ")
print("2--> Mostrar Votos. ")
print("3--> SALIR")
print("_____________________")

while(True):
    opcion=int(input("Ingresa una opción: "))
    if(opcion==1): 
        print("__________________________________") 
        print("         Menú Votaciones ")
        print("__________________________________")
        print("1--> Voto para Senado. ")
        print("2--> Voto para Camara. ")
        print("3--> Voto para Consulta. ")
        print("0--> SALIR ")
        print("__________________________________")  
        opcion=int(input("Digita una opción de voto: "))
        

        if(opcion==1):
            contadorSenado=1
            
            contadorSenado+=contadorSenado

        elif(opcion==2):
            contadorCamara=1
            
            contadorCamara+=contadorCamara
        elif(opcion==3):
            print("         Menú Votaciones ")
            print("__________________________________")
            print("1--> Voto para Pacto Historico. ")
            print("2--> Voto para Centro Esperanza. ")
            print("3--> Voto para Equipo. ")
            print("0--> SALIR ")
            print("__________________________________")
            
            opcionConsulta=100
            while(opcionConsulta!=0):

                opcionConsulta=int(input("Digite la opción de consulta que desea votar: "))

                pacto=0
                centro=0
                equipo=0

                if opcionConsulta==1:
                    pacto +=1
                elif opcionConsulta==2:
                    centro+=1
                elif opcionConsulta==3:
                    equipo+=1
                elif opcionConsulta==0:
                    break   
                else:
                    print("Digite una opción valida para consulta")

    elif(opcion==2):
        print(f'Votos para Cenado: {contadorSenado}')
        print(f'Votos para Camara: {contadorCamara}')
        print(f'Votos para Pacto Historico: {pacto}')
        print(f'Votos para Centro Esperanza: {centro}')
        print(f'Votos para Equipo: {equipo}')
    elif(opcion==3):
        break
    else:
        print("Digite una opción valida para el primer menu.")    

        


        
        



