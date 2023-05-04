

You can use the following methods of the `robot` object:

```
# robot: the robot that will manipulate objects
robot.align("align the peg to hole")
robot.close("gripper around puck")
robot.drop("gripper around puck")
robot.grab("peg")
robot.insert("peg into hole")
robot.move("gripper to left of window handle")
robot.open("drawer handle")
robot.place("puck at goal")
robot.put("gripper above puck")
robot.reach("to goal")
robot.push("button")
robot.push("the gripper into the puck")
robot.push("window left harder")
robot.push("window right harder")
robot.push("window to the left")
robot.pull("door open")
robot.push("gripper into puck")
robot.slide("gripper into drawer handle")
robot.slide("gripper right")
robot.slide("gripper to right")
robot.slide("window left")
robot.slide("window right")
robot.slide("the puck to the goal")
```

This may help, too:

```
# robot: the robot that will manipulate objects
robot.check("the robot's gripper is near puck and the robot's gripper is open")
robot.check("the robot's gripper is open")
```
'''

def robot_program(robot):
    if robot.check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if robot.check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if robot.check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if robot.check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if robot.check("the robot's gripper is not vertically aligned with button"):
