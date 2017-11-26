import RPi.GPIO as GPIO                           #Import GPIO library
import time                                       #Import time library
import communication

GPIO.setmode(GPIO.BCM)                          #Set GPIO pin numbering
pir = 21                                          #Associate pin 26 to pir
GPIO.setup(pir, GPIO.IN)                          #Set pin as GPIO in
time.sleep(2)                                     #Waiting 2 seconds for the sensor to initiate

def startDetectMotion():
    print "Detecting motion"
    while True:
       if GPIO.input(pir):                            #Check whether pir is HIGH
          print "Motion Detected!"
          communication.sendToThingsPeak()
          time.sleep(2)                               #D1- Delay to avoid multiple detection
       time.sleep(0.1)                                #While loop delay should be less than detection(hardware) delay