# plate-slide-back-side: slide the plate back sideways into the target location
# def plate_slide_back_side(robot):
def plate_slide_back_side(robot):
    if check("the robot's gripper is not above or below the plate"):
        robot.lift("gripper above the plate")
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move("gripper to the left or right side of the plate")
    if check("the plate is not between the robot's gripper and the target location"):
        robot.move("gripper towards the plate")
    if check("the plate is between the robot's gripper and the target location"):
        robot.slide("plate back into the target location sideways") 

# check function
def check(condition):
    if condition:
        return True
    else:
        return False

# example usage
plate_slide_back_side(robot)