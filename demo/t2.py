import pygame
pygame.init()

screen_width, screen_height = 800,600
screen_surface = pygame.display.set_mode((screen_width, screen_height))

sky_surface_raw = pygame.image.load("pics/sky.png")
sky_raw_width, sky_raw_height = sky_surface_raw.get_size()
sky_surface = pygame.transform.scale(sky_surface_raw, (screen_width, sky_raw_height))

grass_surface_raw = pygame.image.load("pics/grass.png")
grass_surface= pygame.transform.scale(grass_surface_raw, (screen_width,screen_height-sky_raw_height))
ninja_standing= pygame.image.load("pics/nj_stand.png").convert_alpha()

ninja_width,ninja_height= 80,100

ninja_run_right= pygame.image.load("pics/nj_run_right.png").convert_alpha()
ninja_run_right_surface= pygame.transform.scale(ninja_run_right,(ninja_width,ninja_height))

ninja_run_left= pygame.image.load("pics/nj_run_left.png").convert_alpha()
ninja_run_left_surface= pygame.transform.scale(ninja_run_left,(ninja_width,ninja_height))

ninja_standing_surface= pygame.transform.scale(ninja_standing,(ninja_width,ninja_height))

ninja_sit = pygame.image.load("pics/nj_meditaing.png").convert_alpha()
ninja_sit_surface= pygame.transform.scale(ninja_sit,(ninja_width,ninja_height))

ninja_brucelee= pygame.image.load("pics/nj_brucelee.png").convert_alpha()
ninja_brucelee_surface= pygame.transform.scale(ninja_brucelee,(ninja_width,ninja_height))
vel=5
clock= pygame.time.Clock()

current_ninja_surface= ninja_standing_surface
current_ninja_rect= current_ninja_surface.get_rect(center=(screen_width//2, sky_raw_height-ninja_height//2+3))


running = True
while running:
  clock.tick(60)  # Use Clock instead of delay for consistent frame pacing
  # event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        current_ninja_surface= ninja_run_left_surface
        print("Left Key Down pressed:", event.key)
      elif event.key == pygame.K_RIGHT:
        current_ninja_surface= ninja_run_right_surface
        print("Right Key Down pressed:", event.key)
      elif event.key == pygame.K_DOWN:
          current_ninja_surface= ninja_sit_surface
          print("Down Key pressed:", event.key)


    if event.type == pygame.KEYUP:
      print("Key Up pressed:", event.key)
      current_ninja_surface= ninja_standing_surface


    if event.type == pygame.MOUSEBUTTONDOWN:
      print("Mouse Button Down pressed:", event.button)
      if current_ninja_rect.collidepoint(event.pos):
        current_ninja_surface= ninja_brucelee_surface


    if event.type == pygame.MOUSEBUTTONUP:
      print("Mouse Button Up pressed:", event.button)
      current_ninja_surface= ninja_standing_surface


  # end for loop for events


  # hanldle key presses for movement
  keys = pygame.key.get_pressed()
  
  # Horizontal movement (available in both modes)
  if keys[pygame.K_LEFT]:
    current_ninja_rect.left -= vel
    if current_ninja_rect.left <= 0:
      current_ninja_rect.left = 0

    print("Left pressed:", current_ninja_rect.left)
    
  if keys[pygame.K_RIGHT]:
    current_ninja_rect.right += vel
    if current_ninja_rect.right>= screen_width:
      current_ninja_rect.right = screen_width

    print("Right pressed:", current_ninja_rect.right)
  # print(current_ninja_rect.left, current_ninja_rect.right)


    


  screen_surface.blit(sky_surface, (0,0))
  screen_surface.blit(grass_surface, (0,sky_raw_height))
  screen_surface.blit(current_ninja_surface, current_ninja_rect)
  pygame.display.update()
# End while