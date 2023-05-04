
    if check("the robot's gripper is not vertically aligned with the plate handle and the robot's gripper is not near the plate handle"):
        robot.move("gripper near plate handle")
    if check("the robot's gripper is vertically aligned with the plate handle and the robot's gripper is not near plate handle"):
        robot.move("gripper to plate handle")
    if check("the robot's gripper is in front of the plate handle and the robot's gripper is not right of the plate handle"):
        robot.move("plate handle to right of gripper")
    if check("the robot's gripper is vertically aligned with the plate handle"):
        robot.move("the plate to the goal")

# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    if check("the robot's gripper is not vertically aligned with the plate handle and the robot's gripper is not near the plate handle"):
        robot.move("gripper near plate handle")
    if check("the robot's gripper is vertically aligned with the plate handle and the robot's gripper is not near plate handle"):
        robot.move("gripper to plate handle")
    if check("the robot's gripper is in front of the plate handle and the robot's gripper is not behind the plate handle"):
        robot.move("plate handle behind gripper")
    if check("the robot's gripper is vertically aligned with the plate handle"):
        robot.move("the plate to the goal")

# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate handle and the robot's gripper is not near the plate handle"):
        robot.move("gripper near plate handle")
    if check("the robot's gripper is vertically aligned with the plate handle and the robot's gripper is not near plate handle"):
        robot.move("gripper to plate handle")
    if check("the robot's gripper is in front of the plate handle"):
        robot.move("plate to the goal")

# plate-slide: slide the plate to the target location
def plate_slide(robot):
    if check("the robot's gripper is not vertically aligned with the plate handle and the robot's gripper is not near the plate handle"):
        robot.move("gripper