

Then, write a program to perform the task `push-back`.

# push-back: slide the puck backwards to the target location
def push_back(robot):
    # Steps:
    #  1. Put gripper below puck
    #  2. Push gripper into the back of puck
    #  3. Slide puck to goal
    # Move the robot's gripper below the puck.
    if check("the robot's gripper is not below puck"):
        robot.move_gripper("below the puck")
    # If the gripper is not near the puck, push the gripper into the back of the
    # puck.
    if check("the robot's gripper is not near puck"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the puck is near the gripper and the puck is below the gripper as seen
    # from the back, push the puck to the target location.
    if check("the robot's gripper is below the puck and the robot's gripper is near the puck"):
        robot.move_gripper("below the target location")