Here's a program to perform `hammer` task:

```
# hammer: hit the nail with the hammer
# def hammer(robot):
    if check("the hammer is not near the nail"):
        robot.reach("to the hammer")
        robot.grab("the hammer")
        robot.reach("to the nail")
    robot.swing("the hammer")
    robot.release("the hammer")
```

Explanation:
- First, we check if the hammer is not near the nail. If so, we reach for the hammer, grab it, and then reach for the nail.
- Next, we swing the hammer towards the nail to hit it.
- Finally, we release the hammer to let it go back to its original position.