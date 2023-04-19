
    # Steps:
    #  1. Line up the gripper as viewed from beneath
    #  2. Push the lever up
    # Because this is "pull", we just need to line up the gripper from beneath.
    # Line up the robot's gripper from beneath.
    if check("the robot's gripper is not aligned with lever as viewed from beneath and the robot's gripper is below lever as viewed from beneath"):
        robot.put("gripper beneath lever")
    # Once the gripper is lined up, rotate the lever up, then back down.
    if check("the robot's gripper is aligned with lever"):
        robot.push("up on lever")
        robot.pull("down on lever")