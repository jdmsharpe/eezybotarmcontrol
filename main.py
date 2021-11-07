import time
# from adafruit_servokit import ServoKit
from eezybotarm import *

robot = EezyBotArm(0, 0, 0)
# kit = ServoKit(channels=16)

while True:
    cmd = input("Please enter EE XYZ coords: \n").split(" ")
    parsed_cmd = robot.convert_cmds(cmd)
    robot.set_joints(parsed_cmd)
    print(robot.fwdkin())