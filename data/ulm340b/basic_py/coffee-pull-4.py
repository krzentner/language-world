
    if check("the robot's gripper is not vertically aligned with mug"):
        robot.place("gripper above mug")
    if check("the robot's gripper is vertically aligned with mug and the robot's gripper is not forward aligned with mug"):
        robot.grab("mug")
    if check("the robot's gripper is forward aligned with mug and mug is not at goal"):
        robot.pull("mug away from table")

# coffee-push: grab the mug and push it to the target location
def coffee_push(robot):
    if check("the robot's gripper is not vertically aligned with mug"):
        robot.place("gripper above mug")
    if check("the robot's gripper is vertically aligned with mug and the robot's gripper is not forward aligned with mug"):
        robot.grab("mug")
    if check("the robot's gripper is forward aligned with mug and mug is not at goal"):
        robot.push("mug onto table")

# pick-place-wall: pick up the puck and hold it at the target location on the wall
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# sweep-into-goal: push the puck to the target location
def sweep_into_goal(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# block-stack-side: grab the block and set it down on top