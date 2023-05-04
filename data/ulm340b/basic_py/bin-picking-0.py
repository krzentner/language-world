
    if check("the robot's gripper is not near cube"):
        robot.grab("the cube")
    if check("the robot's gripper is around the cube and the cube is not near bin"):
        robot.reach("to bin")
    if check("the robot's gripper is near bin"):
        robot.put("the cube in the bin")
    if check("the robot's gripper is in front of bin and the cube is not in bin"):
        robot.drop("the cube in the bin")

# pick-place-wall: pick up the cube and place it at the target location next to the wall
def pick_place_wall(robot):
    if check("the robot's gripper is not near cube"):
        robot.grab("the cube")
    if check("the robot's gripper is around the cube and the cube is not near goal"):
        robot.reach("to goal")
    if check("the robot's gripper is near goal"):
        robot.place("the cube at the goal")
    if check("the robot's gripper is in front of goal and the cube is not in goal"):
        robot.drop("the cube at the goal")

# place-in-box: drop the cube into the target container
def place_in_box(robot):
    if check("the robot's gripper is not near cube"):
        robot.grab("the cube")
    if check("the robot's gripper is around the cube and the cube is not near bin"):
        robot.reach("to bin")
    if check("the robot's gripper is near bin"):
        robot.put("the cube in the bin")
    if check("the robot's gripper is in front of bin and the cube is not in bin"):
        robot.drop("the cube in the bin")

# pick-out-of-box: pick the cube up out of the container
def pick_out_of_box(robot):
    if check("the robot's gripper is not near cube"):
        robot.grab("the cube")
    if check("the robot's gripper is around the cube and the cube is not near goal"):
        robot.reach("to goal")
    if check("the robot's gripper is near goal"):
        robot.place("the cube at the goal")
    if check("the robot's gripper is in front of goal and the