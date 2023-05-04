
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull the handle up
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the handle becomes left of the gripper, go back to putting the gripper
    # above the handle.
    # Because the handle is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the handle is not left of the robot's gripper and the handle is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the handle")
    # Once the gripper is lined up above the handle and the handle isn't up, pull
    # the handle up.
    if check("the handle is down and the handle is above the robot's gripper and the robot's gripper is above the handle"):
        robot.move_gripper("above the handle")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Insert the peg into the hole from the top
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("the peg is not left of the robot's gripper and the peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg and