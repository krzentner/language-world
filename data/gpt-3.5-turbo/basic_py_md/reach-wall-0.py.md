# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    if check("the robot's gripper is not near the wall"):
        robot.move("gripper to the left of the wall")
    if check("the robot's gripper is to the left of the wall"):
        robot.move("gripper above the wall")
    if check("the robot's gripper is above the wall and not near the goal"):
        robot.move("gripper to the right of the wall")
    if check("the robot's gripper is to the right of the wall and not near the goal"):
        robot.move("gripper above the goal")
    if check("the robot's gripper is above the goal and not holding anything"):
        robot.grab("the target object")
    if check("the gripper is holding the target object and above the goal"):
        robot.drop("the target object")