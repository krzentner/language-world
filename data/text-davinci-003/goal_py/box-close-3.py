
    # Steps:
    #  1. Line up the gripper as viewed from the top
    #  2. Line up the gripper as viewed from in front
    #  3. Push the lid onto the box
    # To close the box, the robot needs to line the lid up from above and from the
    # front before pushing the lid onto the box.
    # Lining up from above
    if check("the robot's gripper is not vertically aligned with lid"):
        robot.move_gripper("vertically aligned with the lid")
    # Lining up from the front
    if check("the robot's gripper is not forward aligned with lid and the lid is below the robot's gripper"):
        robot.move_gripper("forward aligned with the lid")
    # If the gripper is lined up with the lid, it should be in front of the lid.
    # Now, we need to move the gripper down and push the lid onto the box.
    if check("the robot's gripper is forward aligned with the lid"):
        robot.move_gripper("below the lid")
    # Once the gripper is below the lid, we can push the lid onto the box.
    if check("the robot's gripper is below the lid"):