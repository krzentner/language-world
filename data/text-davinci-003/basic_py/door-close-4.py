
    if check("the robot's gripper is not near door handle and the door is open"):
        robot.move("gripper to the door handle")
    if check("the robot's gripper is near the door handle"):
        robot.push("door closed")

# cup-push: slide the cup to the target location
# def cup_push(robot):
    if check("the robot's gripper is not above cup and the robot's gripper is not vertically aligned with cup"):
        robot.put("gripper above cup")
    if check("the robot's gripper is vertically aligned with cup and the robot's gripper is not near cup"):
        robot.push("gripper into cup")
    if check("the robot's gripper is near the cup and the cup is below the robot's gripper"):
        robot.slide("cup to goal")