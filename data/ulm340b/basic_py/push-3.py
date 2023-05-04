
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above puck"):
        robot.move("puck to goal")

# push-back: slide the puck from the front to the back
def push_back(robot):
    if check("the robot's gripper is not near puck and the robot's gripper is below puck"):
        robot.put("gripper near puck")
    if check("the robot's gripper is not forward aligned with puck"):
        robot.push("puck right")
    if check("the robot's gripper is forward aligned with puck"):
        robot.push("puck left")

# push-forward: slide the puck from the back to the front
def push_forward(robot):
    if check("the robot's gripper is not near puck and the robot's gripper is above puck"):
        robot.put("gripper near puck")
    if check("the robot's gripper is not forward aligned with puck"):
        robot.push("puck left")
    if check("the robot's gripper is forward aligned with puck"):
        robot.push("puck right")

# push-left: slide the puck from the right to the left
def push_left(robot):
    if check("the robot's gripper is not near puck and the robot's gripper is to the right of puck"):
        robot.put("gripper near puck")
    if check("the robot's gripper is not forward aligned with puck"):
        robot.push("puck away")
    if check("the robot's gripper is forward aligned with puck"):
        robot.push("puck towards")

# push-left-side: slide the puck from the right to the left by standing to the left of the puck
def push_left_side(robot):
    if check("the robot's gripper is not near puck and the robot's gripper is to the right of puck"):
        robot.put("gripper near puck")
    if check("the robot's gripper is not aligned with puck and the robot's gripper is not left of puck"):
        robot.move("gripper to left of puck")
    if check("the robot's gripper is to the left of puck"):
        robot.move("puck left")

# push-right: slide