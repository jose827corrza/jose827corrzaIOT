import time
import board
import adafruit_ahtx0

i2c=board.I2C()
aht10=adafruit_ahtx0.AHTx0(i2c, address=0x38)

while True:
    print(aht10.temperature)
    print(aht10.relative_humidity)
    print(type(aht10.temperature))
    time.sleep(3)