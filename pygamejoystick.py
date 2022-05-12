import pygame

pygame.init()

pygame.joystick.init()
init = pygame.joystick.get_init()
joy = pygame.joystick.Joystick(0)

print(joy.get_name())

# joy.rumble(11, 11, 2)

done = False
while not done:
    for event in pygame.event.get():  # User did something.
        if event.type == pygame.QUIT:  # If user clicked close.
            done = True  # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
