
"""

task_descriptions = {
    "reach": {
        "instruction":
            """Steps:  1. Reach towards the target""",
        "steps":
            [
                "When the robot's gripper is not near reach target, move the robot's gripper until the robot's gripper is near the reach target"
            ],
    },
    "button-press-topdown": {
        "instruction":
            """Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top""",
        "steps":
            [
                "When the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button and the robot's gripper is closed",
                "When the robot's gripper is vertically aligned with button, move the robot's gripper until the robot's gripper is near the button"
            ],
    },
    "peg-insert-side": {
        "instruction":
            """Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg sideways into the hole""",
        "steps":
            [
                "When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg",
                "When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the peg and the robot's gripper is closed",
                "When peg is horizontally aligned with hole, move the robot's gripper until the robot's gripper is above the peg",
                "When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, move the robot's gripper until the robot's gripper is horizontally aligned with hole"
            ],
    },
    "drawer-close": {
        "instruction":
            """Steps:  1. Put gripper roughly around the drawer handle  2. Push the drawer closed""",
        "steps":
            [
                "When the robot's gripper is not near the drawer handle, move the robot's gripper until the robot's gripper is near the drawer handle",
                "When the robot's gripper is forward aligned with drawer handle, move the robot's gripper until the robot's gripper is