
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Close gripper around mug hancle
    #  4. Grab mug handle with gripper
    #  5. Place mug at goal
    # First, put the gripper mostly above the mug handle.
    if check("the robot's gripper is not almost vertically aligned with mug handle"):
        robot.put("gripper above mug handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the mug handle and the robot's gripper is open"):
        robot.grab("gripper around mug handle")
    # Now that the gripper is around the mug handle, grab the mug handle snugly.
    if check("the robot's gripper is around mug handle and the gripper is not closed"):
        robot.close("gripper around mug handle")
    # Now that the gripper is around the mug handle, we can push the mug to the
    # goal.
    if check("the robot's gripper is around mug handle and the gripper is closed"):
        robot.place("mug at goal")