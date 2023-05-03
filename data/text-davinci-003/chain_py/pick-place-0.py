
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with the gripper
    #  3. Reach to target
    #  4. Place the puck at the target
    # To pick up the puck, we'll need to put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck and the robot's gripper is below the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is above the puck, we can grab it.
    if check("the robot's gripper is above the puck and the robot's gripper is open"): 
        robot.grab("the puck")
    # If the robot is holding the puck, reach to the target location.
    if check("the robot's gripper is around the puck"):
        robot.reach("to target")
    # Once the gripper is near the target location, we can release the puck and
    # move away from it.
    if check("the robot's gripper is near the target location"):
        robot.place("the puck on the target location")