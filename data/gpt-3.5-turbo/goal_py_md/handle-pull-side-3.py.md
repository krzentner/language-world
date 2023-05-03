# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    # 1. Put gripper right of the handle
    # 2. Grab the handle with the gripper
    # 3. Move the gripper up and slightly towards the robot
    # 4. Pull the handle up
    if check("the robot's gripper is not right of the handle"):
        robot.move_gripper("right of the handle")
    if check("the robot's gripper is not around the handle and the robot's gripper is right of the handle"):
        robot.move_gripper("around the handle")
    if check("the robot's gripper is not above the handle and the robot's gripper is around the handle"):
        robot.move_gripper("above the handle and slightly towards the robot")
    if check("the robot's gripper is above the handle"):
        robot.move_gripper("slightly towards the robot")
    if check("the robot's gripper is slightly towards the robot"):
        robot.move_gripper("up and more towards the robot")
    if check("the robot's gripper is up and towards the robot"):
        robot.move_gripper("up and towards the robot", close_gripper=False)

# Helper function to check the status of the robot's gripper
def check(status):
    if status in robot.check_gripper():
        return True
    else:
        return False