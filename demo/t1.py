import pygame
pygame.init()

screen_width,screen_height=750,750
screen_background_color=(0,0,0)

win= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("First Game")
coin_x, coin_y, coin_r = 50,50,30
coin_color=(255,0,0)
vel = 10

# Physcis variables
vel_y = 0
gravity=1.5
jump_s= -30
is_jumping= False

clock = pygame.time.Clock()
run=True
while run:
  clock.tick(30)  # Use Clock instead of delay for consistent frame pacing

  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      run=False
  # End for
 
  keys = pygame.key.get_pressed()

  if keys[pygame.K_ESCAPE]:
    run=False

  # Horizontal movement (available in both modes)
  if keys[pygame.K_LEFT]:
    coin_x-=vel
    if coin_x<= coin_r:
      coin_x= coin_r
  if keys[pygame.K_RIGHT]:
    coin_x+=vel
    if coin_x>= screen_width-coin_r:
      coin_x= screen_width-coin_r

  # Trigger jump mode
  if keys[pygame.K_SPACE] and not is_jumping:
    vel_y = jump_s
    is_jumping = True

  if not is_jumping:
    # Free-roam vertical controls
    if keys[pygame.K_UP]:
      coin_y-= vel
      if coin_y<=coin_r:
        coin_y=coin_r
    if keys[pygame.K_DOWN]:
      coin_y+=vel
      if coin_y>=screen_height-coin_r:
        coin_y=screen_height-coin_r
  else:
    # Move first, then apply gravity for the next frame
    coin_y += vel_y
    vel_y += gravity

    # if ground collision -> exit jump mode, zero velocity, set y to ground level
    if coin_y>=screen_height-coin_r:
      coin_y=screen_height-coin_r
      vel_y=0
      is_jumping = False

    # Celling collision -> bounce down, velocity = 0
    if coin_y<=coin_r:
      coin_y=coin_r 
      vel_y= abs(vel_y) / 2

  # End if not is_jumping:
         
  
  win.fill(screen_background_color)
  pygame.draw.circle(win,coin_color,(int(coin_x),int(coin_y)),coin_r)
  pygame.display.update()

# end while
pygame.quit()



