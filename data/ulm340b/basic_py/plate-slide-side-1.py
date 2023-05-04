
    if check("the robot's gripper is not above the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is above the plate and the robot's gripper is not near the plate"):
        robot.slide("the plate in")
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.push("plate harder")

# plate-slide-top: slide the plate along its length into the target location
def plate_slide_top(robot):
    if check("the robot's gripper is not above the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is above the plate and the robot's gripper is not near the plate"):
        robot.slide("the plate in")
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.push("plate harder")

# slide-back-side: slide the large block sideways into the target location
def slide_back_side(robot):
    if check("the robot's gripper is not above the block"):
        robot.put("the gripper above the block")
    if check("the robot's gripper is above the block and the robot's gripper is not near the block"):
        robot.slide("the block sideways")
    if check("the robot's gripper is near the block and the block is below the robot's gripper"):
        robot.push("block sideways harder")

# slide-back-top: slide the large block along its length into the target location
def slide_back_top(robot):
    if check("the robot's gripper is not above the block"):
        robot.put("the gripper above the block")
    if check("the robot's gripper is above the block and the robot's gripper is not near the block"):
        robot.slide("the block forward")
    if check("the robot's gripper is near the block and the block is below the robot's gripper"):
        robot.push("block forward harder")

# pick-out-of-hole: pick the puck out of the hole
def pick_out_of_hole(robot):
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above