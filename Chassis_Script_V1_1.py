############################################################################
# Chassis Script - Nov. 05, 2021
# Written by: Sirpreet K. Dhillon
#             Hazelle Lebumfacil

# Updates: Using Master Doc
############################################################################

import RPi.GPIO as GPIO # import GPIO libraby
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # Set pi to use pins

from WiE_Design_Master_Script import PIN_DIR_LEFT,PIN_DIR_RIGHT,PIN_SPEED_LEFT,PIN_SPEED_RIGHT 



GPIO.setup(PIN_SPEED_LEFT, GPIO.OUT) 
GPIO.setup(PIN_DIR_LEFT, GPIO.OUT)
GPIO.setup(PIN_SPEED_RIGHT, GPIO.OUT) 
GPIO.setup(PIN_DIR_RIGHT, GPIO.OUT)



# Function to move the robot forward 
def robot_fwd(PWMFREQ):
	print(" forward function has been entered")
	pwm_left = GPIO.PWM(PIN_SPEED_LEFT,PWMFREQ)
	print(" PWMFREQ value is: ", PWMFREQ)
	print(" pwm_left PIN is: ", PIN_SPEED_LEFT)
	pwm_right = GPIO.PWM(PIN_SPEED_RIGHT,PWMFREQ)
	GPIO.output(PIN_DIR_LEFT, GPIO.LOW)
	GPIO.output(PIN_DIR_RIGHT, GPIO.HIGH)
	
	
# Function to move the robot backwards 
def robot_rev(PWMFREQ):
	pwm_left = GPIO.PWM(PIN_SPEED_LEFT,PWMFREQ)
	pwm_right = GPIO.PWM(PIN_SPEED_RIGHT,PWMFREQ)
	GPIO.output(PIN_DIR_LEFT, GPIO.HIGH)
	GPIO.output(PIN_DIR_RIGHT, GPIO.LOW)


# Function to turn right
def robot_turn_right(PWMFREQ_LEFT, PWMFREQ_RIGHT):
	pwm_left = GPIO.PWM(PIN_SPEED_LEFT,PWMFREQ_LEFT)
	pwm_right = GPIO.PWM(PIN_SPEED_RIGHT,PWMFREQ_RIGHT)
	GPIO.output(PIN_DIR_LEFT, GPIO.LOW)
	GPIO.output(PIN_DIR_RIGHT, GPIO.HIGH)

# Function to turn left
def robot_turn_left(PWMFREQ_LEFT, PWMFREQ_RIGHT):
	pwm_left = GPIO.PWM(PIN_SPEED_LEFT,PWMFREQ_LEFT)
	pwm_right = GPIO.PWM(PIN_SPEED_RIGHT,PWMFREQ_RIGHT)
	GPIO.output(PIN_DIR_LEFT, GPIO.LOW)
	GPIO.output(PIN_DIR_RIGHT, GPIO.HIGH)
	
# Function to stop the robot
def robot_stop():
	pwm_left = GPIO.PWM(PIN_SPEED_LEFT, 1)
	pwm_right = GPIO.PWM(PIN_SPEED_RIGHT, 1)
	pwm_left.stop()
	pwm_right.stop()
	
# Function to increase speed (where inc is a positive value to increment by)
def robot_inc_speed(min_dc, max_dc, inc):
	pwm_left = GPIO.PWM(PIN_SPEED_LEFT, 1)
	pwm_right = GPIO.PWM(PIN_SPEED_RIGHT, 1)
	for duty in range (min_dc, max_dc, inc):
		pwm_left.ChangeDutyCycle(duty)
		pwm_right.ChangeDutyCycle(duty)
		time.sleep(0.1)
		
# Function to decrease speed (where dec is a positive value to decrement by)
def robot_dec_speed(min_dc, max_dc, dec):
	pwm_left = GPIO.PWM(PIN_SPEED_LEFT, 1)
	pwm_right = GPIO.PWM(PIN_SPEED_RIGHT, 1)
	for duty in range (max_dc, min_dc, dec):
		pwm_left.ChangeDutyCycle(duty)
		pwm_right.ChangeDutyCycle(duty)
		time.sleep(0.1)

    
    
    
