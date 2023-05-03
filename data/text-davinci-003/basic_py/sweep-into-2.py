
    if check("cube is not left of the robot's gripper and cube is not forward aligned with the robot's gripper"):
        robot.grab("cube")
    if check("the robot's gripper is forward aligned with the cube and the cube is not above the target location"):
        robot.sweep("cube into target location")

# move-on-rails: move the robot along the rails
def move_on_rails(robot):
    if check("the robot is not positioned on the rails"):
        robot.move("onto the rails")
    if check("the robot is on rails"):
        robot.push("forward on the rails")