
import RPi.GPIO as GPIO
from time import sleep
import threading
import rospy
from std_msgs.msg import String  # You might want to use a more appropriate message type

# GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Define pins for the first motor
DIR1 = 10
STEP1 = 8

# Define pins for the second motor
DIR2 = 12
STEP2 = 16

CW = 1
CCW = 0

# Setup the GPIO pins
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(STEP1, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)

# Function to move a motor
def motor_move(DIR, STEP, direction, steps, delay):
    GPIO.output(DIR, direction)
    for x in range(steps):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

# Function to control each motor using a thread
def control_motor(DIR, STEP, CW, CCW):
    while not rospy.is_shutdown():
        motor_move(DIR, STEP, CW, 1600, 0.0005)
        sleep(.75)
        motor_move(DIR, STEP, CCW, 400, 0.005)
        sleep(.75)

# ROS Node initialization
def motor_control_node():
    rospy.init_node('motor_control_node', anonymous=True)
   
    # Thread setup
    try:
        thread1 = threading.Thread(target=control_motor, args=(DIR1, STEP1, CW, CCW))
        thread2 = threading.Thread(target=control_motor, args=(DIR2, STEP2, CW, CCW))

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()
    except KeyboardInterrupt:
        rospy.loginfo("Motor control node shutdown")
        GPIO.cleanup()

if __name__ == '__main__':
    motor_control_node()
