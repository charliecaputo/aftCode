import RPi.GPIO as GPIO
import time

ENC_A = 13 ##emits light pin 13
ENC_B = 11 ## recieves light pin 11

GPIO.setmode(GPIO.BOARD)

GPIO.setup(ENC_A, GPIO.IN)
GPIO.setup(ENC_B, GPIO.IN)

GPIO.add_event_detect(ENC_A, GPIO.RISING)

##itialize test variable


##make a sensor reading function that returns 0 if not blocked and 1 if blocked
def counter(ENC_A):
	"""
	make a sensor reading function that 
	returns 0 if not blocked and 1 if blocked
	"""
    #make count glibal
    global count
    if GPIO.input(ENC_B):
        count = 0
    else:
    	count = 1
    print(count)

if __name__ == "__main__":
    try:
        while True:
            counter(ENC_A)
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

