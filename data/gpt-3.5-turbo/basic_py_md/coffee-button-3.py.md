# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    if check("the robot's gripper is not near the coffee machine button"):
        robot.reach("to the coffee machine button")
    if check("the robot's gripper is near the coffee machine button"):
        robot.push("the button down") 

Note: `check` is a function that takes in a string describing a condition and returns a boolean value indicating whether that condition is true or false. It is assumed that the `robot` object has methods such as `reach`, `move`, `slide`, `push`, `grab`, `align`, `insert`, `put`, `drop`, `close`, and `place` that correspond to the actions described in the comments.