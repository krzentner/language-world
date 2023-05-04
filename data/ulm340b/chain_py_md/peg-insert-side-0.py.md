

The task is to insert the peg into the target location using only sideway
motion. To perform the task, the robot needs to grab the peg first.
`check("robot has peg")` would be true when it does.

The task is completed when `check("peg is in the target location")` is true.
Please try to use the commands `put`, `grab`, `slide` or other commands if
necessary, but try not to use `move` directly.

You may refer to the commands defined as follows:

```
# put: put the robot's gripper near the target location
def put(goal):
    robot.move("gripper to", goal)

# grab: move the robot's gripper to the target location with the gripper closed
def grab(goal):
    robot.put(goal)
    robot.close("gripper around", goal)

# slide: slide the robot's gripper with the gripper closed
def slide(direction):
    robot.put(direction)
    robot.close("gripper around", direction)
    robot.put("gripper", direction)

# pull: pull the robot's gripper open with the gripper closed
def pull(direction):
    robot.put(direction)
    robot.close("gripper around", direction)
    robot.pull("gripper", direction)
```

Your code should run as follows:

```
In [14]: door_open(robot)
In [15]: robot.get('camera')
Out[15]:
array([[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
          0,  0,  0,  0,  0,  