# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
if check("the robot's gripper is not near the wall"):
    robot.move("gripper closer to wall")
if check("the robot's gripper is near the wall and the robot's gripper is not vertically aligned with the target"):
    robot.move("gripper higher")
if check("the robot's gripper is vertically aligned with the target and there is a wall in the way"):
    robot.move("gripper to the side of the wall")
if check("the robot's gripper is closer to the wall than to the target"):
    robot.move("gripper to the other side of the wall")
if check("the robot's gripper is closer to the target than to the wall"):
    robot.reach("to goal")