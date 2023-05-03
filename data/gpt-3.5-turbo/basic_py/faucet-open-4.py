if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper to faucet handle")
    if check("the robot's gripper is not around the faucet handle"):
        robot.grasp("faucet handle")
    if check("the robot's gripper is around the faucet handle and the faucet handle is at the 'off' position"):
        robot.turn("faucet left") 

# faucet-close: turn the faucet right
def faucet_close(robot):
    if check("the robot's gripper is not near the faucet handle"):
        robot.move("gripper to faucet handle")
    if check("the robot's gripper is not around the faucet handle"):
        robot.grasp("faucet handle")
    if check("the robot's gripper is around the faucet handle and the faucet handle is at the 'on' position"):
        robot.turn("faucet right") 

# screwdriver-use: use the screwdriver to turn the screw
def screwdriver_use(robot):
    if check("the robot's gripper is not near screw head"):
        robot.move("gripper to screw head")
    if check("the robot's gripper is not around screw head"):
        robot.grasp("screw head")
    if check("the robot's gripper is around screw head and the screwdriver is not aligned with the screw head"):
        robot.align("screwdriver to screw head")
    if check("the screwdriver is aligned with the screw head and the screwdriver is not turned"):
        robot.turn("screwdriver") 

# object-retrieval: retrieve the desired object
def object_retrieval(robot):
    if check("the robot's gripper is not near desired object"):
        robot.reach("to object")
    if check("the robot's gripper is near the desired object and the object is not grasped"):
        robot.grasp("object")
    if check("the robot's gripper is grasping object and the object is not at the goal location"):
        robot.move("object to goal")
    if check("the object is at the goal location and the gripper is grasping object"):
        robot.release("object") 

# box-open: open the box flaps
def box_open(robot):
    if check("the robot's gripper is not near the box flaps"):
        robot.move("gripper to box flaps")
    if check("the robot's gripper is not around the box flaps"):
        robot.grasp("box flaps")
    if check("the robot's gripper is around the box flaps and the box flaps are not open"):
        robot.pull("box flaps open") 

# box-close: close the box flaps
def box_close(robot):
    if check("the robot's gripper is not near the box flaps"):
        robot.move("gripper to box flaps")
    if