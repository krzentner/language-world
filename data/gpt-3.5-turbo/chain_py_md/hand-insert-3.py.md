# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Align the gripper with the side of the puck
    #  3. Grip the puck securely with the gripper
    #  4. Hold the puck steady
    #  5. Use your own hand to pick up and move the puck to the target location
    #  6. Release the puck
    # First, put the gripper roughly above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.grab("gripper above puck")
    # If the gripper is above the puck, align the gripper with the side of the puck.
    if check("the robot's gripper is above the puck and the puck is not horizontally aligned with the gripper"):
        robot.align("gripper to side of puck")
    # If the gripper is aligned with the side of the puck, grip the puck securely with the gripper.
    if check("the robot's gripper is aligned with the side of the puck and the gripper is not securely gripping the puck"):
        robot.grab("the puck securely with the gripper")
    # Hold the puck steady.
    if check("the robot's gripper is holding the puck securely"):
        robot.grip("the puck steady")
    # Move the puck to the target location using your own hand.
    print("Pick up and move the puck to the target location using your own hand.")
    # Release the puck.
    if check("the puck has been moved to the target location"):
        robot.release("gripper")