

Once you have successfully written a program to push a coffee mug to a target location, your robot will be able to do many other things too.

<br>

### Task 2: What is the robot's current goal?

```
# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Move mug to goal
    # First, put the gripper roughly above the mug, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above mug"):
        robot.put("gripper above mug")
    # If the gripper is not around the mug, drop the gripper around the mug.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    # If the gripper is near the mug and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    # We closed the gripper, and the mug is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the mug to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        robot.move("mug to goal")
```


<div>

    <video width="50%" controls>
        <source src="{{ url_for('video', filename='coffee.mp4') }}" type="video/mp4">
        <source src="{{ url_for('video', filename='coffee.webm') }}" type="video/webm">
        Your browser does not support the video tag.
    </video>

    <div class="text-block">
        Now that the robot has grabbed the mug, what will it do next?
    </div>
    <p>
        <input type="radio" name="coffee-push" id="coffee-push-place" value="place