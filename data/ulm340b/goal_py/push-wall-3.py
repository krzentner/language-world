
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    #  4. Put gripper in front of the wall
    #  5. Slide wall to goal
    #  6. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("above the target location")
    # Move the gripper to the wall.
    if check("the gripper is not near wall and the puck is near target"):
        robot.move_gripper("vertically aligned with wall")
    # Push the gripper into the wall.
    if check("the gripper is above wall and the gripper is not near wall"):
        robot.move_gripper("near wall", close_gripper=True)
    # Slide the wall to the target location.
    if check("the wall is not near target"):
        robot.move_gripper("almost vertically aligned with wall")
    # Re-slide the puck to the target location.
    if check("the wall is near target and the puck is not near target"):
        robot.move_gripper("above the puck")
[eod] [code]from django import forms
