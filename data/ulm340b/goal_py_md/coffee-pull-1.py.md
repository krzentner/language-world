

Now complete the body of `coffee-pull`, like the other example functions.
""",
    task2b=_task2b,
    posttask3=posttask3,
    task3="""
```
# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper around mug
    #  3. Close gripper around mug
    #  4. Slide mug forward towards the target location
    #  5. Move mug to the target location
    # First, put the gripper above the mug so we don't bump into it while trying
    # to grab it.
    if check("the robot's gripper is not above mug"):
        robot.move_gripper("above mug", close_gripper=True)
    # The mug is a very wide object, so to grab it, check that the gripper is in
    # front of it instead of around it.
    if check("the robot's gripper is not forward aligned with mug"):
        robot.move_gripper("forward aligned with mug")
    # If the gripper is around the mug and closed, move it to the target
    # location.
    if check("the robot's gripper is near mug and the robot's gripper is forward aligned with mug"):
        robot.move_gripper("above the target location")
```

""",
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--task", choices=tasks.keys(), nargs="*", default=tasks.keys()
    )
    args = parser.parse_args()
    for task_name in args.task:
        print()
        task_info = tasks[task_name]
        task_intro = task_info["intro"]
        task_instructions = task_info["instructions"]
        posttask = task_info["posttask"]
        try:
            if task_intro is not None:
                print(task_intro)
            task = getattr(sys.modules[__name__], "task" + task_name)
            task()
            task_instructions = tasks[task_name]["instructions"]
            if task_instructions is not None:
                print()
                print(task_instructions)
                time.sleep(1