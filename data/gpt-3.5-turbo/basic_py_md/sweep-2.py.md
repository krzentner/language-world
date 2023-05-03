# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    if check("the robot's gripper is not vertically aligned with cube and the robot's gripper is below the cube"):
        robot.put("the gripper below the cube")
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is not around the cube"):
        robot.grab("the gripper around the cube")
    if check("the gripper is around the cube and the robot is not near the target location"):
        robot.move("the gripper to the left of the target location while holding the cube")
    if check("the gripper is left of the target location and the robot's gripper is vertically aligned with the target location"):
        robot.lower("the gripper until the cube touches the target location")
    if check("the cube is touching the target location"):
        robot.release("the gripper to drop the cube")