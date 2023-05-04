

Your code must:
- Contain only the letters `a` through `z` (no punctuation except quotes `"`).
- Use exactly one instance of each of the following words, except you must fill
  in one missing word with a color:
  - "blue"
  - "green"
  - "purple"
  - "red"
  - "yellow"
- Contain only one instance of the string `"grip"`
- Contain exactly one instance of the word `"move"`
- Begin with the string `"drop"`
- Have a total of at least 15 words, not counting the words listed above.
"""
# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Move gripper down to push the puck along
    # First, put the gripper above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.drop("the green gripper down")
    # Move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck"):
        robot.move("the puck to the goal")



"""
--- Part Two ---

The robot seems to be doing better with the added constraints.
Inspired by this, you decide to add even more constraints to your code.

Your code must:
- Contain exactly five instances of the string `"drop"`
- Contain exactly one instance of the string `"move"`
- Not contain the word `"gripper"`
- Contain at least one color word
- Have a total of at least 50 words
"""
# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Move gripper down to push the puck along
    # First, put the gripper above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.drop("the green gripper down")
        robot.drop("the red gripper down")
        robot.drop("the blue gripper down")
        robot.drop("the yellow gripper down")
       