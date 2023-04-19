
    if check("the robot's gripper is not near cube and the robot's gripper is below cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the cube is below the robot's gripper"):
        robot.reach("to goal")
    if check("the robot's gripper is near the goal and the cube is below the robot's gripper"):
        robot.sweep("cube towards goal")

# reach-into-box: reach into a box to grab an object
# def reach_into_box(robot):
    if check("the robot's gripper is not near the object and the robot's gripper is vertically aligned with the object"):
        robot.extend("arm into box")
    if check("the robot's gripper is not around the object and the robot's gripper is open"):
        robot.drop("gripper around object")
    if check("the robot's gripper is near the object and the object is below the robot's gripper"):
        robot.grab("object")
    if check("the robot's gripper is closed"):
        robot.lift("arm out of box with object")