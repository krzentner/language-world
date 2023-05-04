
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube"):
        robot.grab("cube")
    if check("the robot's gripper is near the cube"):
        robot.sweep("cube into goal")

# sweep-into-goal-side: grab the cube and move it to the target location from the side
def sweep_into_goal_side(robot):
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is near the cube and cube is not aligned to goal and the robot's gripper is closed"):
        robot.put("gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube"):
        robot.grab("cube")
    if check("the robot's gripper is near the cube"):
        robot.sweep("cube into goal")

# sweep-into-goal-side-v2: grab the cube and move it to the target location from the side
def sweep_into_goal_side_v2(robot):
    if check("the robot's gripper is not near cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is near the cube and cube is not aligned to goal"):
        robot.put("gripper above cube")
    if check("the robot's gripper is above the cube"):
        robot.grab("cube")
    if check("the robot's gripper is near the cube and the cube is above the goal"):
        robot.sweep("cube into goal")

# pick-place-overhand: pick up the puck and place it at the target location from above
def pick_place_overhand(robot):
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is closed