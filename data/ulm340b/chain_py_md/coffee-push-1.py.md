

and complete the program by filling in the if statements.
Remember to use correct grammar, capitalization, and punctuation.

```
# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper around mug
    #  2. Move mug towards the goal
    #  3. Check if mug is near goal, if yes: stop, else go to Step 2
    # First, put the gripper roughly around mug, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not around the mug"):
        robot.put("gripper around mug")
    # Now that the gripper is around the mug, we can just push the mug to the
    # goal.
    if check("the robot's gripper is around mug and the robot's gripper is closed"):
        robot.move("mug toward goal")
    # If the mug is near the goal, we can stop.
    # Otherwise, go back to moving the mug towards the goal.
    if check("the mug is near goal"):
        robot.stop("moving mug")
```

```python
import sys

def check(predicate):
    # This function checks if the given predicate is true
    raise NotImplementedError()
    return None

def command(robot, command):
    # This function issues a command to the robot
    raise NotImplementedError()
    return None

class Robot:
    def __init__(self):
        # A robot object
        pass

    def slide(self, direction):
        # The slide command
        raise NotImplementedError()
        return None

    def put(self, relation):
        # The put command
        raise NotImplementedError()
        return None

    def reach(self, goal):
        # The reach command
        raise NotImplementedError()
        return None

    def place(self, relation):
        # The place command
        raise NotImplementedError()
        return None

    def drop(self, relation):
        # The drop command
        raise NotImplementedError()
        return None

    def push(self, command):
        # The push command
        raise NotImplementedError()
        return None

    def grab(self, object):
        # The grab command
        raise NotImplementedError()
        return None

    def pull(self, direction):
        # The pull command
