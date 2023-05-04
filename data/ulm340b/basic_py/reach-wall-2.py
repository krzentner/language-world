
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")

# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.close("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is closed"):
        robot.hold("puck at goal")

# pull: pull the puck towards the robot
def pull(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.place("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.pull("the puck towards the robot")

# window-close-wall: slide the window closed to the right with a short wall in the way
def window_close_wall(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

# peg-insert-side-wall: grab the peg and insert it into the hole from the side with a short wall in the way
def peg_insert_side_wall(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is