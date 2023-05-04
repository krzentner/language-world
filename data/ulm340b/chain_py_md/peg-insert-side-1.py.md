

and use the instructions in `<https://parl.ai/d>`_.

You will not be able to run your program, so if you finish early, you can
just submit your work.


@example

    def peg_insert_side(robot):
        # Steps:
        #  1. Put gripper above the peg
        #  2. Drop gripper around the peg
        #  3. Put gripper above the hole, gripping the peg
        #  4. Slide the peg into the hole
        # We don't want to bump the peg while trying to grab it.
        # So, let's move the gripper above it first.
        if check("the robot's gripper is not above the peg"):
            robot.place("gripper above peg")
        # Now the gripper should be roughly above the peg.
        # It should be safe to grab it.
        if check("the robot's gripper is not around the peg and the robot's gripper is open"):
            robot.drop("gripper around the peg")
        # Now that we have the peg in the gripper, move the gripper so that it is
        # above the hole.
        # If the gripper is not near the hole, move it closer to the hole.
        if check("the robot's gripper is not near the hole"):
            robot.place("gripper above hole")
        # Once the gripper is near the hole, try to move the peg into the hole.
        if check("the robot's gripper is above the hole"):
            robot.slide("peg into hole")

# /
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around the peg
    #  3. Put gripper above the hole, gripping the peg
    #  4. Slide the peg into the hole
    # We don't want to bump the peg while trying to grab it.
    # So, let's move the gripper above it first.
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    # Now the gripper should be roughly above the peg.
    # It should be safe to grab it.
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.drop("gripper around the