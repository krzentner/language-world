
    if check("the robot's gripper is not vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is open"):
        robot.grab("the door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is closed"):
        robot.push("the door to the closed position")

# peg-unstack-side: grab the top block and place it to the side of the other block
def peg_unstack_side(robot):
    if check("the robot's gripper is not vertically aligned with the top peg"):
        robot.put("gripper above top peg")
    if check("the robot's gripper is vertically aligned with the top peg and the robot's gripper is not above the top peg"):
        robot.grab("top peg")
    if check("the robot's gripper is around top peg and top peg is above the other block"):
        robot.place("top peg down")
    if check("the robot's gripper is around top peg and top peg is on the other block"):
        robot.place("top peg aside")

# peg-unstack-side-v2: grab the top block and place it to the side of the other block
def peg_unstack_side_v2(robot):
    if check("the robot's gripper is not vertically aligned with the top peg"):
        robot.put("gripper above top peg")
    if check("the robot's gripper is vertically aligned with the top peg and the robot's gripper is not above the top peg"):
        robot.grab("top peg")
    if check("the robot's gripper is around top peg and top peg is above the other block"):
        robot.place("top peg down")
    if check("the robot's gripper is around top peg and top peg is on the other block"):
        robot.place("top peg aside")

# peg-unstack-side-v3: grab the top block and place it to the side of the other block
def peg_unstack_side_v3(robot):
    if check("the robot's gripper is not vertically aligned with the top peg"):
        robot.put("gripper above top peg")
    if check("the robot's gripper is vertically aligned with the top peg and the