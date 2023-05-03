# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    if check("the robot's gripper is not near the puck"):
        robot.move("gripper to the puck")
    if check("the gripper is above the puck and vertically aligned with the puck"):
        robot.grab("the puck")
    if check("the robot's gripper is not near the target location"):
        robot.move("gripper to the target location")
    if check("the gripper is above the target location and vertically aligned with the target location"):
        robot.place("the puck")