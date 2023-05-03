# Steps:
    #  1. Put gripper above the center of the drawer
    #  2. Drop gripper inside the drawer
    #  3. Push the drawer closed
    # We need to first put the gripper above the center of the drawer, so that we
    # can grab it without risk of pushing the drawer open instead of closed.
    if check("the robot's gripper is not above the center of the drawer and the robot's gripper is not vertically aligned with the drawer handle"):
        robot.put("gripper above the center of the drawer")
    # Once the gripper is above the center of the drawer, we can lower it inside
    # the drawer to grab it.
    if check("the robot's gripper is above the center of the drawer and the robot's gripper is not inside the drawer"):
        robot.drop("gripper inside the drawer")
    # With the gripper inside the drawer and around it, we can now push the door
    # closed.
    if check("the robot's gripper is around the drawer and inside it"):
        robot.push("drawer closed")