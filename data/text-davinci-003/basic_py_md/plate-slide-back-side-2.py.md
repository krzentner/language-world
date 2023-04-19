

if check("the robot's gripper is not above plate"):
    robot.put("gripper above plate")
if check("the plate is not to the left of the robot's gripper and the plate is not forward aligned with the gripper"):
    robot.grab("plate")
if check("the plate is forward aligned with the gripper and the plate is not way to the right of the target location"):
    robot.move("plate to the right")
if check("the plate is almost way to the right of the target location"):
    robot.slide("plate towards target location")
if check("the plate is near the target location"):
    robot.slide("plate backwards")