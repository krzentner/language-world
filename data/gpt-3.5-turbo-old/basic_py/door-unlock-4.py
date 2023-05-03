    if check("the robot's gripper is not near the dial on the door"):
        robot.move("gripper to the dial on the door")
    if check("the robot's gripper is near the dial on the door and the robot's gripper is not around the dial"):
        robot.grab("the dial on the door")
    if check("the robot's gripper is around the dial on the door and the dial is not aligned to unlock position"):
        robot.turn("dial to unlock position")
    if check("the dial on the door is aligned to unlock position"):
        robot.release("the dial on the door")