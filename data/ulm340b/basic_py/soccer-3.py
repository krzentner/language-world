
    if check("the robot's gripper is not above the soccer ball"):
        robot.put("gripper above soccer ball")
    if check("the robot's gripper is vertically aligned with the soccer ball and the robot's gripper is not near the soccer ball"):
        robot.push("gripper into soccer ball")
    if check("the robot's gripper is near the soccer ball and the soccer ball is below the robot's gripper"):
        robot.slide("soccer ball to goal")

# pick-place-wall: pick up the puck and hold it at the target location on the wall
def pick_place_wall(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck"):
        robot.place("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# turn-dial: turn the dial to the target direction
def turn_dial(robot):
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper closer to dial")
    if check("the robot's gripper is near the dial and the robot's gripper is not in front of the dial"):
        robot.move("gripper in front of dial")
    if check("the robot's gripper is in front of the dial"):
        robot.turn("the dial left")

# pick-place-side: pick up the puck from the side and hold it at the target location
def pick_place_side(robot):
    if check("the robot's gripper is not near the puck and the robot's gripper is not open"):
        robot.put("gripper near puck")
    if check("the robot's gripper is near the puck and the robot's gripper is not open"):
        robot.open("gripper")
    if check("the robot's gripper is near the puck"):
        robot.close("gripper around puck")
    if check("the robot's gripper is near the puck and the robot's gripper is around puck"):
        robot.place("