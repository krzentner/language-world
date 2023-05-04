
    if check("the robot's gripper is not vertically aligned with the ball and the robot's gripper is below the ball"):
        robot.place("the gripper above the ball")
    if check("the robot's gripper is vertically aligned with the ball"):
        robot.push("down on the ball")
    if check("the robot's gripper is not around the ball and the robot's gripper is open"):
        robot.put("the gripper around the ball")
    if check("the robot's gripper is around the ball and the robot's gripper is open"):
        robot.close("the gripper around the ball")
    if check("the robot's gripper is vertically aligned with the hoop"):
        robot.raise("the ball into the hoop")

# basketball-v2: put the ball into into the hoop
def basketball_v2(robot):
    if check("the robot's gripper is not vertically aligned with the ball and the robot's gripper is below the ball"):
        robot.place("the gripper above the ball")
    if check("the robot's gripper is vertically aligned with the ball"):
        robot.push("down on the ball")
    if check("the robot's gripper is not around the ball and the robot's gripper is open"):
        robot.put("the gripper around the ball")
    if check("the robot's gripper is around the ball and the robot's gripper is open"):
        robot.close("the gripper around the ball")
    if check("the robot's gripper is vertically aligned with the hoop"):
        robot.put("the ball in the hoop")

# peg-unplug-side: grab the peg and pull it out of the hole from the side
def peg_unplug_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg and peg is not below the robot's gripper"):
        robot.place("gripper above peg")
    if check("peg is below the robot's gripper and peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.