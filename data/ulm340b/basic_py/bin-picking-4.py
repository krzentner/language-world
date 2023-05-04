
    if check("the robot's gripper is not above cube and the robot's gripper is not vertically aligned with the cube"):
        robot.put("the gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not near cube"):
        robot.push("the gripper into cube")
    if check("the robot's gripper is near cube and the robot's gripper is not around cube"):
        robot.put("gripper around cube")
    if check("the robot's gripper is around cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is vertically aligned with the goal"):
        robot.place("cube into goal")
    if check("the robot's gripper is not open"):
        robot.open("gripper")

# bin-picking-side: pick up the cube from the side and place it in the target bin
def bin_picking_side(robot):
    if check("the robot's gripper is not above cube and the robot's gripper is not vertically aligned with the cube"):
        robot.put("the gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not near cube"):
        robot.push("the gripper into cube")
    if check("the robot's gripper is near cube and the robot's gripper is not around cube"):
        robot.put("gripper around cube")
    if check("the robot's gripper is around cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is horizontally aligned with goal"):
        robot.place("cube into goal")
    if check("the robot's gripper is not open"):
        robot.open("gripper")

# pick-place-side: pick up the puck and hold it from the side at the target location
def pick_place_side(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near