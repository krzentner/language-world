
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.put("peg in hole")

# peg-unplug-side: unplug the peg from the hole from the side
def peg_unplug_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is not around peg"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is around peg"):
        robot.pull("peg from hole")

# lift: lift the block up to the target location
def lift(robot):
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.place("gripper above block")
    if check("the robot's gripper is not around the block"):
        robot.drop("gripper around block")
    if check("the robot's gripper is around block"):
        robot.raise("block to goal")

# pick-place-with-camera: pick up the puck and hold it at the target location
def pick_place_with_camera(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# peg-insert-side-with-camera: grab the peg and insert it into the hole from the side
def peg_insert_side_with_camera(robot):
 