
    if check("the robot's gripper is not above the mug handle and the robot's gripper is below the mug handle"):
        robot.put("the gripper above the mug handle")
    if check("the robot's gripper is above the mug handle and the robot's gripper is not near the mug handle"):
        robot.grab("the mug handle")
    if check("the robot's gripper is near the mug handle and the robot's gripper is open"):
        robot.close("the gripper around the mug handle")
    if check("the robot's gripper is around the mug handle"):
        robot.pull("the mug to the goal")

# coffee-push: grab the mug and push it to the target location
def coffee_push(robot):
    if check("the robot's gripper is not above the mug handle and the robot's gripper is below the mug handle"):
        robot.put("the gripper above the mug handle")
    if check("the robot's gripper is above the mug handle and the robot's gripper is not near the mug handle"):
        robot.grab("the mug handle")
    if check("the robot's gripper is near the mug handle and the robot's gripper is open"):
        robot.close("the gripper around the mug handle")
    if check("the robot's gripper is around the mug handle"):
        robot.push("the mug to the goal")

# coffee-pick-place: pick up the mug and hold it at the target location
def coffee_pick_place(robot):
    if check("the robot's gripper is not above the mug handle and the robot's gripper is below the mug handle"):
        robot.put("the gripper above the mug handle")
    if check("the robot's gripper is above the mug handle and the robot's gripper is not near the mug handle"):
        robot.grab("the mug handle")
    if check("the robot's gripper is near the mug handle and the robot's gripper is open"):
        robot.close("the gripper around the mug handle")
    if check("the robot's gripper is around the mug handle"):
        robot.place("the mug at the goal")

# block-stack: place one block on top of another
def block_stack(robot):
    if check("the robot's gripper is not near the target location of block 1"):
        robot