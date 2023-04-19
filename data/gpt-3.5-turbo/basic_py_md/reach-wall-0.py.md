# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    if check("the robot's gripper is not near the wall"):
        robot.move("gripper to wall")
    if check("the robot's gripper is near the wall and the robot's gripper is not above the wall"):
        robot.lift("gripper above the wall")
    if check("the robot's gripper is above the wall and the robot's gripper is not near the goal"):
        robot.move("gripper to goal")
    if check("the robot's gripper is near the goal and the robot's gripper is not vertically aligned with the goal"):
        robot.adjust("gripper to be vertically aligned with goal")
    if check("the robot's gripper is vertically aligned with the goal and the robot's gripper is not at the goal"):
        robot.move("gripper to goal")