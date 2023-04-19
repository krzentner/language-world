# push: slide the puck to the target location
# def push(robot):
# Steps:
#  1. Put gripper above puck
#  2. Push gripper into top of puck
#  3. Slide puck to goal

# The robot can slide the puck by trapping it by pushing down on it from
# above and moving the gripper.

def push(robot):
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper is not around the puck, put it around the puck.
    if check("the robot's gripper is not around puck"):
        robot.move_gripper("near the puck", close_gripper=True)

    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    if check("the robot's gripper is around puck"):
        # Push the gripper into the top of the puck to stabilize it
        if check("the robot's gripper is not inside puck"):
            robot.move_gripper("inside puck")
        # If the gripper is inside the puck, start sliding it towards the target
        # location
        if check("the robot's gripper is inside puck"):
            robot.move_gripper("above the target location")