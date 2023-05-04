
    if check("the robot's gripper is not vertically aligned with soccer ball"):
        robot.put("the gripper above the ball")
    if check("the robot's gripper is not near the soccer ball"):
        robot.move("the robot's gripper forward into the ball")
    if check("the robot's gripper is in front of the ball"):
        robot.push("the ball forward")

# pick-place-wall: pick up the puck and place it on top of the ledge
def pick_place_wall(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is not near the puck"):
        robot.drop("the gripper around the puck")
    if check("the robot's gripper is near the puck"):
        robot.close("the gripper around the puck")
    if check("the puck is in the robot's gripper"):
        robot.raise("the puck to the goal")
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.release("the puck at the goal")

# pick-place-bin: pick up the puck and place it inside the bin
def pick_place_bin(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is not near the puck"):
        robot.drop("the gripper around the puck")
    if check("the robot's gripper is near the puck"):
        robot.close("the gripper around the puck")
    if check("the puck is in the robot's gripper"):
        robot.put("the puck into the bin")
    if check("the puck is vertically aligned with the bin"):
        robot.release("the puck at the goal")

# pick-place-shelf: pick up the puck and place it on the ledge
def pick_place_shelf(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is not near the puck"):
        robot.drop("the gripper around the puck")
    if check("the robot's gripper is near