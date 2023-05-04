
    if check("the robot's gripper is not vertically aligned with plate and the robot's gripper is below the plate"):
        robot.move("the gripper above the plate")
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not near the plate"):
        robot.push("the gripper into the plate")
    if check("the robot's gripper is near the plate and the robot's gripper is not horizontally aligned with plate"):
        robot.align("gripper with plate")
    if check("the robot's gripper is horizontally aligned with plate and the robot's gripper is not above the target location"):
        robot.slide("the plate back")
    if check("the robot's gripper is above the target location"):
        robot.push("the plate into the goal")

# plate-slide: slide the plate away from the target location
def plate_slide(robot):
    if check("the robot's gripper is not vertically aligned with plate and the robot's gripper is below the plate"):
        robot.move("the gripper above the plate")
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not near the plate"):
        robot.push("the gripper into the plate")
    if check("the robot's gripper is near the plate and the robot's gripper is not horizontally aligned with plate"):
        robot.align("gripper with plate")
    if check("the robot's gripper is horizontally aligned with plate and the robot's gripper is not above the target location"):
        robot.slide("the plate forward")
    if check("the robot's gripper is above the target location"):
        robot.pull("the plate away from the goal")

# plate-slide-side: slide the plate to the left from the target location
def plate_slide_side(robot):
    if check("the robot's gripper is not vertically aligned with plate and the robot's gripper is below the plate"):
        robot.move("the gripper above the plate")
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not near the plate"):
        robot.push("the gripper into the plate")
    if check("the robot's gripper is near the plate and the robot's gripper is not horizontally aligned with plate"):
        robot.align("gripper with