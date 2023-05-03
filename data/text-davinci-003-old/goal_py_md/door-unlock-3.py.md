

Steps:
  1. Put gripper directly above the dial
  2. Drop gripper to the left of the dial
  3. Turn the dial clockwise
  4. Stop turning dial when it stops of its own accord 

# door-unlock: turn the dial on the door
# def door_unlock(robot):
    # Steps:
    #  1. Put gripper directly above the dial
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")
    #  2. Drop gripper to the left of the dial
    if check("the robot's gripper is not left of the dial"):
        robot.move_gripper("left of the dial", close_gripper=True)
    #  3. Turn the dial clockwise
    if check("the robot's gripper is left of the dial"):
        robot.move_gripper("right")
    #  4. Stop turning dial when it stops of its own accord
    if check("the dial is turning on its own accord"):
        robot.stop_gripper()