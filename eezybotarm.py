import math
import numpy as np
from transformation import *

class EezyBotArm:
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """
    #

    # Link lengths (all in mm)
    l1 = 92.0
    l2 = 135.0
    l3 = 147.0
    l4 = 87.0

    def __init__(self, q1: float = 0.0, q2: float = 0.0, q3: float = 0.0) -> None:
        """Sets initial joint values."""
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3

    def convert_cmds(self, *args: str) -> list:
        to_return = []
        for arg in args:
            for i in arg:
                to_return.append(float(i))
        return to_return

    def get_joints(self) -> list:
        return [self.q1, self.q2, self.q3]

    def set_joints(self, joints: list) -> None:
        # Unwrap and convert to radians
        q1 = joints[0] * np.pi/180
        q2 = joints[1] * np.pi/180
        q3 = joints[2] * np.pi/180

        self.q1 = q1
        self.q2 = q2
        self.q3 = q3

    def fwd_kin(self) -> np.array:
        T_b = np.identity(4)
        T_b1 = transz(self.l1) @ rotz(self.q1) @ T_b
        T_12 = rotx(np.pi/2)   @ rotz(self.q2) @ T_b1
        T_23 = transx(self.l2) @ rotz(self.q3) @ T_12
        T_34 = transx(self.l3) @ rotx(-np.pi/2) @ T_23
        T_ee = transx(self.l4 * np.cos(self.q1)) @ transy(self.l4 * np.sin(self.q1)) @ T_34
        return T_ee

    def fwdkin(self) -> np.array:
        # Find the position of the end effector using the forward kinematics equations
        x_EE = round((np.cos(self.q1) * (np.cos(self.q2+self.q3)*self.l3 + np.cos(self.q2)*self.l2))+(self.l4*np.cos(self.q1)), 3)
        y_EE = round((np.sin(self.q1) * (np.cos(self.q2+self.q3)*self.l3 + np.cos(self.q2)*self.l2))+(self.l4*np.sin(self.q1)), 3)
        z_EE = round((self.l1 + np.sin(self.q2)*self.l2 + np.sin(self.q2+self.q3)*self.l3), 3)

        # Return the end effector position in (mm)
        return x_EE, y_EE, z_EE

# robot = EezyBotArm(0, np.pi, 0)
# print(robot.fwd_kin()[0:3, 3])
# print(robot.fwdkin())