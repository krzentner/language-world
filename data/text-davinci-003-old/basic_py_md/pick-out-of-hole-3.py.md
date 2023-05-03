

if check("the robot's gripper is not vertically aligned with the peg"):
        robot.place ("gripper above peg")
if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around peg"):
        robot.drop ("gripper around peg")
if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.close ("gripper around peg")
if check("the robot's gripper is around peg and the peg is below the robot's gripper"):
        robot.lift ("peg out of hole")
if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place ("puck at goal")