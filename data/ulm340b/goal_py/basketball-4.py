
    # Steps:
    #  1. Move the robot's gripper to above the ball.
    #  2. Close the gripper around the ball.
    #  3. Bring the ball to the basket and hold the robot's gripper open.
    #  4. Drop the ball into the basket.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    if check("the robot's gripper is not closed and the robot's gripper is above the ball"):
        robot.move_gripper("below the ball", close_gripper=True)
    if check("the robot's gripper is above the basket"):
        robot.move_gripper("above the basket")
    if check("the robot's gripper is above the basket and the robot's gripper is closed"):
        robot.move_gripper("below the basket", close_gripper=False)

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the left
    #  2. Push down on the button from the side
    # Because this is "side", we just need to line up the gripper from the side.
    # Line up the gripper as seen from the left.
    if check("the robot's gripper is not left aligned with button"):
        robot.move_gripper("left aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is left aligned with button"):
        robot.move_gripper("near the button")

# pick-place-wall: pick up the block and hold it at the target location
def pick_place_wall(robot):
    # Steps:
    #  1. Move the gripper to above the block.
    #  2. Close the gripper around the block.
    #  3. Bring the block to the target location and hold the gripper open.
    #  4. Drop the block onto the target location.
    if check("the robot's gripper is not above the block"):
        robot.move_gripper("above the block")
 