# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    if check("the robot's gripper is not vertically aligned with the puck and the puck is not behind the small wall"):
        robot.put("gripper above puck and to the left of small wall")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck"):
        robot.grab("puck")
    if check("the robot's gripper is around the puck and the robot's gripper is not above the small wall"):
        robot.lift("the puck over the small wall")
    if check("the robot's gripper is above the small wall and the puck is not at the target location"):
        robot.push("the puck to the goal")