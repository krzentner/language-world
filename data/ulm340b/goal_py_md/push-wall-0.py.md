

And then please use this space to write a program to control the robot to do
this task. Try to match the style of the other robot programs, especially the
ones for `push` and `reach`.

<details>

---

```

# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put gripper above the puck, but close to the wall
    #  2. Push gripper into top of puck
    #  3. Slide puck over wall to goal
    # First, move the gripper down so it's above the puck, but close to the
    # wall.
    if check("the robot's gripper is not above puck and the robot's gripper is not near the wall"):
        robot.move_gripper("near the wall", close_gripper=True)
    # If the gripper is near the puck and not around the puck, try moving the
    # gripper onto the puck so we trap the puck.
    if check("the robot's gripper is near puck and the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    if check("the robot's gripper is near puck and the puck is below the robot's gripper"):
        robot.move_gripper("near the target location")

```

---

</details>
"""

# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.move_gripper("left of the door handle")