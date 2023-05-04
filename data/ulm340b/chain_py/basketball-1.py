
    # Steps:
    #  1. Put gripper above ball
    #  2. Drop gripper around ball
    #  3. Close gripper around ball
    #  4. Pick up ball
    #  5. Move gripper to ball hoop
    #  6. Release gripper
    #  7. Let go of the ball
    # First, we need to put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.put("gripper above ball")
    # If the gripper is above the ball, put the gripper around the ball.
    if check("the robot's gripper is above the ball and the robot's gripper is open"):
        robot.put("gripper around ball")
    # If the gripper is around the ball, close the gripper.
    # The ball should be inside the gripper now.
    if check("the robot's gripper is around the ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    # If the gripper is around the ball, move the gripper above the basket
    if check("the robot's gripper is around the ball and the ball is below the robot's gripper"):
        robot.put("gripper above ball hoop")
    # If the gripper is above the basket, drop the ball.
    if check("the robot's gripper is above ball hoop and the ball is below the robot's gripper"):
        robot.release("the ball")

# peg-insert-back: grab the peg and insert it into the hole from the back
def peg_insert_back(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg backwards into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if