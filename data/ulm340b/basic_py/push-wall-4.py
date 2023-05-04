
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# stack: slide the puck to the target location and then hold it in place
def stack(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")
    if check("the robot's gripper is above the puck"):
        robot.drop("the gripper on the puck")
    if check("the robot's gripper is not near the puck"):
        robot.grab("the puck")

# pick-stack: pick up the puck and hold it at the target location
def pick_stack(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")
    if check("the robot's gripper is not below puck"):
        robot.slide("the puck to the goal")

# pick-place-wall: pick up the puck and hold it at the target location with a small wall in the way
def pick_place_wall(robot):
    if check("the robot