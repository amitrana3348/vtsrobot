import RPi.GPIO as GPIO
import time  
in1 = 14
in2 = 15
enable = 18
in3 = 23
in4 = 24

GPIO.setmode(GPIO.BCM)

def init():
    GPIO.setup(enable,GPIO.OUT)
    GPIO.setwarnings(False)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)

    GPIO.output(in1,False)
    GPIO.output(in2,False)
    GPIO.output(in3,False)
    GPIO.output(in4,False)

    speed = GPIO.PWM(enable,100)
    speed.start(05)

    
#speed.ChangeDutyCycle(x)  
def right(spd):
    speed.ChangeDutyCycle(spd)
    GPIO.output(in1,False)
    GPIO.output(in2,True)
    GPIO.output(in3,True)
    GPIO.output(in4,False)

def left(spd):
    speed.ChangeDutyCycle(spd)
    GPIO.output(in1,True)
    GPIO.output(in2,False)
    GPIO.output(in3,False)
    GPIO.output(in4,True)
    
def forward(spd):
    speed.ChangeDutyCycle(spd)
    GPIO.output(in1,True)
    GPIO.output(in2,False)
    GPIO.output(in3,True)
    GPIO.output(in4,False)

def reverse(spd):
    speed.ChangeDutyCycle(spd)
    GPIO.output(in1,False)
    GPIO.output(in2,True)
    GPIO.output(in3,False)
    GPIO.output(in4,True)

def stop():
    speed.ChangeDutyCycle(0)
    GPIO.output(in1,False)
    GPIO.output(in2,False)
    GPIO.output(in3,False)
    GPIO.output(in4,False)

try:
    while True:
        right(100)
        time.sleep(2)
        stop()
        time.sleep(1)
    
        reverse(25)
        time.sleep(2)
        stop()
        time.sleep(1)
except KeyboardInterrupt:
    stop()
    print'\n Exiting Code'
