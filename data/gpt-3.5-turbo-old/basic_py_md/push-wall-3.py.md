# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper and the wall is not in front of the puck"):
        robot.slide("the puck until it hits the wall")
    if check("the robot's gripper is almost vertically aligned with the wall and the robot's gripper is open"):
        robot.put("gripper around the wall")
    if check("the robot's gripper is around the wall and the robot's gripper is closed"):
        robot.slide("the puck around the wall")
    if check("the robot's gripper is near the target location and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")