# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       aria                                                         #
# 	Created:      7/11/2023, 9:55:29 AM                                        #
# 	Description:  IQ2 project                                                  #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import random
randy = random.randint(5, 10)
# Brain should be defined by default
brain = Brain()
leftMotor = Motor(Ports.PORT1)
rightMotor = Motor(Ports.PORT6)

leftMotor.set_velocity(100, PERCENT)
rightMotor.set_velocity(30, PERCENT)

leftMotor.spin(DirectionType.FORWARD)
rightMotor.spin(DirectionType.REVERSE)

while True:
    if leftMotor.velocity() > 0:
        print(leftMotor.velocity())
    sleep(2, SECONDS)
    print (randy + 2)