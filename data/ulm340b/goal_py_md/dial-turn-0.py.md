
'''

'''
ANSWER:
# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put the gripper next to the dial
    #  2. Line up the gripper with the dial
    #  3. Turn the dial
    # First, put the gripper roughly next to the dial.
    if check("the robot's gripper is not near the dial"):
        robot.move_gripper("above the dial")
    # If the gripper is near the dial, we can line up the gripper with the dial
    if check("the robot's gripper is forward aligned with the dial"):
        robot.move_gripper("around the dial")
'''
[eod] [code]import pygame

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 255, 255))
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)



def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()
    #pygame.time.delay(2000)

    while