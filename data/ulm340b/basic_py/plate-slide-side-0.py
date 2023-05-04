
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near plate"):
        robot.slide("the gripper to the plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is near the plate"):
        robot.push("the plate to the goal")

# plate-slide-topdown: slide the plate from above into the target location
def plate_slide_topdown(robot):
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near plate"):
        robot.slide("the gripper to the plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is near the plate"):
        robot.push("the plate to the goal")

# spatula-slide: use a spatula to slide an object to the target location
def spatula_slide(robot):
    if check("the robot's gripper is not vertically aligned with spatula"):
        robot.put("gripper above spatula")
    if check("the robot's gripper is vertically aligned with spatula and the robot's gripper is not near spatula"):
        robot.slide("gripper to spatula")
    if check("the robot's gripper is near spatula and the robot's gripper is not forward aligned with spatula"):
        robot.align("gripper to spatula")
    if check("the robot's gripper is forward aligned with spatula and the object is not below the spatula"):
        robot.slide("object under spatula")
    if check("the object is below the spatula and the spatula is not vertically aligned with object"):
        robot.align("spatula to object")
    if check("the spatula is vertically aligned with object and the spatula is not in front of object"):
        robot.align("spatula to object")
    if check("the spatula is vertically aligned with object and the object is not forward aligned with goal"):
        robot.align("spatula to goal")
    if check("the spatula is vertically aligned with object and the object is forward aligned with goal"):
        robot.push("object to goal")
