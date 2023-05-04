
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# peg-insert-side-only: insert the peg into the hole from the side (no grabbing)
def peg_insert_side_only(robot):
    if check("peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# pick: pick up the puck from the table
def pick(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around puck"):
        robot.move("puck to goal")

# pick-place-wall: pick up the puck from the table with a short wall in the way
def pick_place_wall(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around puck"):
        robot.move("puck to goal")


# place: drop the puck at the target location
def place(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is closed"):
        robot.open("gripper around puck")
    if check("the robot'