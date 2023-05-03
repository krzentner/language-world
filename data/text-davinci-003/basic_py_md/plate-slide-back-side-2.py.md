

The program should aim to slide a plate back sideways into the target location.

If check("the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate"):
    robot.put("gripper above plate")

If check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate"):
    robot.grab("plate with gripper")

If check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
    robot.slide("plate back to the goal")

If check("the plate is just before the goal position"):
    robot.push("plate into the goal position")