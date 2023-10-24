from machine import Pin
import utime as time
import utime
from dht import DHT11, InvalidChecksum

adc = machine.ADC(26)
conversion_factor = 100 / (65535)

while True:    
    time.sleep(1)
    pin = Pin(15, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t  = (sensor.temperature)
    h = (sensor.humidity)
    print("READINGS FROM DHT-11 SENSOR :") 
    print("Temperature: {}".format(sensor.temperature))
    print("Humidity: {}".format(sensor.humidity))
    
    rainCoverage = 100 - (adc.read_u16() * conversion_factor)
    print("READING FROM THE RAIN SENSOR : ")
    
    print(round(rainCoverage, 1), "%")
    utime.sleep_ms(1000)



