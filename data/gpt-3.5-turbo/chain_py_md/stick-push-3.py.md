# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
    # Steps:
    # 1. Position the stick near the thermos
    # 2. Use the stick to slide the thermos to the target location
    # First, position the stick roughly near the thermos. We cannot bump the thermos while positioning the stick, so we need to be careful here.
    if check("the stick is not near the thermos"):
        robot.position("the stick near the thermos")
    # Move the stick towards the thermos and slide the thermos towards the target location. We need to be careful to not exceed the maximum reach of the stick.
    if check("the stick is near the thermos and the thermos is not near the target"):
        robot.slide("the thermos with the stick to the target location")