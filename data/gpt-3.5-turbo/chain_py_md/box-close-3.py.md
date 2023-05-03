# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Put gripper above the lid handle
    #  2. Drop gripper around the lid handle
    #  3. Close gripper around lid handle
    #  4. Lift the lid off the box
    #  5. Move the lid to the top of the box
    #  6. Replace the lid on the box
    # First, put the gripper above the lid handle so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the lid handle"):
        robot.place("gripper above lid handle")
    # If the gripper isn't around the lid handle, put it around the lid handle.
    if check("the robot's gripper is not around lid handle and the robot's gripper is open"):
        robot.drop("gripper around lid handle")
    # If the gripper is near the lid handle and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near lid handle and the robot's gripper is open"):
        robot.close("gripper around lid handle")
    # We closed the gripper, and the lid handle is still near the gripper, so maybe we
    # grabbed it.
    # Now lift the lid off the box
    if check("the robot's gripper is around the lid handle and lid is still on the box"):
        robot.lift("the lid off the box")
    # Move the lid to the top of the box
    if check("the robot's gripper is holding the lid and the lid is not at the top of the box"):
        robot.move("the lid to the top of the box")
    # Finally, replace the lid on the box
    if check("the lid is at the top of the box"):
        robot.replace("the lid on the box")