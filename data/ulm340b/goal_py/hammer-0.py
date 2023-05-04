
    # Steps:
    #  1. Put gripper above hammer
    #  2. Lift the hammer
    #  3. Put hammer near nail
    #  4. Hit the nail with the hammer
    # First, move the robot gripper roughly above the hammer.
    if check("the robot's gripper is not vertically aligned with hammer"):
        robot.move_gripper("vertically aligned with hammer")
    # Once the robot's gripper is above the hammer, close the gripper around the
    # hammer.
    if check("the robot's gripper is vertically aligned with hammer and the robot's gripper is not around hammer"):
        robot.move_gripper("around hammer", close_gripper=True)
    # If the hammer is above the nail, drop it.
    if check("the robot's gripper is above the hammer and the hammer is above the nail"):
        robot.move_gripper("around the hammer", open_gripper=True)
    # If the robot's gripper is above the hammer, and the hammer is above the
    # nail, drop the hammer onto the nail.
    # Because the hammer is bigger than the nail, we can just check if it is in
    # front of it rather than around it.
    if check("the hammer is below the robot's gripper and hammer is horizontally aligned with nail"):
        robot.move_gripper("above the hammer", close_gripper=True)

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Push down on the peg to insert it into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # If the peg is below the gripper as seen from above, it is likely held by
    # the gripper.
    # Because the peg is a long object, check if the gripper is forward aligned
    # with it instead of around it.
    if check("