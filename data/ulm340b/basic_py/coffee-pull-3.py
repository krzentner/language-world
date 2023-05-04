
    if check("the mug is not near the robot's gripper"):
        robot.grab("mug")
    if check("the robot's gripper is forward aligned with mug"):
        robot.pull("away from cup")
    if check("the robot's gripper is below mug"):
        robot.put("mug at goal")

# coffee-push: grab the mug and push it to the target location
def coffee_push(robot):
    if check("the mug is not near the robot's gripper"):
        robot.grab("mug")
    if check("the robot's gripper is forward aligned with mug"):
        robot.push("mug to goal")

# pick-place-wall: pick up the puck and hold it over the goal
def pick_place_wall(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is closed"):
        robot.place("puck above goal")

# pick-place-wall-in: pick up the puck and hold it above the target location
def pick_place_wall_in(robot):
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is around puck and the robot's gripper is closed"):
        robot.place("puck inside goal")

# pick-place-side-in: grab the peg and place it into the hole
def pick_place_side_in(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the