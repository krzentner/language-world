
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.grab("the puck")
    if check("the robot's gripper is forward aligned with the puck"):
        robot.put("the puck above the target")
    if check("the robot's gripper is near the target and the puck is left of the robot's gripper"):
        robot.drop("the puck")

# push-retract: slide the puck to the target location and return
def push_retract(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")
    if check("the robot's gripper is near the goal and the puck is not below the robot's gripper"):
        robot.retract("to the puck")

# pick-place-retract: pick up the puck and hold it at the target location then return
def pick_place_retract(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.grab("the puck")
    if check("the robot's gripper is forward aligned with the puck"):
        robot.put("the puck above the target")
    if check("the robot's gripper is near the target and the puck is left of the robot's gripper"):
        robot.drop("the puck")
    if check("the robot's gripper is near the target and the puck is not left of the robot's gripper"):
        robot.retract("to the puck")

