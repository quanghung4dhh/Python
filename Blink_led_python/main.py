from machine import Pin
import time

led = Pin(2, Pin.OUT) #Khai báo chân LED

while True:
    led.value(not led.value()) #Blink led
    print(123)                 #In ra màn hình khi LED nháy
    time.sleep(0.2)            #Đặt khoảng thời gian giữa 2 lần nháy 0.2s
