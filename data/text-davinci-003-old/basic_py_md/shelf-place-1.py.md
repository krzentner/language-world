 

if check("the robot's gripper is not above the block"):
    robot.place("gripper above block")
if check("the robot's gripper is not around block and the robot's gripper is open"):
    robot.drop("gripper around block")
if check("the robot's gripper is near block and the robot's gripper is open"):
    robot.close("gripper around block")
if check("the robot's gripper is above block and the robot's gripper is closed"):
    robot.reach("to shelf")
if check("the robot's gripper is near shelf and the block is below the robot's gripper"):
    robot.slide("the block to the shelf")
if check("the robot's gripper is above shelf and the block is below the robot's gripper"):
    robot.place("block on shelf")
if check("the robot's gripper is around block and the block is on shelf"):
    robot.release("gripper from block")