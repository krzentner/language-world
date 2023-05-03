# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    if check("the robot's gripper is not above mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is vertically aligned with the mug and the robot's gripper is not near mug"):
        robot.push("gripper into mug")
    if check("the robot's gripper is near the mug and the mug is below the robot's gripper"):
        robot.grab("mug")
    if check("the mug is securely grasped by the robot's gripper"):
        if check("the robot's gripper is not vertically aligned with table"):
            robot.put("gripper above table")
        if check("the robot's gripper is vertically aligned with table and the robot's gripper is not near table"):
            robot.push("gripper towards table")
        if check("the robot's gripper is near the table and the mug is above the table"):
            robot.push("mug on table")