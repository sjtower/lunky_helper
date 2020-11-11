import pyWinhook as pyHook
import pygame
import os

COUNT = 0
BOW_STATE = 0
SISTER_COUNT = 0


# method to handle keyboard presses while this program is not in focus.
def OnKeyboardEvent(event):
    print('MessageName: %s' % event.MessageName)
    print('Message: %s' % event.Message)
    print('Time: %s' % event.Time)
    print('Window: %s' % event.Window)
    print('WindowName: %s' % event.WindowName)
    print('Ascii: %s' % event.Ascii, chr(event.Ascii))
    print('Key: %s' % event.Key)
    print('KeyID: %s' % event.KeyID)
    print('ScanCode: %s' % event.ScanCode)
    print('Extended: %s' % event.Extended)
    print('Injected: %s' % event.Injected)
    print('Alt %s' % event.Alt)
    print('Transition %s' % event.Transition)
    print('---')

    if event.Key == 'Left':
        cycle_orb_count()

    if event.Key == 'Right':
        cycle_bow()

    if event.Key == 'Up':
        cycle_sister_count()

    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True


# create the hook manager
hm = pyHook.HookManager()
# register one callback
hm.KeyDown = OnKeyboardEvent

# hook into the mouse and keyboard events
hm.HookKeyboard()


def main():
    # initialize pygame
    pygame.init()

    # set the program window to the top-right corner of the screen
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (5, 50)

    # initialize pygame's joysticks/controllers
    pygame.joystick.init()

    print("Available controllers: " + str(pygame.joystick.get_count()))

    # set values for the size of the tracker window
    display_width = 100
    display_height = 233

    # set the window size via pygame
    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Lunky Helper')

    black = (0, 0, 0)

    # a flag that tells us if the program crashed (should never be True)
    crashed = False

    # load the bow and orb images into pygame
    orb_image = pygame.image.load('SpelunkOrb.png')
    bow_image = pygame.image.load('SpelunkBow.png')
    sister_image_1 = pygame.image.load('SpelunkSister1.png')
    sister_image_2 = pygame.image.load('SpelunkSister2.png')
    sister_image_3 = pygame.image.load('SpelunkSister3.png')

    x = 0
    y = 0

    i = 0
    while not crashed:
        game_display.fill(black)

        display_orbs(game_display, orb_image, x, y)

        display_bow(bow_image, game_display, i, x, y)

        display_sisters(game_display, sister_image_1, sister_image_2, sister_image_3, x, y)

        # go through all the pygame events for processing. We don't do much here because we process via pyWinhook
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        # update pygame display (required)
        pygame.display.update()
        # tracking variable for the bow flashing effect
        i = i + 1

    pygame.joystick.quit()
    pygame.quit()
    quit()


def display_orbs(game_display, orb_image, x, y):
    # while COUNT goes up, display more orbs. COUNT is reset to 0 when it reaches 3
    if COUNT > 0:
        # display the first orb
        game_display.blit(orb_image, (x, y + 55))
    if COUNT > 1:
        # display the second orb
        game_display.blit(orb_image, (x, y + 103))
    if COUNT > 2:
        # display the third orb
        game_display.blit(orb_image, (x, y + 151))


def display_bow(bow_image, game_display, i, x, y):
    if BOW_STATE == 1:
        # display the bow
        game_display.blit(bow_image, (x + 20, y))
    elif BOW_STATE == 2 and i % 4 == 0:
        # display the bow with a flashing effect every 4th update
        game_display.blit(bow_image, (x + 20, y))


def display_sisters(game_display, sister_image_1, sister_image_2, sister_image_3, x, y):
    # while COUNT goes up, display more sisters. SISTER_COUNT is reset to 0 when it reaches 3
    if SISTER_COUNT > 0:
        # display the first sister
        game_display.blit(sister_image_1, (x, y + 55))
    if SISTER_COUNT > 1:
        # display the second sister
        game_display.blit(sister_image_2, (x, y + 105))
    if SISTER_COUNT > 2:
        # display the third sister
        game_display.blit(sister_image_3, (x, y + 155))


def cycle_orb_count():
    global COUNT
    if COUNT > 2:
        COUNT = -1
    COUNT = COUNT + 1


def cycle_bow():
    global BOW_STATE
    if BOW_STATE > 1:
        BOW_STATE = -1
    BOW_STATE = BOW_STATE + 1


def cycle_sister_count():
    global SISTER_COUNT
    if SISTER_COUNT > 2:
        SISTER_COUNT = -1
    SISTER_COUNT = SISTER_COUNT + 1


if __name__ == '__main__':
    import pythoncom

    main()
    # required for pyWinhook to process background input
    pythoncom.PumpMessages()
