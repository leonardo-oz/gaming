import pygame
pygame.init()

width,height=750,750

win= pygame.display.set_mode((width,height))
pygame.display.set_caption("First Game")
coin_x, coin_y, coin_r = 50,50,30
vel = 10

# Physcis variables
vel_y = 0
gravity=1.5
jump_s= -30
is_jumping= False

run=True
while run:
  pygame.time.delay(50)

  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      run=False
  # End for
 
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    coin_x-=vel
    if coin_x<= coin_r:
      coin_x= coin_r
  if keys[pygame.K_RIGHT]:
    coin_x+=vel
    if coin_x>= width-coin_r:
      coin_x= width-coin_r

  if not is_jumping:
    if keys[pygame.K_UP]:
      coin_y-= vel
      if coin_y<=coin_r:
        coin_y=coin_r
    if keys[pygame.K_DOWN]:
      coin_y+=vel
      if coin_y>=height-coin_r:
        coin_y=height-coin_r

  # simulate jumping 
  if keys[pygame.K_SPACE] and not is_jumping:
    vel_y = jump_s
    is_jumping = True

  if is_jumping:
    vel_y += gravity
    coin_y += vel_y
    if coin_y>=height-coin_r:
      coin_y=height-coin_r
      is_jumping = False
  else:
    vel_y = vel
      


  win.fill((0,0,0))
  pygame.draw.circle(win,(255,0,0),(coin_x,coin_y),coin_r)
  # print(f"x: {coin_x}, y:{coin_y}")
  pygame.display.update()




# end while
pygame.quit()



