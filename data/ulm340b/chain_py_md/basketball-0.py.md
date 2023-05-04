

Please do not change anything else above this point,
and please keep the above instructions there even after you finish writing
the program.

"""

# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Place gripper above the ball
    #  2. Push gripper down around ball
    #  3. Close gripper around ball
    #  4. Lift the ball
    #  5. Move ball above the hoop
    #  6. Drop ball into the hoop

    # First, place the gripper above the ball so that we can pick it up
    if check("the robot's gripper is not above the ball and the robot's gripper is not vertically aligned with ball"):
        robot.place("gripper above the ball")

    # If the ball is under the gripper, push the gripper down around the ball to pick it up
    if check("the robot's gripper is above the ball"):
        robot.push("down around ball")

    # If the gripper is around the ball, we should be able to pick it up by closing the gripper
    if check("the robot's gripper is around the ball"):
        robot.close("gripper around the ball")

    # If the ball is not near the gripper or not aligned to the gripper, the robot likely dropped it. Go back to placing the gripper above the ball.
    if check("the ball is not near the robot's gripper or the ball is not vertically aligned with the robot's gripper"):
        robot.place("gripper above the ball")

    # If the ball is being held by the gripper, move the gripper up and keep the ball above the gripper
    if check("the ball is near the robot's gripper and the ball is vertically aligned with the robot's gripper"):
        robot.lift("ball above the gripper")

    # If the ball is above the gripper and the ball is not above the hoop, move the ball above the hoop
    if check("the ball is above the robot's gripper and the ball is not above the hoop"):
        robot.place("ball above the hoop")

    # If the ball is above the hoop, drop the ball into the hoop
    if check("the ball is above the hoop"):
        robot.drop("the ball into the hoop")
[eod] 