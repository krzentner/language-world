# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the peg hole
    #  2. Lower gripper until it is around peg
    #  3. Lift up the peg out of the hole
    #  4. Move peg to goal
    # Put the gripper roughly above the peg hole so that it is not close to the peg.
    if check("the robot's gripper is not above the peg hole"):
        robot.place("gripper above peg hole")
    # Once the gripper is roughly above the peg hole, lower it until it is around the peg.
    if check("the robot's gripper is above the peg hole and the robot's gripper is not around the peg"):
        robot.drop("gripper around peg")
    # Once the gripper is around the peg, lift up the peg out of the hole.
    if check("the robot's gripper is around peg and the robot's gripper is not lifted up"):
        robot.lift("peg out of hole")
    # Once the peg is lifted up, move it to the goal location.
    if check("the peg is lifted up"):
        robot.place("peg at goal")