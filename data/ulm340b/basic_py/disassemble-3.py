
    if check("the robot's gripper is not vertically aligned with wrench"):
        robot.put("gripper around wrench")
    if check("the robot's gripper is near the wrench and the robot's gripper is open"):
        robot.close("gripper around wrench")
    if check("the robot's gripper is vertically aligned with wrench"):
        robot.pull("wrench off peg")

# peg-unstack-side: grab the top peg and lift it off from the side
def peg_unstack_side(robot):
    if check("the robot's gripper is not vertically aligned with peg and the robot's gripper is above peg"):
        robot.put("gripper below peg")
    if check("the robot's gripper is below peg and the robot's gripper is not around peg"):
        robot.put("gripper around peg")
    if check("the robot's gripper is around peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is around peg"):
        robot.lift("peg off table")

# peg-unstack-side-v2: grab the top peg and lift it off from the side
def peg_unstack_side_v2(robot):
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is not around peg"):
        robot.put("gripper around peg")
    if check("the robot's gripper is around peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is around peg"):
        robot.lift("peg off table")

# assemble: put the peg into the hole on the table
def assemble(robot):
    if check("the robot's gripper is not left of hole"):
        robot.put("gripper above hole")
    if check("the robot's gripper is left of hole and the robot's gripper is not near hole"):
        robot.slide("gripper above hole")
    if check("the robot's gripper is near hole and the robot's gripper is open"):
        robot.put("gripper around hole")
    if check("the robot'