import RPi.GPIO as GPIO
import time
#### Please make the connections as below,
in1 = 14
in2 = 15
enable = 18
in3 = 23
in4 = 24

GPIO.setmode(GPIO.BCM)
global speed

def init():
    global speed
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
    global speed
    speed.ChangeDutyCycle(spd)
    GPIO.output(in1,False)
    GPIO.output(in2,True)
    GPIO.output(in3,True)
    GPIO.output(in4,False)

def left(spd):
    global speed
    speed.ChangeDutyCycle(spd)
    GPIO.output(in1,True)
    GPIO.output(in2,False)
    GPIO.output(in3,False)
    GPIO.output(in4,True)
    
def forward(spd):
    global speed
    speed.ChangeDutyCycle(spd)
    GPIO.output(in1,True)
    GPIO.output(in2,False)
    GPIO.output(in3,True)
    GPIO.output(in4,False)

def reverse(spd):
    global speed
    speed.ChangeDutyCycle(spd)
    GPIO.output(in1,False)
    GPIO.output(in2,True)
    GPIO.output(in3,False)
    GPIO.output(in4,True)

def stop():
    global speed
    speed.ChangeDutyCycle(0)
    GPIO.output(in1,False)
    GPIO.output(in2,False)
    GPIO.output(in3,False)
    GPIO.output(in4,False)
