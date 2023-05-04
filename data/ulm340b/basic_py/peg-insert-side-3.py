
    if check("the robot's gripper is not vertically aligned with the peg and the robot's gripper is above peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is above peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is around peg and the robot's gripper is below hole"):
        robot.place("peg into hole from the side")

# peg-insert-side-with-camera: grab the peg and insert it into the hole from the side
def peg_insert_side_with_camera(robot):
    if check("the robot's gripper is not vertically aligned with the peg and the robot's gripper is above peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is above peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is around peg and the robot's gripper is below hole"):
        robot.place("peg into hole from the side")

# peg-unstack-side: push the peg to the side until it is unstacked
def peg_unstack_side(robot):
    if check("the robot's gripper is not above the peg and the robot's gripper is not below peg"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the robot's gripper is in front of the peg"):
        robot.push("peg right")

# place-red-in-green-bin: pick up red puck and hold it in the green bin
def place_red_in_green_bin(robot):
    if check("the robot's gripper is not vertically aligned with red puck"):
        robot.put("gripper above red puck")
    if check("the robot's gripper is vertically aligned with the red puck and the robot's gripper is not around red puck"):
        robot.close("gripper around red puck")
    if check("the robot's gripper is above red puck"):
        robot.place("red puck above green bin")
    if check("the robot's gripper is vertically aligned with green bin"):
        robot.drop("red puck in green bin")

# place-red-on-blue: pick up the red block and place it on top