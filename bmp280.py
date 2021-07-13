
"""
este archivo es el mas basico para el BMP280, para especificar la direccion del sensor, en el argumento del metodo
dafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=@@@@)
donde los @@@@ es donde va la direccion
la salida de los datos es tipo flotante.

"""
import time
import board
import adafruit_bmp280

i2c=board.I2C()
bmp280=adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
bmp280.sea_level_pressure=1023.5
#change this to match the location's pressure (hPa) at sea level
while True:
    print(bmp280.temperature)
    print(bmp280.pressure)
    print(bmp280.altitude)
    #print(type(bmp280.temperature))
    time.sleep(2)
    
    