

If check("the robot's gripper is not above the plate"):
    robot.put("gripper above plate")
if check("the robot's gripper is not forward aligned with plate"):
    robot.grab("plate")
if check("the plate is not horizontally aligned with the target"):
    robot.align("plate to target")
if check("the plate is horizontally aligned with the target"):
    robot.slide("plate back to target")