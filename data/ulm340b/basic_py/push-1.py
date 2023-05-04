
    if check("the robot's gripper is not near puck and the robot's gripper is not above puck"):
        robot.move("gripper above puck")
    if check("the robot's gripper is above puck and puck is not to left of the robot's gripper"):
        robot.move("puck to left of robot's gripper")
    if check("puck is left of the robot's gripper"):
        robot.push("puck to goal")

# slide: slide the puck to the target location
def slide(robot):
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above puck and puck is not left of the robot's gripper"):
        robot.move("puck to left of robot's gripper")
    if check("the robot's gripper is above puck and puck is left of the robot's gripper"):
        robot.slide("puck to goal")

# insert: insert the block into the hole
def insert(robot):
    if check("block is not left of the robot's gripper and the robot's gripper is not above block"):
        robot.place("gripper above block")
    if check("the robot's gripper is above block and the robot's gripper is not around block"):
        robot.drop("gripper around block")
    if check("the robot's gripper is above block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.align("block to hole")
    if check("the robot's gripper is near hole"):
        robot.insert("block into hole")

# push-block-side: push the block to the goal
def push_block_side(robot):
    if check("the robot's gripper is not above the block"):
        robot.put("gripper above block")
    if check("the robot's gripper is above the block and the block is not to left of the robot's gripper"):
        robot.move("block to left of robot's gripper")
    if check("the robot's gripper is above the block and the block is to left of the robot's gripper"):
        robot.push("