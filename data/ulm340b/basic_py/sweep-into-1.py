
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.grab("cube")
    if check("the robot's gripper is almost horizontally aligned with cube"):
        robot.move("cube to goal")
    if check("the robot's gripper is almost horizontally aligned with cube and the robot's gripper is forward aligned with cube"):
        robot.drop("cube at goal")

# sweep-onto: sweep the cube on top of the target puck
def sweep_onto(robot):
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.grab("cube")
    if check("the robot's gripper is almost horizontally aligned with cube"):
        robot.move("cube above puck")
    if check("the robot's gripper is almost horizontally aligned with cube and the robot's gripper is forward aligned with cube"):
        robot.drop("cube onto puck")

# pick-place-side: pick up the cube and place it at the target location
def pick_place_side(robot):
    if check("the robot's gripper is not vertically aligned with cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.put("gripper around cube")
    if check("the robot's gripper is around cube"):
        robot.lift("cube")
    if check("the robot's gripper is above cube"):
        robot.move("cube to goal")
    if check("the robot's gripper is vertically aligned with cube"):
        robot.drop("cube at goal")

# stack: stack the cube on top of the target
def stack(robot):
    if check("the robot's gripper is not vertically aligned with cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.put("gripper around cube")
    if check("the robot's gripper is around cube"):
        robot.lift("cube")
    if check("the robot's gripper is above cube"):
        robot.move("cube above target")
    if check("the robot's gripper is vertically aligned with cube"):
        robot.drop("cube