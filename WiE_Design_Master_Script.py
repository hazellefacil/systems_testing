############################################################################
# Chassis Script - Nov. 05, 2021
# Written by: Sirpreet K. Dhillon
#             Hazelle Lebumfacil

# Updates: Chassis functions imported and used
############################################################################

# Pin Assignment 
PIN_DIR_LEFT = 36
PIN_DIR_RIGHT = 16
PIN_SPEED_LEFT = 32
PIN_SPEED_RIGHT = 12

pwm_left = GPIO.PWM(PIN_SPEED_LEFT,0) 
pwm_right = GPIO.PWM(PIN_SPEED_RIGHT,0)


# Import GPIO Library
import RPi.GPIO as GPIO
import time

# Import Robot Test Files
import Chassis_Script as chassis

# Disable warnings
GPIO.setwarnings(False)

# Set pi to use pins
GPIO.setmode(GPIO.BOARD)



############################################################################
# Example For Chassis Testing

# Change PWMFREQ should be changed for moving fwd and bckwd
PWMFREQ = 0

# Change PWMFREQ_LEFT and PWMFREQ_RIGHT for turning 
# The smaller value should be the direction to turn towards
PWMFREQ_RIGHT = 0
PWMFREQ_LEFT = 0

# For gradually increasing and decreasing speed
MIN_DUTY_CYCLE = 10
MAX_DUTY_CYCLE = 90

INCREMENT_BY = 8
DECREMENT_BY = 5


chassis.robot_fwd(PWMFREQ)
robot_stop()

chassis.robot_rev(PWMFREQ)
robot_stop()

chassis.robot_turn_right(PWMFREQ_LEFT, PWMFREQ_RIGHT)
robot_stop()

chassis.robot_inc_speed(MIN_DUTY_CYCLE,MAX_DUTY_CYCLE,INCREMENT_BY)
robot_stop()

chassis.robot_dec_speed(MIN_DUTY_CYCLE,MAX_DUTY_CYCLE,DECREMENT_BY)
robot_stop()








