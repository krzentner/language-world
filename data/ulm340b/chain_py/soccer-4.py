
    # Steps:
    #  1. Put gripper behind the ball
    #  2. Push the ball to the goal
    # If the ball is in front of the gripper, it needs to be behind the gripper.
    if check("the soccer ball is in front of the robot's gripper"):
        robot.move("gripper behind soccer ball")
    # If the ball is behind the gripper, push the ball forward towards the goal.
    if check("the soccer ball is behind the robot's gripper"):
        robot.push("the ball towards the goal")

# peg-insert-topdown: grab the peg and insert it into the hole from the top
def peg_insert_topdown(robot):
    # Steps:
    #  1. Move the gripper above the peg
    #  2. Close the gripper around the peg
    #  3. Align the gripper and peg to the hole
    #  4. Insert the peg into the hole
    #  5. Push the peg down into the hole
    # Move the gripper above the peg so that we can put it around the peg.
    if check("the robot's gripper is not above the peg"):
        robot.put("the gripper above the peg")
    # If the peg is not left of the gripper, we should be able to grab it.
    if check("peg is not left of the robot's gripper"):
        robot.close("gripper around peg")
    # Once the peg is grabbed, move the gripper towards the hole.
    if check("the robot's gripper is around peg"):
        robot.align("gripper to hole")
    # If the gripper and peg are above the hole, try inserting the peg into the
    # hole.
    if check("the robot's gripper is vertically aligned with hole"):
        robot.insert("peg into hole")
    # If the gripper is still vertically aligned with the hole, try pushing the
    # peg down harder to fully insert it.
    if check("the robot's gripper is vertically aligned with hole"):
        robot.push("down on peg")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door handle
    #