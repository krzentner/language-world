
"""


def door_unlock(robot):
    if check("the robot's gripper is not near the door dial"):
        robot.put("gripper around door dial")
    if check("the robot's gripper is not left of the door dial"):
        robot.grab("door dial")
    if check("the robot's gripper is around door dial"):
        robot.turn("dial counter clockwise")
    if check("the door dial is not clockwise aligned with the door handle"):
        robot.turn("dial to the right")
    if check("the door dial is clockwise aligned with the door handle"):
        robot.pull("gripper away from dial")
    if check("the door dial is aligned with door handle"):
        robot.pull("door open")


"""## Challenge Task #6: `door-unlock-with-peg`

Now let's do the task 'door-unlock' with an object: `door-unlock-with-peg`.

Please write a program to perform the task `door-unlock-with-peg`.
Begin with the text:

```
# door-unlock-with-peg: turn the dial on the door with the peg
def door_unlock_with_peg(robot):
```
"""

def door_unlock_with_peg(robot):
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is vertically aligned with the peg and the peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is around the peg"):
        robot.put("the peg around the dial")
    if check("the robot's gripper is not near the door dial"):
        robot.put("the peg near the door dial")
    if check("the robot's gripper is around the dial and the peg is clockwise aligned with the door handle"):
        robot.pull("peg away from the dial")
    if check("the door dial is not clockwise aligned with the door handle"):
        robot.put("the peg around the dial")
    if check("the robot's gripper is around the dial and the peg is clockwise aligned with the door handle"):
        robot.pull("peg away from the dial")
    if check("the robot's gripper is not below the