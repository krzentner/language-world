
    if check("the robot's gripper is not vertically aligned with the mug handle and the robot's gripper is below the mug handle"):
        robot.put("gripper above mug handle")
    if check("the robot's gripper is vertically aligned with the mug handle and the robot's gripper is not right of the mug handle"):
        robot.put("gripper right of mug handle")
    if check("the robot's gripper is right of the mug handle and the robot's gripper is open"):
        robot.close("gripper around mug handle")
    if check("the robot's gripper is right of the mug handle and the robot's gripper is near the mug handle"):
        robot.lift("the mug off the table")
    if check("the mug is off the table"):
        robot.move("the mug to the goal")

# stack-block-vert: pick up the block and set it on the target block
def stack_block_vert(robot):
    if check("the robot's gripper is not above the block"):
        robot.place("gripper above the block")
    if check("the robot's gripper is not above the block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is above the block and the robot's gripper is near the block"):
        robot.lift("the block off the table")
    if check("the block is off the table"):
        robot.put("the block on the goal block")

# door-lock: turn the key in the door to unlock it
def door_lock(robot):
    if check("the robot's gripper is not vertically aligned with key"):
        robot.place("gripper above key")
    if check("the robot's gripper is above key and the robot's gripper is not around the key"):
        robot.put("gripper around key")
    if check("the robot's gripper is around key"):
        robot.turn("key to left")

# door-unlock: turn the key in the door to lock it
def door_unlock(robot):
    if check("the robot's gripper is not vertically aligned with key"):
        robot.place("gripper above key")
    if check("the robot's gripper is above key and the robot's gripper is not around the key"):
        robot.put("g