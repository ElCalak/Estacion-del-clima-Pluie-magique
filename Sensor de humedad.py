"""
Sensor de humedad en valores I2C y LCD programado:

██████████████████████████████████████████████████████████████████████████████████
█─▄▄▄─██▀▄─██▄─▄████▀▄─██▄─█─▄███▄─▄▄▀█▄─▄▄─████▀▄─██─▄▄▄▄█─▄─▄─█─▄▄─█▄─▄▄▀██▀▄─██
█─███▀██─▀─███─██▀██─▀─███─▄▀█████─██─██─▄█▀████─▀─██▄▄▄▄─███─███─██─██─▄─▄██─▀─██
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀

*** TODOS LOS DERECHOS RESERVADOS POR LA LICENCIA GNU ***
-------

Repositorio en Github: https://github.com/ElCalak/Sensor-de-humedad-para-Pluie-magique-/tree/main

"""

from machine import Pin, ADC #De la clase machine trae los modulos Pin (Para la declaracion de pines fisicos) y ADC (Para la creacion y manipulacion de objetos de tipo ADC)
from time import sleep #De la clase time importa el modulo sleep para detener el programa
from machine import I2C #De la clase machine trae el modulo I2C para la creacion de objetos I2C
from lcd_api import LcdApi #De la clase personalizada lcd_api trae el modulo LcdApi para el soporte de LCD
from pico_i2c_lcd import I2cLcd #De la clase personalizada pico_i2c_lcd trae el modulo I2cLcd para la creacion y manipulacion de objetos I2cLcd

sens = ADC(28) #Crea un objeto de tipo ADC en el pin 28 (El pin GIPO28 de la raspberry pi pico es ADC)

#Declaracion de variables globales
dire = 0x27 #Almacena la direccion del LCD
Fil = 2 #Numero de filas del LCD
col = 16 #Numero de columnas del LCD

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000) #Crea un objeto de tipo I2C que se comunica con los pines 0 y 1 y tiene una frecuendia de 40k
lcd = I2cLcd(i2c, dire, Fil, col) #Crea un objeto de tipo I2cLcd con relacion al objeto i2c y las variables declaradas
lcd.putstr("Bienvenido!...") #Mensaje para comprobar el funcionamiento del LCD
sleep(5) #Detiene el programa 5 segundos
lcd.clear() #Limpia el LCD

while True: #Inicia ciclo sin fin

    lec = sens.read_u16() #Crea una variable que almacena la lectura analogica del objeto analogo global sens

    por = ((lec * 100)/65535) #Crea una relacion porcentual con respecto al valor leido

    flport = "{:.1f}".format(por) #Crea una varibale que almacena el cambio del formato del porcentaje

    print(flport + str("%")) #Imprime el porcentaje en la consola
    lcd.putstr(flport + str("%")) #Imprime el porcentaje en el LCD

    sleep(1) #Detiene el programa 1 segundo

    lcd.clear() #Limpia el LCD
