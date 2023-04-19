# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    if check("the robot's gripper is not vertically aligned with the hole"):
        robot.put("gripper above hole")
    if check("the robot's gripper is aligned with the hole"):
        robot.push("gripper into hole")
    if check("the robot's gripper is around the peg"):
        robot.lift("peg out of hole")
    if check("the robot's gripper is not above the target location"):
        robot.move("gripper to target location")
    if check("the robot's gripper is above the target location"):
        robot.place("peg at target location")