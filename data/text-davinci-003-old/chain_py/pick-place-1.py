
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above the puck.
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    # If the gripper isn't already around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # If we can close the gripper around the puck, try to move the puck to the
    # goal.
    if check("the robot's gripper is closed around the puck"):
        robot.move("puck to goal")

# push-through-opening: push the puck through the opening
# def push_through_opening(robot):
    # Steps:
    #  1. Put gripper above puck  
    #  2. Push gripper into top of puck
    #  3. Push the puck into the opening
    # First, put the gripper roughly above the puck.
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    # If the gripper isn't already around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck, we can trap the puck by pushing down on
    # it from above.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.push("the gripper into the puck")
    # Now that the puck is trapped, we can push it into the opening.
    # We need to keep pushing until the puck passes through the opening.
    if check("the puck is not through the opening"):
        robot.push("the puck through the opening")