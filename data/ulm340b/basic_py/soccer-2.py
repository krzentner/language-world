
    if check("the robot's gripper is not above the soccer ball"):
        robot.put("the gripper above the soccer ball")
    if check("the robot's gripper is above the soccer ball and the robot's gripper is not near the soccer ball"):
        robot.push("the soccer ball to the goal")

# hammer: pick up the hammer and hit the nail
def hammer(robot):
    if check("the robot's gripper is not above the hammer"):
        robot.put("the gripper above the hammer")
    if check("the robot's gripper is above the hammer and the robot's gripper is not near the hammer"):
        robot.grab("hammer")
    if check("the robot's gripper is forward aligned with the hammer and the hammer is not above the nail"):
        robot.align("the hammer to the nail")
    if check("the hammer is above the nail"):
        robot.hit("the nail with the hammer")

# basketball: pick up the basketball and hold it at the target location
def basketball(robot):
    if check("the robot's gripper is not above the basketball"):
        robot.put("the gripper above the basketball")
    if check("the robot's gripper is above the basketball and the robot's gripper is not near the basketball"):
        robot.grab("the basketball")
    if check("the robot's gripper is around the basketball and the robot's gripper is above the basketball"):
        robot.move("the basketball to the goal")

# tennis: pick up the tennis ball and hold it at the target location
def tennis(robot):
    if check("the robot's gripper is not above the tennis ball"):
        robot.put("the gripper above the tennis ball")
    if check("the robot's gripper is above the tennis ball and the robot's gripper is not near the tennis ball"):
        robot.grab("the tennis ball")
    if check("the robot's gripper is around the tennis ball and the robot's gripper is above the tennis ball"):
        robot.move("the tennis ball to the goal")

# lasso-rope: lasso the hula-hoop with the rope
def lasso_rope(robot):
    if check("the robot's gripper is not above the hula hoop"):
        robot.put("the gripper above the hula hoop")
    if check("the robot's gripper