

Then the program instructions.

if check("the robot's gripper is not near the dial"):
        robot.move("gripper near dial")
if check("the robot's gripper is near the dial"):
        robot.grab("dial")
if check("the robot's gripper is below the dial and the dial is not facing goal"):
        robot.turn("dial clockwise")
if check("the dial is facing goal"):
        robot.release("dial")