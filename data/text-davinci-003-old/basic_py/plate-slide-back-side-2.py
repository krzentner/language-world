
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    if check("the robot's gripper is not near the plate and the robot's gripper is open"):
        robot.grab("plate")
    if check("the robot's gripper is near the plate and the plate is not horizontally aligned with the goal"):
        robot.align("plate to the goal")
    if check("the plate is horizontally aligned with the goal"):
        robot.slide("plate back to goal")