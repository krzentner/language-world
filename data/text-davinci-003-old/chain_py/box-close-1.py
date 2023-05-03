
    # Steps:
    #  1. Put gripper above the box lid
    #  2. Pick up the box lid
    #  3. Place the lid on the box
    # Before picking up the box lid, the robot should roughly position its
    # gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.put("gripper above box lid")
    # If the gripper is mostly above the box lid, there should be no problem
    # picking it up.
    if check("the robot's gripper is above the box lid"):
        robot.pick("up box lid")
    # Once the box lid is picked up, the robot can place it back on the box.
    if check("the robot's gripper is carrying box lid"):
        robot.place("lid back on box")