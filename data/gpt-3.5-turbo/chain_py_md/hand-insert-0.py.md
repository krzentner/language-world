# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    # Steps:
    #  1. Put gripper above table
    #  2. Drop gripper around puck
    #  3. Pick up puck with hand
    #  4. Move hand to goal
    #  5. Drop puck at goal
    # Put the gripper above the table near the puck.
    if check("the robot's gripper is not above the table near the puck"):
        robot.put("gripper above table near the puck")
    # Drop the gripper around the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.drop("gripper around the puck")
    # Pick up the puck with the hand without using the robot's gripper.
    if check("the puck is not in the robot's hand"):
        robot.pickup("puck with the hand")
    # Move the hand to the goal.
    if check("the hand is not at the goal"):
        robot.move("hand to the goal")
    # Drop the puck at the goal.
    if check("the puck is in the robot's hand and the hand is at the goal"):
        robot.drop("puck at the goal")