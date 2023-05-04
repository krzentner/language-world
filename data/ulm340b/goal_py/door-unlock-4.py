
    # Steps:
    #  1. Put gripper around door dial
    #  2. Turn the door dial
    # Line up the robot's gripper around the door dial.
    if check("the robot's gripper is not forward aligned with door dial"):
        robot.move_gripper("around the door dial")
    # If the robot's gripper is lined up with the door dial, we can turn the
    # door dial.
    if check("the robot's gripper is not near door dial"):
        robot.move_gripper("left of the door dial")

# sweep-into: push the puck into the drawer, then close it
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck into drawer
    #  4. Close the drawer
    # Sweep the puck into the drawer.  This is basically the same as pushing,
    # except the goal location is now inside the drawer.
    if check("the robot's gripper is not near puck and the robot's gripper is vertically aligned with puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    if check("the robot's gripper is not near puck"):
        robot.move_gripper("inside the drawer")

# door-close: close the door
def door_close(robot):
    # Steps:
    #  1. Push the door closed
    # Close the door by pushing it.  Don't push too fast, though, because the
    # door handle makes a wide loop.
    if check("the robot's gripper is not forward aligned with the door handle"):
        robot.move_gripper("forward aligned with the door handle")

# peg-unstack-side: grab the top peg from a stack and insert it into the hole
def peg_unstack_side(robot):
    # Steps:
    #  1. Put gripper above top peg
    #  2. Grab the top peg with the gripper
    #  3. Line the top peg up with the hole
   