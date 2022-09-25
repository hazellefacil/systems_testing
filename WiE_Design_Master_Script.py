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




# Import GPIO Library
import RPi.GPIO as GPIO
import time

# Import Robot Test Files
import Chassis_Script_V1_1 as chassis

# setup for pins -- SIRI COMMENT --> change it to appropriate later 
# pwm_left = GPIO.PWM(PIN_SPEED_LEFT,10) 
# pwm_right = GPIO.PWM(PIN_SPEED_RIGHT,10)

# Disable warnings
GPIO.setwarnings(False)
print("warnings off done")

# Set pi to use pins
GPIO.setmode(GPIO.BOARD)
print("board mode is set")



############################################################################
# Example For Chassis Testing

# Change PWMFREQ should be changed for moving fwd and bckwd
PWMFREQ = 50

# Change PWMFREQ_LEFT and PWMFREQ_RIGHT for turning 
# The smaller value should be the direction to turn towards
PWMFREQ_RIGHT = 50
PWMFREQ_LEFT = 50

# For gradually increasing and decreasing speed
MIN_DUTY_CYCLE = 10
MAX_DUTY_CYCLE = 90

INCREMENT_BY = 8
DECREMENT_BY = 5

print("starting forward")
chassis.robot_fwd(PWMFREQ)
print(" forward done ")
print(" stopping... ")
chassis.robot_stop()
print(" stopped ")

chassis.robot_rev(PWMFREQ)
chassis.robot_stop()

chassis.robot_turn_right(PWMFREQ_LEFT, PWMFREQ_RIGHT)
chassis.robot_stop()

chassis.robot_inc_speed(MIN_DUTY_CYCLE,MAX_DUTY_CYCLE,INCREMENT_BY)
chassis.robot_stop()

chassis.robot_dec_speed(MIN_DUTY_CYCLE,MAX_DUTY_CYCLE,DECREMENT_BY)
chassis.robot_stop()








