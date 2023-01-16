
def cajeroautomatico():
    print("")
    print(":::::::::::")
    print("Banco SORU")
    print(":::::::::::")
    print("")
    saldo=1000
    contador=1
    while contador<=3:
        contraseña=input("Ingrese la contraseña: ")
        if contraseña=="123":
            contador=4
            respuesta=0
            while respuesta!=5:
                print("1. Consultar saldo")
                print("2. Depositar saldo")
                print("3. Retirar saldo")
                print("4. Transferir saldo")
                print("5. Salir")            
                try:
                    respuesta=int(input("Respuesta: "))
                    if respuesta==1:
                        print("Tu saldo es: S./",saldo)
                    elif respuesta==2:
                        deposito=float(input("Ingresa la cantidad a depositar: "))
                        print("Saldo inicial: S./",saldo)
                        print("Monto depositado: S./",deposito)
                        saldo=saldo+deposito
                        print("Saldo final: S./", saldo)
                    elif respuesta==3:             
                        retiro=float(input("Ingrese la cantidad a retirar: "))
                        if retiro>saldo:
                            print("***La cantidad supera el saldo***")
                            print("Tu saldo actual es S/.",saldo)
                        else:
                            saldo=saldo-retiro
                            print("Tu saldo actual es S/.",saldo)
                    elif respuesta==4:
                        numerocuenta=input("Ingrese el numero de cuenta a transferir: ")
                        montotransferir=float(input("Ingrese monto a transferir: "))
                        if montotransferir>saldo:
                            print("***La cantidad supera el saldo***")
                            print("Tu saldo actual es S/.",saldo)
                        else:
                            print("Saldo inicial: S/.",saldo)
                            print("Numero de cuenta a transferir: ",numerocuenta)
                            print("Monto transferido S/.",montotransferir)
                            print("Saldo final S/.",saldo-montotransferir)
                            saldo=saldo-montotransferir
                    elif respuesta==5:
                        print("Gracias por confiar en nosotros")
                    elif respuesta!=4:
                        print("***Opcion invalida, ingrese bien las opciones***")
                except:
                    print("***Opcion invalida, ingrese bien las opciones***")
                
        else:        
            if contador==3:
                print("***Has fallado los 3 intentos***")
            else:
                print("***La contraseña es incorrecta***")            
            print("Te quedan ",3-(contador)," intentos.")
            contador=contador+1
      
#Algoritmo
print("Autor: Chancafe Miramira Frank Jhonatan")
print("Telefono: 976 407 080")
print("Correo: frank_mch97@hotmail.com")
print("Estado: Estudiante de Desarrollo de Sistemas")
print("Instituto: IDAT")
print("Ciclo: V")
print("Año: 2022")

cajeroautomatico()


