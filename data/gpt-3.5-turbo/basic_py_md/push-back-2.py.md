# push-back: slide the puck backwards to the target location
def push_back(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.rotate("the gripper 180 degrees")
        robot.push("the gripper into the puck")
    if check("the robot's gripper is above the puck and the puck is below the robot's gripper"):
        robot.rotate("the gripper back to its initial position")
        robot.slide("the puck to the goal in reverse")