# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal while avoiding the wall
    # The robot needs to push the puck to the target location while avoiding a small wall.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location while avoiding the wall.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        # Check if the puck is aligned with the wall.
        if check("the wall is in the way and the puck is aligned with the wall"):
            # Move the gripper to the side of the wall while keeping the same height.
            robot.move_gripper("left of the wall", y_offset=0)
        # Once the gripper is clear of the wall, move it towards the target location.
        if check("the gripper is not yet above the target location"):
            robot.move_gripper("above the target location")