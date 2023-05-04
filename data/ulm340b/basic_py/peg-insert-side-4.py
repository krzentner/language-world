
    if check("the robot's gripper is not above peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is above peg and the robot's gripper is not around peg"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.rotate("to align with hole")
    if check("the robot's gripper is forward aligned with hole"):
        robot.push("peg into hole")

# peg-unstack-side: unstack the peg and place it at the target location
def peg_unstack_side(robot):
    if check("the robot's gripper is not vertically aligned with peg and the robot's gripper is not around peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is above peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.move("peg off the peg")
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.put("peg at goal")

# pick-place-wall: pick up the puck and hold it at the target location on the wall
def pick_place_wall(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# latch-door-v1-side: open the door by sliding the latch from