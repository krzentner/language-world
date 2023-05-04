
    if check("the robot's gripper is not near mug handle"):
        robot.put("gripper near mug handle")
    if check("the robot's gripper is near the mug handle and the robot's gripper is open"):
        robot.put("gripper around mug handle")
    if check("the robot's gripper is near mug handle and the robot's gripper is closed"):
        robot.pull("the mug from the table")

# coffee-push: push the mug to the target location
def coffee_push(robot):
    if check("the robot's gripper is not near mug handle"):
        robot.put("gripper near mug handle")
    if check("the robot's gripper is near the mug handle and the robot's gripper is open"):
        robot.put("gripper around mug handle")
    if check("the robot's gripper is near mug handle and the robot's gripper is closed"):
        robot.push("the mug onto the table")

# coffee-slide: slide the mug to the target location
def coffee_slide(robot):
    if check("the robot's gripper is not above the mug handle"):
        robot.put("gripper above mug handle")
    if check("the robot's gripper is not near mug handle"):
        robot.put("gripper into mug handle")
    if check("the robot's gripper is above the mug handle and the robot's gripper is near mug handle"):
        robot.push("the mug to the table")
    if check("the robot's gripper is above the mug handle and the robot's gripper is near mug handle"):
        robot.move("the mug to the goal")

# stack: pick up the block and place it on top of the other block
def stack(robot):
    if check("the robot's gripper is not above the block"):
        robot.put("gripper above block")
    if check("the robot's gripper is above the block and the robot's gripper is not near block"):
        robot.put("gripper near block")
    if check("the robot's gripper is above the block and the robot's gripper is near block"):
        robot.close("gripper around block")
    if check("the robot's gripper is above the block and the robot's gripper is closed around block"):
        robot.lift("block into air")
  