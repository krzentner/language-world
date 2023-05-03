# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("the peg is not within the gripper and the peg is not vertically aligned with the hole"):
        robot.move("gripper to the hole")
    if check("the robot's gripper is vertically aligned with the peg and the gripper is not around the peg"):
        robot.grab("peg")
    if check("the robot's gripper is around the peg and the peg is not vertically aligned with the target location"):
        robot.move("gripper to the target")
    if check("the robot's gripper is vertically aligned with the target location"):
        robot.place("peg at target")