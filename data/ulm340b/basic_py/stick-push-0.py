
    if check("the robot's gripper is not vertically aligned with stick"):
        robot.put("gripper above stick")
    if check("stick is not left of the robot's gripper and stick is not forward aligned with the robot's gripper"):
        robot.grab("stick")
    if check("the robot's gripper is forward aligned with stick and stick is not vertically aligned with thermos"):
        robot.align("stick to thermos")
    if check("stick is vertically aligned with thermos"):
        robot.push("thermos to the goal")

# stick-place: grab the stick and place it upright inside the thermos at the target location
def stick_place(robot):
    if check("the robot's gripper is not vertically aligned with stick"):
        robot.put("gripper above stick")
    if check("stick is not left of the robot's gripper and stick is not forward aligned with the robot's gripper"):
        robot.grab("stick")
    if check("the robot's gripper is forward aligned with stick and stick is not vertically aligned with thermos"):
        robot.align("stick to thermos")
    if check("stick is vertically aligned with thermos and thermos is below the robot's gripper"):
        robot.drop("stick into the thermos")

# shape-insert: grab the shape and insert it into the matching target location
def shape_insert(robot):
    if check("the robot's gripper is not vertically aligned with shape"):
        robot.put("gripper above shape")
    if check("shape is not left of the robot's gripper and shape is not forward aligned with the robot's gripper"):
        robot.grab("shape")
    if check("the robot's gripper is forward aligned with shape and shape is not horizontally aligned with target"):
        robot.align("shape to target")
    if check("shape is horizontally aligned with target"):
        robot.insert("shape into goal")

# block-stack: stack the block on top of the target
def block_stack(robot):
    if check("the robot's gripper is not above the block"):
        robot.put("gripper above block")
    if check("the robot's gripper is above the block and the robot's gripper is not around the block"):
        robot.put("gripper around block")
    if check("the robot's