
    # Steps:
    #  1. Put the hammer above the nail
    #  2. Drop the hammer on the nail
    # Line up the hammer so that it as viewed from above is near the nail.
    if check("the hammer is not vertically aligned with the nail"):
        robot.put("hammer above nail")
    # If the hammer is near the nail, drop it.
    if check("the hammer is vertically aligned with the nail"):
        robot.drop("hammer on nail")