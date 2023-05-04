

"""

def push_back(robot):
    # Steps:
    #  1. Put gripper behind puck
    #  2. Push gripper into puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck is not below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not behind puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not behind puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # If the gripper is around the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is behind puck and the puck is below the robot's gripper"):
        robot.move_gripper("behind the target location")

# push-back: slide the puck backwards to the target location
def push_back(robot):
    # Steps:
    #  1. Put gripper behind puck
    #  2. Push gripper into puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck is not below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not behind puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot