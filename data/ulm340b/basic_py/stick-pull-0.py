
    if check("the robot's gripper is not vertically aligned with stick"):
        robot.put("gripper above stick")
    if check("the robot's gripper is vertically aligned with stick"):
        robot.grab("stick")
    if check("the robot's gripper is near stick"):
        robot.pull("stick towards thermos")
    if check("the robot's gripper is near stick and the robot's gripper is closed"):
        robot.pull("stick towards goal")

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    if check("the robot's gripper is not vertically aligned with stick"):
        robot.put("gripper above stick")
    if check("the robot's gripper is vertically aligned with stick"):
        robot.grab("stick")
    if check("the robot's gripper is near stick"):
        robot.push("stick towards thermos")
    if check("the robot's gripper is near stick"):
        robot.push("stick towards goal")

# block-stack-side: stack the block onto the block below from the side
def block_stack_side(robot):
    if check("the robot's gripper is not above block"):
        robot.place("gripper above block")
    if check("the robot's gripper is above block and the robot's gripper is not around block"):
        robot.drop("gripper around block")
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.put("block on goal")

# block-stack-topdown: stack the block onto the block below from above
def block_stack_topdown(robot):
    if check("the robot's gripper is not near block and the robot's gripper is not vertically aligned with block"):
        robot.put("gripper above block")
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
  