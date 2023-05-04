
    if check("the robot's gripper is above the block"):
        robot.put("gripper above the block")
    if check("the robot's gripper is not around the block"):
        robot.grab("the block")
    if check("the robot's gripper is above block"):
        robot.put("gripper to the shelf")
    if check("the robot's gripper is near the shelf"):
        robot.put("the block on the shelf")

# shelf-place-side: pick up the block and place it at the target location
def shelf_place_side(robot):
    if check("the robot's gripper is above the block"):
        robot.put("gripper above the block")
    if check("the robot's gripper is not around the block"):
        robot.grab("the block")
    if check("the robot's gripper is above block"):
        robot.put("gripper to the shelf")
    if check("the robot's gripper is near the shelf"):
        robot.put("the block on the shelf")

# shelf-place-sideway: pick up the block and place it at the target location
def shelf_place_sideway(robot):
    if check("the robot's gripper is above the block"):
        robot.put("gripper above the block")
    if check("the robot's gripper is not around the block"):
        robot.grab("the block")
    if check("the robot's gripper is above block"):
        robot.put("gripper to the shelf")
    if check("the robot's gripper is near the shelf"):
        robot.put("the block on the shelf")

# flip: flip over the object
def flip(robot):
    if check("the robot's gripper is not above the block"):
        robot.put("gripper above the block")
    if check("the robot's gripper is not around the block"):
        robot.grab("the block")
    if check("the robot's gripper is around the block"):
        robot.flip("over the object")

# pick-place-side: pick up the block and put it at the target location
def pick_place_side(robot):
    if check("the robot's gripper is not above the block"):
        robot.put("gripper above the block")
    if check("the