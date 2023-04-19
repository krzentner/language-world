# push-back: slide the puck backwards to the target location
# def push_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck backwards to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper backwards.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it backwards.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it backwards to the target location.
    # Move the gripper backwards while sliding the puck to the target location.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide_backwards("the puck to the goal")