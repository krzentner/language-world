# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    # Steps:
    #  1. Put gripper above and slightly to the side of the cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move gripper sideways to move the cube to the goal
    # First, put the gripper above and slightly to the side of the cube.
    if check("the robot's gripper is not above and slightly to the side of the cube"):
        robot.put("gripper above and slightly to the side of the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the cube to the goal.
    if check("the robot's gripper is grasping the cube"):
        # Move the gripper to the left of the center of the cube
        robot.move("gripper to left of the center of the cube")
        # Slide the cube to the target location
        robot.slide("cube to the goal")