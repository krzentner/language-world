
    if check("the robot's gripper is not below stick"):
        robot.reach("down to stick")
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.put("gripper around stick")
    if check("the robot's gripper is around stick"):
        robot.pull("stick to goal")

# hammer: grab the hammer and use it to hit the bell
def hammer(robot):
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.move("gripper above hammer")
    if check("the robot's gripper is vertically aligned with the hammer and the hammer is below the robot's gripper"):
        robot.grab("hammer")
    if check("the robot's gripper is around the hammer"):
        robot.hit("hammer on bell")

# hammer-side: grab the hammer and use it to hit the bell from the side
def hammer_side(robot):
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.move("gripper above hammer")
    if check("the robot's gripper is vertically aligned with the hammer and the hammer is below the robot's gripper"):
        robot.grab("hammer")
    if check("the robot's gripper is around the hammer"):
        robot.hit("hammer on bell from the side")

# scoop: grab the spoon and use it to scoop the ball into the cup
def scoop(robot):
    if check("the robot's gripper is not above spoon"):
        robot.put("gripper above spoon")
    if check("the robot's gripper is not around spoon and the robot's gripper is open"):
        robot.drop("gripper around spoon")
    if check("the robot's gripper is above spoon and the robot's gripper is closed"):
        robot.reach("to ball")
    if check("the robot's gripper is near ball"):
        robot.push("spoon into ball")
    if check("the robot's gripper is near ball and the robot's gripper is forward aligned with ball"):
        robot.slide("ball into cup")

# pour: use the cup to pour the ball into the bowl
def pour(robot):
    if check("the robot's gripper is not near cup"):
        robot.reach("to cup")
 