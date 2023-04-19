# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Detect the wall
    #  4. Move the gripper over the wall
    #  5. Slide the puck to the goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is not around the puck, move it there and close the
    # gripper.
    if check("the robot's gripper is around the puck and the robot's gripper is not close"):
        robot.move_gripper("above the puck", close_gripper=True)
    # Detect the wall and move the gripper over it.
    if check("the robot has not detected the wall"):
        robot.detect_wall()
        return
    elif check("the robot's gripper is not over the wall"):
        robot.move_gripper("over the wall")
    # Slide the puck to the goal.
    if check("the robot's gripper is over the wall and not above the goal"):
        robot.move_gripper("above the goal")