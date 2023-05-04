
    if check("the robot's gripper is not above the dial"):
        robot.place("gripper above dial")
    if check("the robot's gripper is above the dial and the robot's gripper is open"):
        robot.drop("gripper around dial")
    if check("the robot's gripper is around the dial and the robot's gripper is open"):
        robot.close("gripper around dial")
    if check("the robot's gripper is vertically aligned with the dial and the robot's gripper is closed"):
        robot.turn("the dial clockwise")

# peg-unstack-side: take a peg from the side of the stack and place it at the target location
def peg_unstack_side(robot):
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is around peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.lift("the peg into the air")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.drop("the peg to the goal")

# peg-unstack-top: take a peg from the top of the stack and place it at the target location
def peg_unstack_top(robot):
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is around peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.lift("the peg into the air")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.drop("the peg to the goal")

#