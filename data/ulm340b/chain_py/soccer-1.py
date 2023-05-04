
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push gripper into top of soccer ball
    #  3. Slide soccer ball to goal
    # The soccer ball can be slid by trapping it against a wall.
    # If the gripper isn't above the soccer ball, put it there.
    if check("the robot's gripper is not above soccer ball"):
        robot.put("gripper above soccer ball")
    # If the gripper is above the soccer ball but not near it, push it down.
    if check("the robot's gripper is above soccer ball and the robot's gripper is not near soccer ball"):
        robot.push("gripper into soccer ball")
    # If the gripper is near the soccer ball we probably have it trapped against
    # the wall, so push it forward.
    # Close the gripper to make sure we keep control of the soccer ball.
    if check("the robot's gripper is near soccer ball and soccer ball is below robot's gripper"):
        robot.slide("soccer ball to goal")

# peg-insert-topdown: push the peg down into the hole
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg down into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above the peg")
    # If the peg is not forward aligned with the robot's gripper, close the
    # gripper around the peg to grab it.
    if check("peg is not forward aligned with the robot's gripper and the robot's gripper is open"):
        robot.close("gripper around peg")
    # If the peg is forward aligned with the gripper, move the gripper over to
    # align with the hole.
    # Make sure the robot's gripper is above the peg, so that we don't bump the
    # peg while grabbing it.
    if check("peg is forward aligned with the robot's gripper and peg is not aligned with hole"):