# move-gripper-left: move the gripper to the left by a given distance
def move_gripper_left(robot, distance):
    robot.move("gripper left by " + str(distance) + " units")

# move-gripper-right: move the gripper to the right by a given distance
def move_gripper_right(robot, distance):
    robot.move("gripper right by " + str(distance) + " units")

# move-gripper-up: move the gripper up by a given distance
def move_gripper_up(robot, distance):
    robot.move("gripper up by " + str(distance) + " units")

# move-gripper-down: move the gripper down by a given distance
def move_gripper_down(robot, distance):
    robot.move("gripper down by " + str(distance) + " units") 

# rotate-gripper-left: rotate the gripper to the left by a given angle 
def rotate_gripper_left(robot, angle):
    robot.rotate("gripper left by " + str(angle) + " degrees")

# rotate-gripper-right: rotate the gripper to the right by a given angle 
def rotate_gripper_right(robot, angle):
    robot.rotate("gripper right by " + str(angle) + " degrees")

# rotate-gripper-up: rotate the gripper up by a given angle 
def rotate_gripper_up(robot, angle):
    robot.rotate("gripper up by " + str(angle) + " degrees")

# rotate-gripper-down: rotate the gripper down by a given angle 
def rotate_gripper_down(robot, angle):
    robot.rotate("gripper down by " + str(angle) + " degrees")