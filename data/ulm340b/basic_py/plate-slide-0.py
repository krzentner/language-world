
    if check("the robot's gripper is not above plate and the robot's gripper is not vertically aligned with plate"):
        robot.place("gripper above plate")
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not near plate"):
        robot.push("gripper into plate")
    if check("the robot's gripper is near plate"):
        robot.slide("plate into goal")

# block-slide: slide the block into the target location
def block_slide(robot):
    if check("the robot's gripper is not above block and the robot's gripper is not vertically aligned with block"):
        robot.place("gripper above block")
    if check("the robot's gripper is vertically aligned with block and the robot's gripper is not near block"):
        robot.push("gripper into block")
    if check("the robot's gripper is near block"):
        robot.slide("block into goal")

# block-pickup: pick up the block and bring it to the target location
def block_pickup(robot):
    if check("the robot's gripper is not vertically aligned with block and the robot's gripper is not near block"):
        robot.move("gripper above block")
    if check("the robot's gripper is vertically aligned with block and the robot's gripper is not around block"):
        robot.grab("block")
    if check("the robot's gripper is above block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is closed around block and the robot's gripper is above the block"):
        robot.move("block to goal")

# block-pickup-side: pick up the block and bring it to the target location
def block_pickup_side(robot):
    if check("the robot's gripper is not vertically aligned with block and the robot's gripper is not near block"):
        robot.put("gripper above block")
    if check("the robot's gripper is vertically aligned with block and the robot's gripper is not around block"):
        robot.grab("block")
    if check("the robot's gripper is above block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is closed around