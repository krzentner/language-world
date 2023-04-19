# push-back: slide the puck backwards to the target location
# def push_back(robot):
   if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
   if check("the robot's gripper is vertically aligned with the puck"):
        robot.pull("the gripper away from the puck")
   if check("the robot's gripper is not near the target location"):
        robot.move("the gripper back to the goal")
   if check("the robot's gripper is near the target location and the puck is below the robot's gripper"):
        robot.slide("the puck back to the goal")