
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the plate is above the robot's gripper and the robot's gripper is vertically aligned with plate"):
        robot.grab("plate")
    if check("the robot's gripper is vertically aligned with plate and the plate is forward aligned with robot's gripper"):
        robot.push("plate to left")
    if check("the plate is in front of the robot's gripper and the robot's gripper is not near plate"):
        robot.push("plate left harder")

# plate-slide-front-side: slide the plate forward sideways into the target location
def plate_slide_front_side(robot):
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the plate is above the robot's gripper and the robot's gripper is vertically aligned with plate"):
        robot.grab("plate")
    if check("the robot's gripper is vertically aligned with plate and the plate is forward aligned with robot's gripper"):
        robot.push("plate to right")
    if check("the plate is in front of the robot's gripper and the robot's gripper is not near plate"):
        robot.push("plate right harder")

# plate-slide-back-front: slide the plate back forward into the target location
def plate_slide_back_front(robot):
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the plate is above the robot's gripper and the robot's gripper is vertically aligned with plate"):
        robot.grab("plate")
    if check("the robot's gripper is vertically aligned with plate and the plate is forward aligned with robot's gripper"):
        robot.push("plate back")
    if check("the plate is in front of the robot's gripper and the robot's gripper is not near plate"):
        robot.push("plate back harder")

# plate-slide-front-back: slide the plate forward back into the target location
def plate_slide_front_back(robot):
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the plate is above the