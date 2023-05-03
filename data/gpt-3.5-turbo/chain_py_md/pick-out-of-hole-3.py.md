# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Push the peg up out of the hole
    #  3. Grab the peg with the gripper
    #  4. Move the peg to the goal
    # First, put the gripper above the peg in the hole.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg is still in the hole, we need to push it up to grab it.
    if check("peg is not above the hole"):
        robot.push("peg up out of hole")
    # Once the peg is above the hole, grab it.
    if check("peg is above the hole and the robot's gripper is open"):
        robot.grab("peg")
    # If the gripper is around the peg, move it to the goal location.
    if check("the robot's gripper is around the peg"):
        robot.place("peg at goal")