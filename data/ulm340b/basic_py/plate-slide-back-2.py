
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move("gripper above plate")
    if check("the robot's gripper is near the plate and the plate is not close to the goal"):
        robot.push("plate to goal")
    if check("the robot's gripper is in front of the plate"):
        robot.slide("plate forward")

# cup-slide-back: slide the cup back into the target location
def cup_slide_back(robot):
    if check("the robot's gripper is not vertically aligned with the cup"):
        robot.put("gripper above cup")
    if check("the robot's gripper is vertically aligned with the cup and the robot's gripper is not near the cup"):
        robot.grab("cup")
    if check("the robot's gripper is near the cup"):
        robot.slide("cup towards goal")
    if check("the robot's gripper is in front of the cup"):
        robot.push("cup forward into goal")

# plate-slide-left: slide the plate from the left to the target location
def plate_slide_left(robot):
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper over plate")
    if check("the robot's gripper is above the plate and the robot's gripper is not near the plate"):
        robot.drop("gripper on plate")
    if check("the robot's gripper is near the plate and the plate is not close to the goal"):
        robot.push("plate to goal")
    if check("the robot's gripper is in front of the plate"):
        robot.slide("plate forward")

# cup-slide-left: slide the cup from the left to the target location
def cup_slide_left(robot):
    if check("the robot's gripper is not vertically aligned with the cup"):
        robot.place("gripper above cup")
    if check("the robot's gripper is vertically aligned with the cup and the robot's gripper is not near the cup"):
        robot.grab("cup")
    if check("the robot's gripper is near the cup"):
        robot.slide("cup towards goal")
    if check("the robot's gripper is in front of the cup"):
        robot.push("cup forward into goal")

#