
    if check("the robot's gripper is not above the wall"):
        robot.place("gripper over wall")
    if check("the robot's gripper is above the wall"):
        robot.place("gripper over goal")

# pick-place-wall: pick the puck up and place it at the target location with a short wall in the way
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.put("the gripper over the puck")
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.drop("the gripper around the puck")
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.close("the gripper around the puck")
    if check("the robot's gripper is above the puck and the robot's gripper is closed"):
        robot.place("the puck over the goal")

# pick-place-wall-shelf: pick the puck up and place it on the top shelf at the target location with a short wall in the way
def pick_place_wall_shelf(robot):
    if check("the robot's gripper is not above the puck"):
        robot.put("the gripper over the puck")
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.drop("the gripper around the puck")
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.close("the gripper around the puck")
    if check("the robot's gripper is above the puck and the robot's gripper is closed"):
        robot.lift("the puck to the shelf")

# pick-place-wall-bin: pick the puck up and place it in the box at the target location with a short wall in the way
def pick_place_wall_bin(robot):
    if check("the robot's gripper is not above the puck"):
        robot.put("the gripper over the puck")
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.drop("the gripper around the puck")
    if check("the robot's gripper is near the puck and the robot's gripper is open