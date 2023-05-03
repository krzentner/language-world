# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull the handle up
    # First, put the gripper roughly above the handle, so that we can see it
    if check("the robot's gripper is not above the handle"):
        robot.place("gripper above handle")
    # If the gripper is above the handle, move gripper down to grab the handle
    if check("the robot's gripper is above handle and the robot's gripper is not around handle"):
        robot.drop("gripper around handle")
    # If the gripper is around the handle, pull the handle upwards
    if check("the robot's gripper is around handle"):
        robot.pull("handle upwards from the side")