
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the window handle is left of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper left.
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    # If the robot's gripper is starting to be behind the window handle, push
    # harder.
    if check("the robot's gripper is behind the window handle"):
        robot.push("window left harder")

# peg-insert-topdown: grab the peg and insert it into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Insert the peg into the hole from above
    # The robot's gripper is parallel to the table, so it's easiest to just drop
    # the gripper down on top of the peg and then move it up.
    # If the robot's gripper is not aligned with the peg as seen from above,
    # align it.
    if check("the robot's gripper is not above peg and the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # As long as the gripper is aligned with the peg but not around it, close the
    # gripper around the peg.
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around the peg"):
        robot.put("gripper around peg")
    # If the peg is lined up with the hole, insert it.
    if check("the robot's gripper is