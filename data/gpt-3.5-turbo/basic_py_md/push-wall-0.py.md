# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck towards the small wall")
    if check("the small wall is in front of the puck and the robot's gripper"):
        robot.push("the puck up against the wall")
    if check("the puck is against the wall and the robot's gripper is not around the puck"):
        robot.grab("the puck against the wall")
    if check("the robot's gripper is around the puck and the robot's gripper is not above the goal"):
        robot.put("the gripper above the goal")
    if check("the robot's gripper is above the goal and the puck is not below the robot's gripper"):
        robot.push("the puck towards the goal")
    if check("the puck is below the robot's gripper and the robot's gripper is above the goal"):
        robot.release("the puck at the goal")