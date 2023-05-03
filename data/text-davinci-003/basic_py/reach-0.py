
    if check("the robot's arm is not horizontally aligned with the target location"):
        robot.turn("the robot's arm to the aim at the target location")
    if check("the robot's arm is horizontally aligned with the target location and the robot's wrist is not pointed in the direction of the target location"):
        robot.turn("the robot's wrist to aim at the target location")
    if check("the robot's arm and wrist are both horizontally aligned with the target location and the robot's elbow is not bent to reach the target location"):
        robot.bend("the robot's elbow in the direction of the target location")
    if check("the robot's arm, wrist, and elbow are all aligned with the target location"):
        robot.reach("grasp the target location")