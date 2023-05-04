

The `assembly` task contains two objects, a `peg` and a `wrench`, that you must manipulate.
Like with the robot's gripper, you can check if the `peg` or `wrench` are at the same location as the robot's gripper or some other location.
You can also check if the `peg` is `left` or `right` of the robot's gripper, and if the `wrench` is `left`, `right`, `above`, or `below` the robot's gripper.

If the robot's gripper is near a `peg` or `wrench`, it can perform a `grab` action, like:

```
if check("peg is near the robot's gripper"):
    robot.grab("peg")
if check("wrench is near the robot's gripper"):
    robot.grab("wrench")
```

This will make the robot pick up the `peg` or `wrench`.
Once a `peg` or `wrench` has been grabbed by the robot's gripper, they will move with it until they are placed down.

If the robot's gripper is near a `peg` or `wrench` that it has grabbed, it can perform a `place` action, like:

```
if check("peg is near the robot's gripper"):
    robot.place("peg")
if check("wrench is near the robot's gripper"):
    robot.place("wrench")
```

This will make the robot put the `peg` or `wrench` it is holding down at that location.
If you want to put down the `peg` but only if the `peg` is in some other state, you can pass a dictionary of conditions as the second argument to the `place` action, like:

```
if check("peg is near the robot's gripper"):
    robot.place("peg", {"vertically aligned with the hole"})
```

This will only put down the `peg` if it is `vertically aligned with the hole`.

You may want to check if the `peg` is above or below the robot's gripper, even if the robot hasn't grabbed it.
You can check that as:

```
if check("the robot's gripper is above peg"):
    ...
if check("the robot's gripper is below peg"):
    ...
```

and the same for the `wrench`.

```
# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
