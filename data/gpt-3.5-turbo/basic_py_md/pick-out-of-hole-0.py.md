# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    if check("the robot's gripper is not vertically aligned with the peg in the hole"):
        robot.put("gripper above peg in hole")
    if check("the robot's gripper is not around peg in hole and the robot's gripper is open"):
        robot.drop("gripper around peg in hole")
    if check("the robot's gripper is around peg in hole and the robot's gripper is closed"):
        robot.lift("peg out of hole")
    if check("the robot's gripper is near the goal location and the robot's gripper is closed"):
        robot.align("peg to goal location")
    if check("the robot's gripper is above the goal location and the robot's gripper is closed"):
        robot.place("peg at goal location")