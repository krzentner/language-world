# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck and there is no wall blocking the path"):
        robot.push("gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper and there is no wall blocking the path"):
        robot.slide("puck until the wall is encountered")
    if check("the robot detects that there is a wall blocking its path and the puck is not pushed up against the wall"):
        robot.push("puck against the wall")
    if check("the puck is pushed up against the wall and the robot is not in the right position to push it towards the target"):
        robot.move("gripper to one side of the puck")
    if check("the robot's gripper is beside the puck and aligned towards the target"):
        robot.push("the puck towards the goal")