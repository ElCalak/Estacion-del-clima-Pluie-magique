"""
Sensor de temperatura LM35 en I2C y LCD programado:

██████████████████████████████████████████████████████████████████████████████████
█─▄▄▄─██▀▄─██▄─▄████▀▄─██▄─█─▄███▄─▄▄▀█▄─▄▄─████▀▄─██─▄▄▄▄█─▄─▄─█─▄▄─█▄─▄▄▀██▀▄─██
█─███▀██─▀─███─██▀██─▀─███─▄▀█████─██─██─▄█▀████─▀─██▄▄▄▄─███─███─██─██─▄─▄██─▀─██
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀

*** TODOS LOS DERECHOS RESERVADOS POR LA LICENCIA GNU ***

Debug:

    Christopher Gonzalez Linares
    Ivan Garcia Cermeno

Repositorio en Github: https://github.com/ElCalak/Sensor-de-temperatura-LM35-para-Pluie-magique

"""

from machine import Pin, ADC #De la clase machine trae los modulos Pin (Para la declaracion de pines fisicos) y ADC (Para la creacion y manipulacion de objetos de tipo ADC)
from time import sleep #De la clase time importa el modulo sleep para detener el programa
from machine import I2C #De la clase machine trae el modulo I2C para la creacion de objetos I2C
from lcd_api import LcdApi #De la clase personalizada lcd_api trae el modulo LcdApi para el soporte de LCD
from pico_i2c_lcd import I2cLcd #De la clase personalizada pico_i2c_lcd trae el modulo I2cLcd para la creacion y manipulacion de objetos I2cLcd

sens = ADC(28)#Crea un objeto de tipo ADC en el pin 28 (El pin GIPO28 de la raspberry pi pico es ADC)

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

    temp = ((lec * 150)/65535) - 60 #Crea una variable que almacena la relacion entre la lectura y la temperatura maxima que puede leer el LM35

    flform = "{:.1f}".format(temp) #Crea una variable que almacena el cambio de formato de la temperatura

    print(flform) #Imprime la temperatura
    lcd.putstr(flform) #Imprime la temperatura en el LCD

    sleep(1) #Detiene el programa 1 segundo

    lcd.clear() #Limpia el LCD
