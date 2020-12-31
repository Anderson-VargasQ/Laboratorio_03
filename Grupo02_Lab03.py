# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Cuenta_bancaria:
    
    def __init__(self,numero_unico,clave):
        self.numero_unico= numero_unico
        self.clave= clave
        
class Targeta_bancaria(Cuenta_bancaria):
    
    def __init__(self,numero_unico,clave,numero_cuenta,condicion):
        super().__init__(numero_unico,clave)
        self.numero_cuenta=numero_cuenta
        self.condicion= condicion

class Persona(Targeta_bancaria):

    def __init__(self,numero_unico,clave,numero_cuenta,condicion,nombre,dni,edad,consignacion=0):
        super().__init__(numero_unico,clave,numero_cuenta,condicion)
        self.nombre=nombre
        self.dni= dni
        self.edad= edad
        self.consignacion=consignacion
        
    def monto(self):
        
        b=int(input("Ingrese su clave: "))
        if self.clave==b:
            print(self.consignacion)
                
    def retorno_variable(self):
        return self.clave,self.numero_cuenta,self.condicion,self.nombre,self.dni,self.edad

class Cajero_automatico(Persona):
    
    def __init__(self,numero_unico,clave,numero_cuenta,condicion,nombre,dni,edad):
        super().__init__(numero_unico,clave,numero_cuenta,condicion,nombre,dni,edad)

        
    def autentificarUsuario(self):
        
        nombree= input("Ingrese su nombre: ")
        dnii= int(input("Ingrese su N° DNI: "))
        edadd= int(input("Ingrese su edad: "))
        cuentaa= int(input("Ingrese N° de cuenta: "))
        clavee = int(input("Ingrese su Contraseña: "))

        
        if self.nombre==nombree and self.dni==dnii and self.edad==edadd and self.numero_cuenta==cuentaa and self.clave==clavee:
            print("Autentificación del usuario de forma exitosa.")
            return True
        else:
            print("No se logró identificar al usuario.")
            return False

    def retiros(self,n):
        
        a=self.autentificarUsuario()
        print(a)
        if a==True:
            
            x= int(input("Ingrese DNI: "))
            if self.dni== x:
                y= int(input("Ingrese Contraseña: "))
                if self.clave== y:
                    ab=int(input("Ingrese el monto a retirar: "))
                    n.consignacion -= ab
                    print("Retiro Exitoso")
            else: 
                print("Error en el proceso")
        else:
            print("Fallo de autentificación")

    def depositos(self,n,m):
        
        a=self.autentificarUsuario()
        if a==True:

            x= int(input("Ingrese DNI: "))
            if self.dni== x:
                y= int(input("Ingrese Contraseña: "))
                if self.clave== y:
                    ab=int(input("Ingrese el monto a depositar: "))
                    abc=int(input("Ingrese el número de cuenta: "))
                    for i in n:
                        if i.numero_cuenta==abc:
                            i.consignacion+=ab
                    print("Depósito Exitoso")
            else: 
                print("Error en el proceso")
    
    def cambiarClave(self,m):
        a=self.autentificarUsuario()
        if a == True:
            x= int(input("Ingrese DNI: "))
            if self.dni== x:
                y= int(input("Ingrese Contraseña: "))
                if self.clave== y:
                    n= int(input("Ingrese nueva contraseña: "))
                    m.clave = n
            else: 
                print("Error en el proceso")

def main():
    listaclientes=[]
    def registrocliente():
    
        print("Registro de Nuevo Cliente")
        nombre=str(input("\nDigite el nombre del cliente:\n"))
        dni=int(input("\nDigite su DNI. Son 8 dígitos.\n"))
        edad=int(input("\nDigite su edad.\n"))
        clave=int(input("\nDigite su clave. Son 4 dígitos.\n"))
        condicion=True
        numero_cuenta=int(input("\nDigite su número de cuenta. Son 5 dígitos.\n"))
        numero_unico= int(input("\nDigite su número único. Son 4 dígitos.\n"))  
      
        
        if edad<18:
            print("Usted es menor de edad, no puede registrarse.")
            print("\nPuede registrase nuevamente si usted lo desea.\n")
        if edad>60:
            print("El registro no se puede efectuar. El límite de edad es 60 años.")
            print("\nPuede registrase nuevamente si usted lo desea.\n")
        if 18<=edad<=60:
            print("\nRegistro exitoso\n")
            v=Persona(numero_unico,clave,numero_cuenta,condicion,nombre,dni,edad)
            listaclientes.append(v)
        return listaclientes
    
    def buscar_cliente_registrado():
    
        print("Buscar si el cliente está registrado en nuestro banco.")
        numero_unico=int(input("\nDigite el numero único del cliente.\n"))
        contador=0
        for v in listaclientes:
            if numero_unico==v.numero_unico:
                a,b,c,d,e,f = v.retorno_variable()
                posicion=contador
                break
            else:
                contador+=1
        return a,b,c,d,e,f,numero_unico,posicion
    
    listaclientes=[]
    while True:
        print("BIENVENIDO AL BANCO 'HAIL MEC.UNT'")
        opciones=int(input("\n¿QUÉ OPERACIÓN DESEA RELIZAR?\nOPRIME 1.- PARA REGISTRAR NUEVO CLIENTE\nOPRIMA 2.- HACER UN RETIRO\nOPRIMA 3.- HACER TRANSACCIONES\nOPRIMA 4.- CAMBIAR LA CLAVE\nOPRIMA 5.-CONSULTA SALDO\n"))
        if opciones==1:
            listaclientes=registrocliente()
        if opciones==2:
            a,b,c,d,e,f,g,h=buscar_cliente_registrado()
            z=Cajero_automatico(g,a,b,c,d,e,f)
            z.retiros(listaclientes[h])
        if opciones==3:
            a,b,c,d,e,f,g,h=buscar_cliente_registrado()
            z=Cajero_automatico(g,a,b,c,d,e,f)
            z.depositos(listaclientes,h)
        if opciones==4:
            a,b,c,d,e,f,g,h=buscar_cliente_registrado()
            z=Cajero_automatico(g,a,b,c,d,e,f)
            z.cambiarClave(listaclientes[h])
        if opciones==5:
            a,b,c,d,e,f,g,h=buscar_cliente_registrado()
            listaclientes[h].monto()
            
            
if __name__=="__main__":
    main()