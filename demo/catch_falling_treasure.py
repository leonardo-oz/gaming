import pygame 
from health_bar import Heath_Bar_Heart
from falling_object import Bomb,Aid,Treasure
from ninja_config import NinjaState
from ninja import Ninja

def main():
    pygame.init()
    pygame.mixer.init()

    # ============== Game Setup ===========================================
    screen_width, screen_height = 1200,600
    screen_surface = pygame.display.set_mode((screen_width, screen_height))
    
    sky_surface_raw = pygame.image.load("pics/sky.png")
    _, sky_raw_height = sky_surface_raw.get_size()
    sky_surface = pygame.transform.scale(sky_surface_raw, (screen_width, sky_raw_height))
    grass_surface_raw = pygame.image.load("pics/grass.png")
    grass_surface= pygame.transform.scale(grass_surface_raw, (screen_width,screen_height-sky_raw_height))

    # =========================================================================
    # PHASE 1: PRE-LOAD & SETUP RESOURCES (RUNS ONCE AT STARTUP)
    # =========================================================================
    bomb_hit_sound = pygame.mixer.Sound("sounds/cartoon_music-bomb-explosion-large-amp-short-517328.mp3")
    aid_hit_sound = pygame.mixer.Sound("sounds/heal.mp3")
    treasure_hit_sound= pygame.mixer.Sound("sounds/coin.mp3")



    # Create a Heath Bar Object
    heart = pygame.image.load("pics/heart.png").convert_alpha()
    heart_surface= pygame.transform.scale(heart,(20,20))
    h= Heath_Bar_Heart(heart_surface,20,10)

    # Create a ninja object
    ninja_width,ninja_height= 80,100
    nj_file_dic = {
        NinjaState.STANDING: "nj_stand.png",
        NinjaState.RUNNING_RIGHT: "nj_run_right.png",
        NinjaState.RUNNING_LEFT: "nj_run_left.png",
        NinjaState.MEDITATING: "nj_meditaing.png",
        NinjaState.BRUCE_LEE: "nj_brucelee.png",
        NinjaState.DEAD: "nj_dead.png"

    }
    nj_ini_rec = pygame.Rect(screen_width//2,
                            #  sky_raw_height-ninja_height//2+3,
                            screen_height-ninja_height-10,
                            ninja_width,ninja_height)
    ninja_vel=5
    ninja = Ninja(nj_ini_rec,nj_file_dic,vel=ninja_vel)

    bomb_width, bomb_height = 50,50
    aid_width, aid_height = 50,50
    treasure_width, treasure_height = 50,50

    # Load & Scalar Surface lists
    bomb_surfaces = [
        pygame.transform.scale(pygame.image.load(f"pics/bomb_{i}.png"),(bomb_width, bomb_height))
        for i in range(1,4)
    ]
    aid_surfaces = [
        pygame.transform.scale(
            pygame.image.load("pics/aid.png").convert_alpha(), (aid_width, aid_height)
        )
    ]
    treasure_surfaces = [
        pygame.transform.scale(
            pygame.image.load(f"pics/treasure_{i}.png").convert_alpha(), (treasure_width, treasure_height)
        )
        for i in range(1, 4)
    ]

    exposive_width, explosive_height = 50,50
    explosive_frames = [
        pygame.transform.scale(pygame.image.load(f"pics/explosive_{i}.png"),(exposive_width, explosive_height))
        for i in range(1,4) # Outer Loop for image indexing
        for _ in range(4)   # Inner Loop for repeat
    ]


    # ============= create gaming object groups ============
    ninja_group = pygame.sprite.GroupSingle(ninja)
    explosive_group = pygame.sprite.Group()
    falling_objects_group = pygame.sprite.Group()

    # ================ Register Class-Level Resource ==============
    Bomb.setup_resources(bomb_surfaces,bomb_hit_sound,explosive_frames,explosive_group)
    Aid.setup_resources(aid_surfaces,aid_hit_sound)
    Treasure.setup_resources(treasure_surfaces,treasure_hit_sound)


    # =========================================================================
    # PHASE 2: INSTANTIATING OBJECTS (RUNS CONTINUOUSLY IN GAME LOOP)
    # ========================================================================
    # ========= Create Gaming Events ================
    SPAWN_BOMB_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_BOMB_EVENT,2000)
    SPAWN_AID_EVENT = pygame.USEREVENT +2 
    pygame.time.set_timer(SPAWN_AID_EVENT, 5000)
    SPAWN_TREASURE_EVENT = pygame.USEREVENT +3 
    pygame.time.set_timer(SPAWN_TREASURE_EVENT, 3000)


    # ========= Play Backgorund music ============
    pygame.mixer.music.load("sounds/background_ninja.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)
    
    clock= pygame.time.Clock()
    fps = 60
    running = True

    while running:
        clock.tick(fps)  # Use Clock instead of delay for consistent frame pacing
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == SPAWN_BOMB_EVENT:
                falling_objects_group.add(Bomb(screen_width,bomb_width,bomb_height))
                # print("Bomb event triggered")
            elif event.type == SPAWN_AID_EVENT:
                falling_objects_group.add(Aid(screen_width,aid_width,aid_height))
            elif event.type == SPAWN_TREASURE_EVENT:
                falling_objects_group.add(Treasure(screen_width,treasure_width,treasure_height))
            
            ninja.handle_events(event)
        # End for for event in pygame.event.get():

        # State Update
        ninja_group.update(screen_width)
        falling_objects_group.update(screen_height)
        explosive_group.update()

        # Collision Logic (Only process if player is alive)
        if ninja.is_alive:
            hits = pygame.sprite.spritecollide(ninja, falling_objects_group, dokill = True )
            for hit in hits:
                hit.apply_effect(ninja)

        # Render
        screen_surface.blit(sky_surface,(0,0))
        screen_surface.blit(grass_surface, (0, sky_raw_height))

        h.draw(screen_surface,ninja.num_of_lives)
        ninja_group.draw(screen_surface)
        falling_objects_group.draw(screen_surface)
        explosive_group.draw(screen_surface)

        pygame.display.update()
    # End while
    pygame.quit()
# End main method

if __name__ == "__main__":
    main()