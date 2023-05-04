
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not near the plate"):
        robot.slide("gripper into plate")
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.push("plate to goal")

# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    if check("the plate is not left of the robot's gripper"):
        robot.grab("plate")
    if check("the plate is left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.slide("plate to the right")
    if check("the plate is forward aligned with the robot's gripper and the plate is not horizontally aligned with the target"):
        robot.align("plate to the goal")
    if check("plate is horizontally aligned with the target"):
        robot.insert("plate into the goal")

# plate-press: slide the plate forward into the target
def plate_press(robot):
    if check("the plate is not left of the robot's gripper"):
        robot.grab("plate")
    if check("the plate is left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.slide("plate forward")
    if check("the plate is forward aligned with the robot's gripper and the plate is not horizontally aligned with the target"):
        robot.align("plate to the goal")
    if check("plate is horizontally aligned with the target"):
        robot.insert("plate into the goal")

# push-microwave: push the buttons from left to right
def push_microwave(robot):
    if check("the robot's gripper is not left of button 1"):
        robot.put("gripper left of button 1")
    if check("the robot's gripper is left of button 1 and the robot's gripper is not in front of button 1"):
        robot.push("into button 1")
    if check("the robot's gripper is in front of button 1 and the robot's gripper is not left of button 2"):
        robot.grab("button 1")