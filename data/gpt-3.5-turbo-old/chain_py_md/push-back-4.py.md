# push-back: slide the puck backwards to the target location
# def push_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into bottom of puck
    #  3. Slide puck backwards to goal
    # First, we need to put the gripper above the puck, but closer to the robot's
    # end.
    if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck and the gripper is not near the end of the puck"):
        robot.move("gripper above puck and closer to the robot's end")
    # We grab the puck by pushing the gripper into the bottom of the puck
    if check("the robot's gripper is above the puck and the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck"):
        robot.push("the gripper into the bottom of the puck")
    # Once the gripper is around the puck we can slide it backwards to the goal
    if check("the robot's gripper is around the puck and puck is between robot and goal"):
        robot.slide("the puck backwards to the goal")