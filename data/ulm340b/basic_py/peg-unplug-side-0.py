
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is forward aligned with the robot's gripper and the peg is not above robot's gripper"):
        robot.put("gripper under peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not left of the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not left of the robot's gripper"):
        robot.remove("peg from hole")

# grasp-screw-vertical: pick up the screw in vertical orientation
def grasp_screw_vertical(robot):
    if check("the robot's gripper is not above the screw"):
        robot.move("gripper above screw")
    if check("the robot's gripper is above the screw and the robot's gripper is not around the screw"):
        robot.place("gripper around screw")
    if check("the robot's gripper is around the screw and the screw is below the robot's gripper"):
        robot.lift("screw")

# grasp-screw-horizontal: pick up the screw in horizontal orientation
def grasp_screw_horizontal(robot):
    if check("the robot's gripper is not above the screw"):
        robot.put("gripper above screw")
    if check("the robot's gripper is above the screw and the robot's gripper is not around the screw"):
        robot.put("gripper around screw")
    if check("the robot's gripper is around the screw and the screw is below the robot's gripper"):
        robot.lift("screw")

# insert-screw-vertical: insert the screw into the hole in vertical orientation
def insert_screw_vertical(robot):
    if check("the robot's gripper is not above the hole"):
        robot.move("gripper above hole")
    if check("the robot's gripper is above the hole and the screw is below the robot's gripper"):
        robot.lower("screw into hole")

# insert-screw-horizontal: insert the screw into the hole in horizontal orientation
def insert_screw_horizontal(robot):
    if check("the robot's gripper is not above the hole"):
        robot.move("gripper above hole")
    if check("