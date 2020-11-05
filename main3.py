from __future__ import print_function
import pyWinhook as pyHook
import pygame

COUNT = 1
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
    pygame.joystick.init()

    print(pygame.joystick.get_count())

    joystick = pygame.joystick.Joystick(1)
    joystick.init()

    display_width = 150
    display_height = 180

    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Lunky Helper')

    black = (0, 0, 0)
    white = (255, 255, 255)

    clock = pygame.time.Clock()
    crashed = False
    orb_image = pygame.image.load('hiclipart.com.png')

    x = 0
    y = 0

    while not crashed:
        game_display.fill(black)

        if COUNT > 0:
            game_display.blit(orb_image, (x, y))
        if COUNT > 1:
            game_display.blit(orb_image, (x, y + 60))
        if COUNT > 2:
            game_display.blit(orb_image, (x, y + 120))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        #     elif event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             COUNT = cycle_count(COUNT)
        #     elif event.type == pygame.JOYBUTTONDOWN:
        # print(event.dict, event.joy, event.button, 'pressed')
        # if joystick.get_button(4):
        #     COUNT = cycle_count(COUNT)

        pygame.display.update()
        clock.tick(60)

    pygame.joystick.quit()
    pygame.quit()
    quit()


def cycle_count():
    global COUNT
    if COUNT > 2:
        COUNT = -1
    COUNT = COUNT + 1


if __name__ == '__main__':
    import pythoncom

    main()
    pythoncom.PumpMessages()
