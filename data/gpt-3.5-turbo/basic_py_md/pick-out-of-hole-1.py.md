# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    if check("the robot's gripper is not vertically aligned with the peg in the hole and the robot's gripper is not almost closed"):
        robot.put("gripper above hole")
    if check("the robot's gripper is not around the peg and the robot's gripper is not closed"):
        robot.grab("peg")
    if check("the robot's gripper is around the peg and the peg is not aligned with the hole"):
        robot.align("peg to hole")
    if check("the robot's gripper is around the peg and the peg is aligned with the hole"):
        robot.pull("peg out of hole")
    if check("the robot's gripper is holding the peg and the robot's gripper is not above the target location"):
        robot.put("gripper above target")
    if check("the robot's gripper is holding the peg and the robot's gripper is above the target location and the robot's gripper is not almost closed"):
        robot.move("gripper to target")
    if check("the robot's gripper is holding the peg and the robot's gripper is above the target location and the robot's gripper is almost closed"):
        robot.place("peg at target")