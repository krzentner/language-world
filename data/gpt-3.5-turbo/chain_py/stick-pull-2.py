# Steps:
    #  1. Put gripper above stick
    #  2. Grab stick with gripper
    #  3. Put gripper above thermos lid
    #  4. Hook stick around thermos lid
    #  5. Pull thermos to goal
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above stick"):
        robot.move("gripper above stick")
    # If the gripper isn't around the stick, grab the stick.
    if check("the robot's gripper is not around stick" and "the stick is not in robot's gripper"):
        robot.grab("stick")
    # If the gripper is above the stick, put the gripper above the thermos lid.
    if check("the robot's gripper is above stick and the robot's gripper is not above thermos lid"):
        robot.move("gripper above thermos lid")
    # If the gripper is above the thermos lid, hook the stick around it.
    if check("the robot's gripper is above thermos lid and the stick is hooked around lid"):
        robot.hook("stick around lid")
    # If the stick is hooked around the lid, pull the thermos to the target location.
    if check("the stick is hooked around lid"):
        robot.pull("thermos to goal")