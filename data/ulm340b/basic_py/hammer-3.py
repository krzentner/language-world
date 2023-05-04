
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.put("gripper above hammer")
    if check("the hammer is not vertically aligned with the nail and the hammer is below the robot's gripper"):
        robot.move("hammer to nail")
    if check("the hammer is vertically aligned with the nail"):
        robot.strike("nail with hammer")

# lift: lift the tool using the rope
def lift(robot):
    if check("the robot's gripper is not above the tool"):
        robot.move("gripper above tool")
    if check("the robot's gripper is below the tool"):
        robot.lift("tool with rope")

# spatula: flip over the pancake with the spatula
def spatula(robot):
    if check("the robot's gripper is not vertically aligned with the spatula"):
        robot.move("gripper to spatula")
    if check("the robot's gripper is vertically aligned with the spatula and the robot's gripper is not around the spatula"):
        robot.grab("spatula")
    if check("the robot's gripper is around the spatula and the robot's gripper is not forward aligned with the spatula"):
        robot.orient("spatula")
    if check("the robot's gripper is forward aligned with the spatula and the spatula is not horizontally aligned with the pancake"):
        robot.align("spatula with pancake")
    if check("the spatula is horizontally aligned with the pancake"):
        robot.flip("pancake with spatula")


# BEHAVIORS
# lift with spatula
def lift_w_spatula(robot):
    if check("the robot's gripper is not vertically aligned with the spatula"):
        robot.move("gripper to spatula")
    if check("the robot's gripper is vertically aligned with the spatula and the robot's gripper is not around the spatula"):
        robot.grab("spatula")
    if check("the robot's gripper is around the spatula and the robot's gripper is not forward aligned with the spatula"):
        robot.orient("spatula")
    if check("the robot's gripper is forward aligned with the spatula and the spatula is not horizontally aligned with the tool"):
        robot.align("spatula with tool")
    if check("the spatula is horizontally aligned with the tool"):
        robot.lift("tool with spatula")

# lift with tongs
def