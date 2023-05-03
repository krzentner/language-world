# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the hole
    #  2. Slide gripper down into the hole until it touches the peg
    #  3. Grab the peg by closing the gripper around it
    #  4. Lift the peg out of the hole and move it to the target location
    # First, put the gripper above the hole, lining it up with the peg.
    if check("the robot's gripper is not vertically aligned with the hole"):
        robot.put("gripper above hole")
    # Once the gripper is above the hole, we can slide it down into the hole until it touches the peg.
    if check("the robot's gripper is above the hole and the robot's gripper is not touching the peg"):
        robot.slide("gripper down into the hole")
    # If the gripper is touching the peg, we can grab it by closing the gripper around it.
    if check("the robot's gripper is touching the peg"):
        robot.close("gripper around peg")
    # With the peg in the gripper, we can lift it out of the hole and move it to the target location.
    if check("the robot's gripper has the peg and is above the target location"):
        robot.place("peg at the goal")