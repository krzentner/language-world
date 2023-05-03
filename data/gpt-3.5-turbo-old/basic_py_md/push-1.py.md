# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        # move gripper above puck
        robot.move("gripper to above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        # move gripper towards the puck
        robot.move("gripper towards puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        # slide the puck to the target location
        robot.slide("puck to goal")