import time
import board
import adafruit_bh1750

i2c=board.I2C()
bh1750=adafruit_bh1750.BH1750(i2c, address=0x23)

while True:
    print("%.2f lux"%bh1750.lux)
    print(type(bh1750.lux))
    time.sleep(3)