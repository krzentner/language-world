if check("the hammer is not near the nail"):
        robot.grab("hammer")
        robot.move("hammer to the nail")
    if check("the hammer is near the nail and the hammer head is aligned to the nail head"):
        robot.swing("hammer at the nail") 
    if check("the hammer has hit the nail"):
        robot.pull("hammer back")