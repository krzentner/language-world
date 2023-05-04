
"""



_ANSWER_KEYS = [


    "drawer-open",
    "When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.",
    "When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.",
    "When the robot's gripper is around drawer handle, the robot should pull away from drawer.",

    "door-lock",
    "When the robot's gripper is not vertically aligned with door handle, the robot should put gripper above door handle.",
    "When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.",
    "When the robot's gripper is vertically aligned with the door handle, the robot should pull door open.",

    "reach",
    "When the robot's gripper is not near reach target, the robot should reach to goal.",

    "door-open",
    "When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.",
    "When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.",
    "When the robot's gripper is vertically aligned with the door handle, the robot should pull door open.",

    "button-press-topdown",
    "When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.",
    "When the robot's gripper is vertically aligned with button, the robot should push down on button.",

    "drawer-close",
    "When the robot's gripper is not near the drawer handle, the robot should grab drawer handle.",
    "When the robot's gripper is forward aligned with drawer handle, the robot should push drawer closed.",

    "peg-insert-side",
    "When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.",
    "When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.",
    "When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.",
    "When peg is horizontally aligned with hole, the robot should insert peg into hole.",