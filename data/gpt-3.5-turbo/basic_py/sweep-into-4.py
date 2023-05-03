def sweep_into(robot):
    if check("the robot's gripper is not above the cube and the cube is not close to the robot's gripper"):
        robot.put("gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not around the cube"):
        robot.grab("cube")
    if check("the robot's gripper is around the cube and the gripper is not above the target location"):
        robot.move("gripper above target location")
    if check("the robot's gripper is above the target location and the cube is not on the target location"):
        robot.move("gripper towards target location")
    if check("the cube is on the target location"):
        robot.release("cube")