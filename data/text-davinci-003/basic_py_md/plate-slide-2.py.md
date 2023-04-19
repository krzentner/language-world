

if check("the robot's gripper is not near plate"):
    robot.move("gripper near plate")
if check("the robot's gripper is not above plate"):
    robot.place("gripper above plate")
if check("the robot's gripper is above plate and the plate is not forward aligned with the robot's gripper"):
    robot.rotate("plate to forward align with gripper")
if check("the plate is forward aligned with the robot's gripper and the plate is not aligned with the target destination"):
    robot.align("plate with target destination")
if check("the plate is aligned with the target destination and the robot's gripper is open"):
    robot.close("gripper around plate")
if check("the robot's gripper is near the plate and the robot's gripper is closed"):
    robot.slide("the plate to the target destination")