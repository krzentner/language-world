

Steps:
  1. Put gripper above lid
  2. Grab lid with gripper
  3. Place lid onto box
  4. Push lid on to box

# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Put gripper above lid
    #  2. Grab lid with gripper
    #  3. Place lid onto box
    #  4. Push lid on to box
    # First, put the gripper above the lid.
    if check("the robot's gripper is not above the lid"):
        robot.put("gripper above lid")
    # Then, grab the lid with the gripper.
    if check("the robot's gripper is above the lid and the robot's gripper is not around the lid"):
        robot.grab("lid")
    # Place the lid onto the box.
    if check("the robot's gripper is around the lid"):
        robot.place("lid on box")
    # Finally, push the lid onto the box to close it.
    if check("the robot's gripper is around the lid"):
        robot.push("lid onto box")