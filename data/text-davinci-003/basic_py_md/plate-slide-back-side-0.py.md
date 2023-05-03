

If check("the robot's gripper is not above plate"):
    robot.put("gripper above plate")
if check("the robot's gripper is above plate and plate is not behind robot's gripper"):
    robot.grab("plate")
if check("the robot's gripper is forward aligned with plate and the plate is not horizontally aligned with goal"):
    robot.align("plate to goal")
if check("the plate is almost horizontally aligned with goal and the robot's gripper is not nearly above goal"):
    robot.slide("plate back sideways")
if check("the robot's gripper is nearly above goal and the plate is not vertically aligned with goal"):
    robot.align("plate to goal")
if check("plate is aligned with goal and robot's gripper is not almost above goal"):
    robot.move("gripper above goal")
if check("the robot's gripper is almost above goal"):
    robot.slide("plate back sideways into goal")