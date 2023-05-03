# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above the cube
    #  2. Grab the cube
    #  3. Move the gripper to the left side of the cube
    #  4. Move the gripper to the left until the cube touches the left wall
    #  5. Move the gripper down until the cube touches the floor
    #  6. Move the gripper right and push the cube into the target location
    # First, align the robot's gripper above the cube.
    if check("the robot's gripper is not vertically aligned with cube"):
        robot.put("gripper above cube")
    # Next, pick up the cube.
    if check("the robot's gripper is vertically aligned with cube and the robot's gripper is not around cube"):
        robot.grab("cube")
    # Move the gripper to the left side of the cube.
    if check("the robot's gripper is around cube and the robot's gripper is not on the left side of cube"):
        robot.move("gripper to left of cube")
    # Move the gripper to the left until the cube touches the left wall.
    if check("the robot's gripper is on the left side of cube and the cube is not touching the left wall"):
        robot.slide("cube left until it touches the wall")
    # Move the gripper down until the cube touches the floor.
    if check("the cube is not touching the floor"):
        robot.push("gripper down until cube touches the floor")
    # Move the gripper right and push the cube into the target location.
    if check("the cube is touching the floor and the robot's gripper is on the left side of the cube and the robot's gripper is not in front of the target location"):
        robot.slide("cube right and push into target location")