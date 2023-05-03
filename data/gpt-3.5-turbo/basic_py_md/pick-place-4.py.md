# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck"):
        robot.grab("the puck")
    if check("the robot's gripper is holding the puck and the robot's gripper is not near the target location"):
        robot.move("the gripper to the target location")
    if check("the robot's gripper is near the target location"):
        robot.put("the puck at the target location")