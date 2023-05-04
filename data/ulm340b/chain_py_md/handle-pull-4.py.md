

You may also need to use the following functions:

```
# check: check if a condition is met, and say something if it is
def check(cond):
    # If the condition is met, say what we're about to do, and then do it.
    if robot.check(cond):
        robot.say(cond)
```

```
# align: make object align horizontally to goal
def align(object, goal):
    if check("{} is not horizontally aligned with {}".format(object, goal)):
        robot.move("{} toward {}".format(object, goal))
```

```
# put: put the gripper over the object
def put(object):
    if check("the robot's gripper is not above {}".format(object)):
        robot.move("the gripper above {}".format(object))
    if check("the robot's gripper is not above {}".format(object)):
        robot.move("the gripper near {}".format(object))
```

```
# drop: drop the gripper around the object
def drop(object):
    if check("the robot's gripper is not near {}".format(object)):
        robot.move("the gripper near {}".format(object))
    if check("the robot's gripper is not around {}".format(object)):
        robot.move("the gripper around {}".format(object))
```

```
# grab: grab the object with the gripper
def grab(object):
    if check("{} is not inside the robot's gripper".format(object)):
        robot.grab("{}".format(object))
```

```
# insert: insert the object into the goal
def insert(object, goal):
    if check("{} is not inside {}".format(object, goal)):
        robot.insert("{} into {}".format(object, goal))
```

```
# reach: reach to the goal
def reach(goal):
    if check("the robot's gripper is not near {}".format(goal)):
        robot.move("gripper to {}".format(goal))
```

```
# slide: slide the object to the goal
def slide(object, goal):
    if check("{} is not at {}".format(object, goal)):
        robot.move("{} to {}".format(object, goal))
```

```
# push