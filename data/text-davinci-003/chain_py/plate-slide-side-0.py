
    # Steps:
    #  1. Put gripper above plate handle
    #  2. Drop gripper around plate handle
    #  3. Slice plate to goal
    # First, put the gripper above the plate handle so we can grab it.
    if check("the robot's gripper is not vertically aligned with the plate handle"):
        robot.put("gripper above plate handle")
    # If the gripper is partially around the plate handle, close the gripper.
    if check("the robot's gripper is vertically aligned with the plate handle and the robot's gripper is not around plate handle"):
        robot.put("gripper around plate handle")
    # If the plate is lined up with the robot's gripper, we can slide the plate.
    
    if check("the robot's gripper is along plate handle"):
        robot.slide("plate to goal")