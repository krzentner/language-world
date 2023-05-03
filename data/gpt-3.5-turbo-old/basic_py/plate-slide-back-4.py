if check("the robot's gripper is not above the plate and the robot's gripper is not vertically aligned with the plate"):
        robot.move("gripper above the plate")
    if check("the robot's gripper is vertically aligned with the plate and the plate is not aligned with the goal"):
        robot.align("the plate to the goal")
    if check("the plate is aligned with the goal and the robot's gripper is not near the plate"):
        robot.move("gripper near the plate")
    if check("the robot's gripper is near the plate and the plate is not below the robot's gripper"):
        robot.grab("the plate")
    if check("the plate is below the robot's gripper and the robot's gripper is not near the goal"):
        robot.slide("the plate to the goal")
    if check("the plate is near the goal"):
        robot.release("the plate at the goal")