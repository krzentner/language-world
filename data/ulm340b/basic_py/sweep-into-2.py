
    if check("the robot's gripper is not vertically aligned with cube and the robot's gripper is not open"):
        robot.put("gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube"):
        robot.place("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is not closed"):
        robot.close("the gripper around cube")
    if check("the robot's gripper is forward aligned with cube"):
        robot.move("cube to goal")

# pick-place-wall: pick up the puck and hold it on the target location on the wall
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck on wall")

# pick-out: pick up the puck out of the hole
def pick_out(robot):
    if check("the robot's gripper is not vertically aligned with puck and the robot's gripper is not open"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with puck"):
        robot.place("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is not closed"):
        robot.close("the gripper around puck")
    if check("the robot's gripper is forward aligned with puck"):
        robot.move("puck to goal")

# turn-switch-down: turn the switch down
def turn_switch_down(robot):
    if check("the robot's gripper is not right of the switch"):
        robot.move("gripper to right of switch")
    if check("the switch is not below the robot's gripper"):
        robot.drop("gripper below switch")
    if check("the robot's gripper is near switch"):
        robot.