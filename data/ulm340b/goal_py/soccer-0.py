
    # Steps:
    #  1. Put gripper above ball
    #  2. Push gripper into ball
    #  3. Slide ball to goal
    # The robot can move the ball by pushing down on it from above and moving
    # the gripper.
    # If the ball isn't below the gripper as seen from above, move the gripper
    # above the ball.
    if check("the robot's gripper is not above the ball and the robot's gripper is not vertically aligned with the ball"):
        robot.move_gripper("vertically aligned with the ball")
    # If the gripper is above the ball but not near it, move the gripper down
    # to the ball to push it.
    if check("the robot's gripper is vertically aligned with the ball and the robot's gripper is not near the ball"):
        robot.move_gripper("around the ball", close_gripper=True)
    # If the gripper is near the ball, we've probably pushed it and can now
    # slide the ball to the target location.
    # Close the gripper to make sure we keep control of the ball.
    if check("the robot's gripper is near the ball and the ball is below the robot's gripper"):
        robot.move_gripper("around the target location")


def execute(robot, command):
    if command == "peg-insert-side":
        peg_insert_side(robot)
    elif command == "door-close":
        door_close(robot)
    elif command == "window-close":
        window_close(robot)
    elif command == "drawer-open":
        drawer_open(robot)
    elif command == "window-open":
        window_open(robot)
    elif command == "drawer-close":
        drawer_close(robot)
    elif command == "door-open":
        door_open(robot)
    elif command == "button-press":
        button_press(robot)
    elif command == "button-press-topdown":
        button_press_topdown(robot)
    elif command == "reach":
        reach(robot)
    elif command == "pick-place":
        pick_place(robot)
    elif command == "push":
        push(robot)
    elif command == "soccer":
        soccer(robot)
    else:
        print