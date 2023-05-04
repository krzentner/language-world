

Make sure that you use appropriate function names, and that your code compiles before trying to submit it.

---

Here's what happens when a human writes a program:

```
# human-reach: reach to the target location
def human_reach(human):
    if check("human's gripper is not near reach target"):
        human.reach("to goal")
```

Now let's run the same function on a robot:

```
# robot-reach: reach to the target location
def robot_reach(robot):
    if check("robot's gripper is not near reach target"):
        robot.reach("to goal")
```

It's also valid to just call `reach(human)` or `reach(robot)` directly.

Now, can you please complete these programs so that they work correctly?

```
# human-push: push the puck to the target location
def human_push(human):
    if check("human's gripper is not above puck and human's gripper is not vertically aligned with the puck"):
        human.put("the gripper above the puck")
    if check("human's gripper is vertically aligned with the puck and human's gripper is not near puck"):
        human.push("the gripper into the puck")
    if check("human's gripper is near the puck and the puck is below human's gripper"):
        human.slide("the puck to the goal")

# human-pick-place: pick up the puck and hold it at the target location
def human_pick_place(human):
    if check("human's gripper is not above the puck"):
        human.place("gripper above puck")
    if check("human's gripper is not around puck and human's gripper is open"):
        human.drop("gripper around puck")
    if check("human's gripper is near puck and human's gripper is open"):
        human.close("gripper around puck")
    if check("human's gripper is above puck and human's gripper is closed"):
        human.place("puck at goal")

# robot-push: push the puck to the target location
def robot_push(robot):
    if check("robot's gripper is not above puck and robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("robot's gripper is vertically aligned with the