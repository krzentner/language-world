
    if check("the robot's gripper is not above block"):
        robot.place("gripper above block")
    if check("the robot's gripper is above block"):
        robot.grasp("block")
    if check("the robot's gripper is forward aligned with block"):
        robot.lift("block")
    if check("the robot's gripper is almost above goal"):
        robot.move("block to goal")
    if check("the robot's gripper is above goal"):
        robot.put("block on goal")
    if check("the block is on goal"):
        robot.release("block")

# shelf-push: slide the block to the target location
def shelf_push(robot):
    if check("the robot's gripper is not above block and the robot's gripper is not vertically aligned with the block"):
        robot.put("the gripper above the block")
    if check("the robot's gripper is vertically aligned with the block and the robot's gripper is not near block"):
        robot.push("the gripper into the block")
    if check("the robot's gripper is near the block and the block is below the robot's gripper"):
        robot.slide("the block to the goal")

# shelf-remove: pull the block off of the shelf
def shelf_remove(robot):
    if check("the robot's gripper is not almost vertically aligned with block"):
        robot.put("gripper above block")
    if check("the robot's gripper is almost vertically aligned with block and the robot's gripper is open"):
        robot.put("gripper around block")
    if check("the robot's gripper is vertically aligned with block and the robot's gripper is closed"):
        robot.pull("block off shelf")

# peg-unstack: pick up the smaller object and place it on top of the larger object
def peg_unstack(robot):
    if check("the robot's gripper is not above smaller block"):
        robot.place("gripper above smaller block")
    if check("the robot's gripper is above smaller block"):
        robot.grasp("smaller block")
    if check("the robot's gripper is vertically aligned with smaller block"):
        robot.lift("smaller block")
    if check("the robot's gripper is above larger block"):
        robot.move