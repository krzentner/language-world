

And then you can use commands like:

```
robot.put("gripper above mug")
```

To move the gripper above the mug.

After writing your program, please answer the following questions:

How well do you understand the robot's environment and what it is doing?
How well did you understand how to write the robot's code?
How easy was it to understand the robot's code?

1.  Not at all
2.  Somewhat
3.  With difficulty
4.  Mostly
5.  Completely
6.  I could write it better
7.  With ease
8.  I could improve the code
9.  I could have written the robot's code better

For this experiment, what is your mturk worker ID?
"""

def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Grab mug
    #  3. Move mug to target location
    # Because it is easier to align with the mug from above, we first try to put the gripper above the mug
    if check("the robot's gripper is not above mug"):
        robot.put("gripper above mug")
    # Once the gripper is above the mug, if it is open, close the gripper around the mug
    if check("the robot's gripper is above the mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    # If the robot is holding the mug, it should move it to the target location
    if check("the robot's gripper is above the mug and the robot's gripper is closed"):
        robot.move("mug to target location")

# survey
how_understand_env = np.random.choice(
    [
        # "Not at all",
        "Somewhat",
        "With difficulty",
        # "Mostly",
        # "Completely",
        # "I could write it better",
        # "With ease",
        # "I could improve the code",
        # "I could have written the robot's code better"
    ],
    size=1
)[0]
how_understand_code = np.random.choice(
    [
        # "Not at all",
        "Somewhat",
        "With difficulty",
        # "Mostly",
        # "Completely",
        # "I could write it better",
        # "With ease",
        # "I could improve the code",