
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is not near the goal"):
        robot.slide("the puck to the goal")

# pick-place-wall: pick up the puck and hold it at the target location with a small wall in the way
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed and the robot's gripper is vertically aligned with the puck"):
        robot.place("puck at goal")
    if check("the robot's gripper is above puck and the robot's gripper is closed and the robot's gripper is not vertically aligned with the puck"):
        robot.drop("gripper over puck")
    if check("the robot's gripper is near the puck"):
        robot.align("gripper to goal")
    if check("the robot's gripper is above the puck"):
        robot.place("puck at goal")

# pick-place-wall-v2: pick up the puck and hold it at the target location with a small wall in the way
def pick_place_wall_v2(robot):
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper