
    if check("the robot's gripper is not above plate handle"):
        robot.move("gripper above plate handle")
    if check("the robot's gripper is above plate handle"):
        robot.grab("plate handle")
    if check("the robot's gripper is forward aligned with plate handle"):
        robot.slide("plate to goal")

# plate-slide-back-side-side: slide the plate sideways back to the right
def plate_slide_back_side_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate handle"):
        robot.put("gripper above plate handle")
    if check("the robot's gripper is vertically aligned with the plate handle and the robot's gripper is open"):
        robot.put("gripper around plate handle")
    if check("the robot's gripper is vertically aligned with plate handle and the robot's gripper is closed"):
        robot.slide("plate to right")

# plate-slide-forward-side: slide the plate forward sideways into the target location
def plate_slide_forward_side(robot):
    if check("the robot's gripper is not above plate handle"):
        robot.move("gripper above plate handle")
    if check("the robot's gripper is above plate handle"):
        robot.grab("plate handle")
    if check("the robot's gripper is backward aligned with plate handle"):
        robot.slide("plate to goal")

# plate-slide-forward-side-side: slide the plate sideways forward to the right
def plate_slide_forward_side_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate handle"):
        robot.put("gripper above plate handle")
    if check("the robot's gripper is vertically aligned with the plate handle and the robot's gripper is open"):
        robot.put("gripper around plate handle")
    if check("the robot's gripper is vertically aligned with plate handle and the robot's gripper is closed"):
        robot.slide("plate to right")

# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    if check("the robot's gripper is not above plate handle"):
        robot.move("gripper above plate handle")
    if check("the robot's gripper is above plate handle"):
