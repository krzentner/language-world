

"""

drawer_open_definition = """
def drawer_open(robot):
    """
    # Steps:
    #  1. Move gripper to be below the drawer handle
    #  2. Drop gripper around the drawer handle
    #  3. Pull open the drawer
    # To make sure the drawer is not already open, check if the gripper is
    # vertically aligned with the drawer handle, otherwise move the gripper below
    # the drawer handle.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.grab("drawer handle")
    # Next, drop the gripper around the handle to get a grip.
    if check("the robot's gripper is not around the drawer handle and the robot's gripper is open"):
        robot.close("gripper around drawer handle")
    # Lastly, while the gripper is still mostly around the drawer handle, pull
    # the drawer open.
    if check("the robot's gripper is mostly around the drawer handle"):
        robot.pull("drawer open")
"""

instruction_template = """
# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Move gripper to be below the drawer handle
    #  2. Drop gripper around the drawer handle
    #  3. Pull open the drawer
    # To make sure the drawer is not already open, check if the gripper is
    # vertically aligned with the drawer handle, otherwise move the gripper below
    # the drawer handle.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.grab("drawer handle")
    # Next, drop the gripper around the handle to get a grip.
    if check("the robot's gripper is not around the drawer handle and the robot's gripper is open"):
        robot.close("gripper around drawer handle")
    # Lastly, while the gripper is still mostly around the drawer handle, pull
    # the drawer open.
    if check("the robot's gripper is mostly around the drawer handle"):
        robot.pull("drawer open")

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    # 