
    if check("the robot's gripper is not almost vertically aligned with the stick"):
        robot.place("gripper above stick")
    if check("stick is not left of the robot's gripper and stick is not forward aligned with the robot's gripper"):
        robot.grab("stick")
    if check("the robot's gripper is not forward aligned with stick"):
        robot.put("gripper on top of stick")
    if check("the robot's gripper is forward aligned with stick"):
        robot.put("gripper on top of stick")
    if check("the robot's gripper is not vertically aligned with the stick and stick is not vertically aligned with thermos"):
        robot.push("stick into thermos")
    if check("the robot's gripper is vertically aligned with the stick and stick is vertically aligned with thermos and stick is not horizontally aligned with the thermos"):
        robot.push("stick into thermos")
    if check("stick is not horizontally aligned with thermos and stick is horizontally aligned with thermos"):
        robot.push("stick into thermos")
    if check("the robot's gripper is vertically aligned with the stick and stick is vertically aligned with thermos and stick is horizontally aligned with thermos"):
        robot.push("stick into thermos")
    if check("stick is horizontally aligned with thermos"):
        robot.push("stick into thermos")
    if check("the robot's gripper is vertically aligned with the stick and stick is vertically aligned with thermos and stick is horizontally aligned with thermos"):
        robot.slide("thermos to the goal")

# stick-place: grab the stick and hold it at the target location
def stick_place(robot):
    if check("the robot's gripper is not near stick"):
        robot.grab("stick")
    if check("the robot's gripper is not forward aligned with stick"):
        robot.place("gripper on top of stick")
    if check("the robot's gripper is forward aligned with stick"):
        robot.place("gripper on top of stick")
    if check("the robot's gripper is forward aligned with stick and stick is not horizontally aligned with goal"):
        robot.align("stick to the goal")
    if check("stick is horizontally aligned with goal"):
        robot.place("stick at the goal")

# pick-place-ball: pick up the ball and hold it at the target location
def