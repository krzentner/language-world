# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Move the puck until it hits the wall
    #  4. Move the gripper to the other side of the wall
    #  5. Push the puck to the target location
    # The robot can slide the puck by trapping it by pushing down on it from above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # move it towards the wall.
    # Close the gripper to make sure we keep control of the puck.
    # Keep moving the puck until it hits the wall.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        while not check("the puck has hit the wall"):
            robot.slide("the puck to the wall")
    # When the puck hits the wall, move the gripper to the other side of the wall.
    # Because the robot has a single gripper, we need to move the robot itself to the other side of the wall.
    if check("the puck has hit the wall"):
        robot.move("the robot to the other side of the wall")
    # When the robot is on the other side of the wall, move the gripper above the puck again to slide it further.
    if check("the robot is on the other side of the wall"):
        if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
            robot.put("the gripper above the puck")
        # If the gripper is aligned with the puck but not near it, move the gripper
        # down to the puck to slide it.
        if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
            robot.push("the gripper into the puck")
        # If the gripper is near the puck, we've probably trapped the puck and can
        # slide it the rest of the way to the target location.
        if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
            robot.slide("the puck to the goal")