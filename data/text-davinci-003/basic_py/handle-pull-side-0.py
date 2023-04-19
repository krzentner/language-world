
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.grab("handle")
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")

# unscrew: unscrew the screw from the board
# def unscrew(robot):
    if check("the robot's gripper is not vertically aligned with the screw"):
        robot.put("gripper above screw")
    if check("the robot's gripper is vertically aligned with the screw and the robot's gripper is not above screw"):
        robot.grab("screw inside the gripper")
    if check("the robot's gripper is above screw"):
        robot.rotate("counter clockwise")