# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the wall")
    if check("the wall is blocking the path of the puck and the robot's gripper is not near the wall"):
        robot.move("gripper to right of wall")
    if check("the robot's gripper is near the wall"):
        robot.slide("puck against wall")
    if check("the robot's gripper is in front of the puck"):
        robot.push("the puck to the goal")