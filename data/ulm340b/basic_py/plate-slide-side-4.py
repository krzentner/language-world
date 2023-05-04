
    if check("the robot's gripper is not above plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is above plate and the robot's gripper is not near plate"):
        robot.move("gripper down to plate")
    if check("the robot's gripper is near plate"):
        robot.move("plate to goal")

# plate-slide-front: push the plate into the target location
def plate_slide_front(robot):
    if check("the robot's gripper is not near plate"):
        robot.grab("plate")
    if check("the robot's gripper is near plate"):
        robot.push("plate to goal")

# block-slide-side: slide the block sideways into the target location
def block_slide_side(robot):
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.put("gripper above block")
    if check("the robot's gripper is above block and the robot's gripper is not near block"):
        robot.grab("block")
    if check("the robot's gripper is near block"):
        robot.move("block to goal")

# block-slide-front: push the block into the target location
def block_slide_front(robot):
    if check("the robot's gripper is not vertically aligned with block"):
        robot.put("gripper above block")
    if check("the robot's gripper is not near block"):
        robot.move("gripper to block")
    if check("the robot's gripper is near block"):
        robot.move("block to goal")

# push-back: push the object back along a track to the target location
def push_back(robot):
    if check("the robot's gripper is not above object"):
        robot.put("gripper above object")
    if check("the robot's gripper is above object and the robot's gripper is not near object"):
        robot.move("gripper onto object")
    if check("the robot's gripper is near object"):
        robot.push("object back to goal")

# pick: pick up the object from the target location
def pick(robot):
    if check("the robot's gripper is not above object"):
        robot.put("gripper above object")
    if