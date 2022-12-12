"""
Estacion de clima para plantas programa by:

██████████████████████████████████████████████████████████████████████████████████
█─▄▄▄─██▀▄─██▄─▄████▀▄─██▄─█─▄███▄─▄▄▀█▄─▄▄─████▀▄─██─▄▄▄▄█─▄─▄─█─▄▄─█▄─▄▄▀██▀▄─██
█─███▀██─▀─███─██▀██─▀─███─▄▀█████─██─██─▄█▀████─▀─██▄▄▄▄─███─███─██─██─▄─▄██─▀─██
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀

*** TODOS LOS DERECHOS RESERVADOS POR LA LICENCIA GNU ***

Repositorio en Github: https://github.com/ElCalak/Estacion-del-clima-Pluie-magique

"""

from machine import Pin, ADC #De la clase machine trae los modulos Pin (Para la declaracion de pines fisicos) y ADC (Para la creacion y manipulacion de objetos de tipo ADC)
from time import sleep #De la clase time importa el modulo sleep para detener el programa
from machine import I2C #De la clase machine trae el modulo I2C para la creacion de objetos I2C
from lcd_api import LcdApi #De la clase personalizada lcd_api trae el modulo LcdApi para el soporte de LCD
from pico_i2c_lcd import I2cLcd #De la clase personalizada pico_i2c_lcd trae el modulo I2cLcd para la creacion y manipulacion de objetos I2cLcd

aqua = ADC(28) #Crea un objeto de tipo ADC en el pin 28 referente al sensor de humedad
tem = ADC(27) #Crea un objeto de tipo ADC en el pin 27 referente al sensor LM35

#Declaracion de variables globales
dire = 0x27 #Almacena la direccion del LCD
Fil = 2 #Numero de filas del LCD
col = 16 #Numero de columnas del LCD

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000) #Crea un objeto de tipo I2C que se comunica con los pines 0 y 1 y tiene una frecuendia de 40k
lcd = I2cLcd(i2c, dire, Fil, col) #Crea un objeto de tipo I2cLcd con relacion al objeto i2c y las variables declaradas
lcd.putstr("Bienvenido!...") #Mensaje para comprobar el funcionamiento del LCD
sleep(5) #Detiene el programa 5 segundos
lcd.clear() #Limpia el LCD

while True: #Inica ciclo sin fin

    LecAq = aqua.read_u16() #Crea una variable para almacenar el valor de la lectura del sensor de humedad
    LecTem = tem.read_u16() #Crea una variable para almacenar el valor de la lectura del LM35

    porAq = ((LecAq * 100)/65535) #Crea una relacion porcentual con respecto al valor leido del sensor de humedad
    flport = "{:.1f}".format(porAq) #Crea una varibale que almacena el cambio del formato del porcentaje
    temp = ((LecTem * 150)/65535) - 60 #Crea una variable que almacena la relacion entre la lectura y la temperatura maxima que puede leer el LM35
    flform = "{:.1f}".format(temp) #Crea una variable que almacena el cambio de formato de la temperatura

    lcd.move_to(0,0) #Mueve el cursor del lcd a la posicion 0, 0
    lcd.putstr(str("Temperatura: ") + flform + str("º")) #Imprime el valor de la temperatura en el LCD
    lcd.move_to(0, 1) #Mueve el cursor del LCD a la posicion 0, 1
    lcd.putstr(str("Humedad: ") + flport + str("%")) #Imprime el valor de la Humedad en el LCD

    sleep(120) #Espera 5 minutos

    lcd.clear() #Limpia el LCD

    #Y el ciclo continua y continua...

#Fin del programa
