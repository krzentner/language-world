
    if check("the robot's gripper is not near puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.grab("the puck")
    if check("the robot's gripper is near the puck and the puck is above the robot's gripper"):
        robot.place("the puck at the goal")

# insert: pick up the peg and insert it into the hole
def insert(robot):
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# pick-place-wall: pick up the puck and place it on the wall
def pick_place_wall(robot):
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.move("gripper above puck")
    if check("the robot's gripper is near puck"):
        robot.grab("puck")
    if check("the robot's gripper is forward aligned with puck and puck is not aligned with wall"):
        robot.move("puck to wall")
    if check("the robot's gripper is forward aligned with puck and puck is aligned with wall"):
        robot.place("puck on wall")

# pick-place-inside-wall: pick up the puck and place it inside the wall
def pick_place_inside_wall(robot):
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.move("gripper above puck")
    if check("the robot's gripper is near puck"):
        robot.grab("puck")
    if check("the robot's gripper is forward aligned with puck and puck is not aligned with wall"):
        robot.move("puck to wall")
    if check("the robot's gripper is forward aligned with puck and