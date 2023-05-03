# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):
    wall_height = 2  # height of the wall in inches
    if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move("gripper up by " + str(wall_height) + " inches")
        robot.slide("the puck to the wall")
        robot.move("gripper down by " + str(wall_height) + " inches")
        robot.push("the gripper through the wall and into the puck")
        robot.slide("the puck to the goal")