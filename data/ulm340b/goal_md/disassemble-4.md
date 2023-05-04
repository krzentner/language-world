I am not sure about this task, and am asking you for advice.
"""


def intro_text():
    return INTRO_TEXT


def task_to_instructions(task_key):
    # instructions_dict = {
    #     "peg-insert-side": """
    # To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    #    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg sideways into the hole
    #    First, put the gripper above the peg.
    #    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    #    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    #    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the peg and the robot's gripper is closed
    #    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    #    - When peg is horizontally aligned with hole, move the robot's gripper until the robot's gripper is above the peg
    #    If the peg is lined up with the hole to the side, insert it.
    #    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, move the robot's gripper until the robot's gripper is horizontally aligned with hole
    # """,
    #     "reach": """
    # To reach to the target location reliably, the robot should perform the following steps:
    #    Steps:  1. Reach towards the target
    #    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    #    - When the robot's gripper is not near reach target, move the robot's gripper until the robot's gripper is near the reach target
 