import pyWinhook as pyHook
import pygame
import os

COUNT = 0
BOW_STATE = 0


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
        cycle_count()

    if event.Key == 'Right':
        cycle_bow()

    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True


# create the hook mananger
hm = pyHook.HookManager()
# register two callbacks
hm.KeyDown = OnKeyboardEvent

# hook into the mouse and keyboard events
hm.HookKeyboard()


def main():
    pygame.init()

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (5, 50)

    pygame.joystick.init()

    print("Available controllers: " + str(pygame.joystick.get_count()))

    joystick = pygame.joystick.Joystick(1)
    joystick.init()

    display_width = 100
    display_height = 233

    game_display = pygame.display.set_mode((display_width, display_height), 0, 32)
    pygame.display.set_caption('Lunky Helper')

    black = (0, 0, 0)

    clock = pygame.time.Clock()
    crashed = False
    orb_image = pygame.image.load('SpelunkOrb.png')
    bow_image = pygame.image.load('SpelunkBow.png')

    x = 0
    y = 0

    i = 0
    while not crashed:
        game_display.fill(black)

        if COUNT > 0:
            game_display.blit(orb_image, (x, y + 55))
        if COUNT > 1:
            game_display.blit(orb_image, (x, y + 48 + 55))
        if COUNT > 2:
            game_display.blit(orb_image, (x, y + 96 + 55))

        if BOW_STATE == 1:
            game_display.blit(bow_image, (x + 20, y))
        elif BOW_STATE == 2 and i % 4 == 0:
            game_display.blit(bow_image, (x + 20, y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        pygame.display.update()
        clock.tick(60)
        i = i + 1

    pygame.joystick.quit()
    pygame.quit()
    quit()


def cycle_count():
    global COUNT
    if COUNT > 2:
        COUNT = -1
    COUNT = COUNT + 1


def cycle_bow():
    global BOW_STATE
    if BOW_STATE > 1:
        BOW_STATE = -1
    BOW_STATE = BOW_STATE + 1


if __name__ == '__main__':
    import pythoncom

    main()
    pythoncom.PumpMessages()
    input('Press ENTER to exit')
