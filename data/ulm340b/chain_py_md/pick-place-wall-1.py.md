

You may call `check` to test whether a condition holds in the environment. Here are a few examples:

```
check("the puck is right of the gripper")
check("the robot's gripper is open")
check("the robot's gripper is below the handle")
check("the robot's gripper is forward aligned with the puck and the puck is not horizontally aligned with the hole")
```

You may call `robot.place`, `robot.drop`, `robot.insert`, `robot.move`, `robot.pull`, `robot.push`, `robot.slide`, and `robot.close` to move the robot. Here are some examples:

```
robot.move("gripper to left of handle")
robot.put("gripper above handle")
robot.pull("handle to right")
robot.slide("handle to right")
robot.place("gripper around handle")
robot.close("gripper around handle")
robot.push("door open")
robot.slide("door to right")
```

Note: if a command is unsuccessful, the robot will still try to complete the command.

## How does the robot move?

![Animation showing how the robot works](assets/robot.gif)

The gripper is in a fixed position, but we can move the robot and the handle freely around the gripper.

## What commands can you call?

```python
# check
check("the robot's gripper is closed")
check("the puck is below the robot's gripper")

# place
robot.place("gripper above window handle")
robot.place("gripper around window handle")
robot.place("puck above puck target")
robot.place("gripper near puck")

# drop
robot.drop("gripper below puck")
robot.drop("gripper around puck")

# insert
robot.insert("handle into hole")

# move
robot.move("gripper left")
robot.move("gripper to left of puck")
robot.move("puck right of puck target")
robot.move("puck to right of puck target")

# pull
robot.pull("window handle right")
robot.pull("window handle to right")

# push
robot.push("window handle right")
robot.push("window handle to right")

# slide
robot.slide("window to the right")
robot.slide("window right")
robot.slide("window handle away from window")
robot.slide("window handle up")
robot.slide("handle into hole")

# close
robot.close("gripper around handle")
```

## What is the purpose of the