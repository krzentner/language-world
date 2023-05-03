# push-back: slide the puck backwards to the target location
def push_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into bottom of puck
    #  3. Slide puck backwards to goal
    # The robot can push the puck backwards using the same technique as pushing
    # it forward, but by pushing into the bottom of the puck instead of the top.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is not near the puck, move it down.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, push down into the bottom of the puck.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("around the puck")
    # Once the gripper is around the puck, slide it backwards towards the target
    # location.
    if check("the robot's gripper is around the puck"):
        robot.move_gripper("above the target location", close_gripper=True)