
##apellido = input("Ingrese su primer apellido: ")

## torceado=apellido[-4:]

## if  torceado == "ez":
##   print("Eres casi español.")
## if torceado == "es":
##   print("eres casi peruano") 


## hcaer un programa que le pida a un usuario su dni compruebe que sea
## de 8 digitos , si es correcto que sume el primer numero y el ultimo numero del dni
## mostrar por pantalla la suma y el resultado 

## ingresa = 12345678
## "1+8=9"

dni_usuario = int(input("ingrese su numero de dni : "))

dni_long = len(dni_usuario)
if dni_long <= 8 :
   