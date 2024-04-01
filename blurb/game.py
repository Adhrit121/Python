import pygame
import time
from tkinter import *
#https://bit.ly/3o0OLfu
#Q807H
pygame.init()
def dialog(message):
    root = Tk()
    root.attributes("-alpha", 0)
    root.overrideredirect(1)
    root.attributes("-topmost", 1)
def get_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
def show_message(message, size=30,side=""):
    if message.strip()=="":
        message="⠀"
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, size)
    text = font.render(message, True, BLACK)
    text_rect = text.get_rect()
    box_width = text_rect.width + 100
    box_height = text_rect.height + 75
    box_rect = pygame.Rect((0, 0), (box_width, box_height))
    box_rect.center = screen.get_rect().center
    pygame.draw.rect(screen, (255, 255, 255), box_rect)
    screen.blit(text, (box_rect.x + 100/2, box_rect.y + 75/2))
def show_message_old(message):
    dialog(message)

# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 550
BORDER_THICKNESS = 13
show_inventory = False
interact_desk=False
interact_tv=False
inventory=[]
screen_width = SCREEN_WIDTH
screen_height = SCREEN_HEIGHT

#show_tv
tv_width = 600
tv_height = 450
tv_screen = pygame.Surface((tv_width, tv_height))
tv_screen.fill((255, 255, 255))
button_width = 100
button_height = 50
button_x = (screen_width - button_width) // 2+(screen_width - button_width)//6
button_y = (screen_height - button_height) // 2+(screen_height - button_height) // 4
return_button = pygame.Rect(button_x, button_y, button_width, button_height)
font = pygame.font.Font(None, 36)

#show_comp
comp_width = 600
comp_height = 550
comp_screen = pygame.Surface((comp_width, comp_height))
comp_screen.fill((255, 255, 255))
button_width = 100
button_height = 50
button_x = (screen_width - button_width) // 2+150
button_y = (screen_height - button_height) //2 +110
return_butt = pygame.Rect(button_x, button_y, button_width, button_height)
font = pygame.font.Font(None, 36)
input_rect = pygame.Rect(345, 176, 250, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color_white = pygame.Color(255, 255, 255)  # Light shade of white
color = color_white
active = False


# Define constants for the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (150, 70, 0)
CLEAR_WHITE=(255, 255, 255, 100)
INVENTORY_WIDTH = SCREEN_WIDTH
INVENTORY_HEIGHT = 500


# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("")
inventory_surface = pygame.Surface((INVENTORY_WIDTH, INVENTORY_HEIGHT))
inventory_surface.fill(CLEAR_WHITE)

# Load the background image and player sprite
background = pygame.image.load("images/floor_large_test.png")
background = pygame.transform.scale(background, (int(background.get_width()/4), int(background.get_height()/4)))
player_image = pygame.image.load("images/player_up.png").convert_alpha()
player_up_image = pygame.image.load("images/player_up.png").convert_alpha()
player_down_image = pygame.image.load("images/player_down.png").convert_alpha()
player_left_image = pygame.image.load("images/player_left.png").convert_alpha()
player_right_image = pygame.image.load("images/player_right.png").convert_alpha()
player_width, player_height = player_image.get_size()
remote = pygame.Rect(425, 37, 16, 20)
butn=pygame.Rect(676,283,91-76,99-83)
comp=pygame.Rect(854,418,98-54,51)
printer_s=pygame.Rect(931,342,988-931,406-342)
printer_button=pygame.Rect(367,218,382-367,234-219)
door_button = pygame.Rect(786, 13, 960 - 786, 36 - 13)
desk_button=pygame.Rect(786, 13, 960 - 786, 36 - 13)


# Load object images
desk = pygame.image.load("images/desk.png").convert_alpha()
desk = pygame.transform.scale(desk, (int(desk.get_width()*4), int(desk.get_height()*4)))
desk_items=['paper']
tv = pygame.image.load("images/tv.png").convert_alpha()
tv = pygame.transform.scale(tv, (int(tv.get_width()*5), int(tv.get_height()*4)))
table = pygame.image.load("images/table.png").convert_alpha()
table = pygame.transform.scale(table, (int(table.get_width()*7), int(table.get_height()*7)))
door = pygame.image.load("images/door_test.png").convert_alpha()
door = pygame.transform.scale(door, (int(door.get_width()*6), int(door.get_height()*6)))

objects=[]
objects_x=[]
objects_y=[]
# Set the initial position of objects


#tv
tv_x = 50
tv_y = -115
objects.append(tv)
objects_x.append(tv_x)
objects_y.append(tv_y)
#desk
desk_x = -100
desk_y = -20
objects.append(desk)
objects_x.append(desk_x)
objects_y.append(desk_y)
#table
table_x = 582
table_y = 118
objects.append(table)
objects_x.append(table_x)
objects_y.append(table_y)
#door
door_x =600
door_y =-228
objects.append(door)
objects_x.append(door_x)
objects_y.append(door_y)


# Set the player's initial position
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

# Set up a clock to manage the game's frame rate
clock = pygame.time.Clock()

#Set up different parts of code:
openedDesk=False
pt1=True
show_pt1='Hello Search for clues in the room and find the key to enter next level'
pt_2=False
show_pt2='''Hello
        Search for clues in the room and find the key to enter next level'''
pinished=False
show_pinished='''Hello
        Search for clues in the room and find the key to enter next level'''
set_pass=False
stay=False
found_paper=False
show_tv=False
tv_open=False
comp_open=False
show_comp_pass=False
show_tv_pass=False
show_comp=False
show_printer=False
printed=False
pass_correct=False
printer_on=False
printer_button_clickable=False
start_printer=False
dones=False
do_not_draw=False
door_click=False
desk_click=False

found_key=False


# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            if door_button.collidepoint(event.pos):
                print("Door clicked")
                door_click=True
            if remote.collidepoint(event.pos):
                print("Found remote")
                show_tv=True
            if show_tv and not show_comp and return_button.collidepoint(event.pos) :
                show_tv = False
            if butn.collidepoint(event.pos) and tv_open==True:
                show_tv_pass=True
            if comp.collidepoint(event.pos):
                print("Starting computer...")
                entered=" "
                show_comp=True
            if show_comp and return_butt.collidepoint(event.pos):
                show_comp=False
            if not show_printer and printer_s.collidepoint(event.pos):
                show_printer=True
                print("Printer view")
            if show_comp and input_rect.collidepoint(event.pos):
                active = True
                color = color_active if active else color_inactive
            if show_printer and printer_button.collidepoint(event.pos):
                print("Started printer")
                start_printer=True
            if show_printer and return_butt.collidepoint(event.pos):
                show_printer=False
            else:
                active = False
                color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i and not active:
                show_inventory = True

            if active:
                try:
                    stringed=int(str(entered_text).strip())
                    passes=True
                except:
                    passes=False
                if event.key == pygame.K_RETURN:
                    print(entered_text)
                    if passes and stringed==1502:
                        pass_correct=True
                    else:
                        print("Wrong password")
                elif event.key == pygame.K_BACKSPACE:
                    try:
                        last=entered_text[-1]
                        entered_text=entered_text.rstrip(last)
                    except:
                        pass
                    if len(entered_text)==4:
                        print(entered_text)
                        try:
                            test=int(entered_text)
                        except:
                            test=str(entered_text)
                        if test==1502:
                            pass_correct=True
                        else:
                            print("Wrong password")
                else:
                    key_name = pygame.key.name(event.key)
                    if len(key_name)<3:
                        entered_text=entered_text+key_name
                    else:
                        print("KEY",key_name,"NOT SUPPORTED")
                    if len(entered_text)>15:
                        entered_text=""
                    if len(entered_text)==4:
                        print(entered_text)
                        try:
                            test=int(entered_text)
                        except:
                            test=str(entered_text)
                        if test==1502:
                            pass_correct=True
                        else:
                            print("Wrong password")
                            start_time = pygame.time.get_ticks()  # get current time in milliseconds
                            elapsed_time = 0
                            show_message("Wrong password")
                            while elapsed_time < 1500:  # 1000 milliseconds = 1 seconds
                                elapsed_time = pygame.time.get_ticks() - start_time
                                pygame.display.update()
                            
                    print(entered_text)
        if event.type == pygame.KEYUP:
            if interact_desk and event.key == pygame.K_x :
                pass
            elif event.key == pygame.K_x:
                show=False
            if event.key == pygame.K_i:
                show_inventory = False





    # Move the player based on keyboard input
    keys = pygame.key.get_pressed()
    player_direction = None
    if keys[pygame.K_UP]:
        player_y -= 5
        if player_y < 0:
            player_y = 0
        player_image = player_up_image
    elif keys[pygame.K_DOWN]:
        player_y += 5
        if player_y > SCREEN_HEIGHT - player_height:
            player_y = SCREEN_HEIGHT - player_height
        player_image = player_down_image
    else:
        player_image = player_image

    if keys[pygame.K_LEFT]:
        player_x -= 5
        if player_x < 0:
            player_x = 0
        player_image = player_left_image
    elif keys[pygame.K_RIGHT]:
        player_x += 5
        if player_x > SCREEN_WIDTH - player_width:
            player_x = SCREEN_WIDTH - player_width
        player_image = player_right_image


    # Draw the game world
    screen.blit(background, (0, 0))




    if start_printer:
        printer_on=True
    else:
        printer_on=False


    for object in objects:
        loc=0
        loc=objects.index(object)
        object_x=objects_x[loc]
        object_y=objects_y[loc]
        screen.blit(object, (object_x, object_y))
    border_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.draw.rect(screen, BROWN, border_rect, BORDER_THICKNESS)
    if show_inventory:
        INVENTORY_X = 0
        INVENTORY_Y = 375
        screen.blit(inventory_surface, (INVENTORY_X, INVENTORY_Y))
        x=500
        if len(inventory)>0:
            for item in inventory:
                item_image = pygame.image.load("images/"+item+".png").convert_alpha()
                item_image = pygame.transform.scale(item_image, (int(item_image.get_width()/3), int(item_image.get_height()/3)))
                inventory_surface.blit(item_image, (x, 5))
                x=x+150
        else:
            font = pygame.font.Font(None, 27)
            text = font.render("Search for clues by clicking on objects", True, BLACK)
            inventory_surface.blit(text, (450,25))
            text = font.render("Using the clues, unlock the door to escape", True, BLACK)
            inventory_surface.blit(text, (450,50))
            text = font.render("Try clicking on the TV remote", True, BLACK)
            inventory_surface.blit(text, (450,75))

    desk_distance = get_distance(player_x, player_y, desk_x, desk_y)
    if desk_distance < 200:
        interact_desk = True
        show_message("Click 'x' to open desk",20)
    else:
        interact_desk = False
    if stay and not found_paper:
        start_time = pygame.time.get_ticks()  # get current time in milliseconds
        elapsed_time = 0
        shows=0
        found_paper=True
        while elapsed_time < 2000:  # 1000 milliseconds = 1 seconds
            elapsed_time = pygame.time.get_ticks() - start_time
            pygame.display.update()
        start_time = pygame.time.get_ticks()
        elapsed_time = 0
        show_message("Found a piece of paper")
        while elapsed_time < 3000:  # 1000 milliseconds = 1 seconds
            elapsed_time = pygame.time.get_ticks() - start_time
            pygame.display.update()
        start_time = pygame.time.get_ticks()
        elapsed_time = 0
        paper = pygame.image.load("images/paper.png").convert_alpha()
        paper = pygame.transform.scale(paper, (int(paper.get_width()), int(paper.get_height())))
        show_message("Paper was added to inventory")
        while elapsed_time < 3000:  # 1000 milliseconds = 1 seconds
            elapsed_time = pygame.time.get_ticks() - start_time
            pygame.display.update()  # update screen during countdown
        objects.remove(desk)
        objects_x.remove(desk_x)
        objects_y.remove(desk_y)
        desk = pygame.image.load("images/desk.png").convert_alpha()
        desk = pygame.transform.scale(desk, (int(desk.get_width()*4), int(desk.get_height()*4)))
        desk_x = -100
        desk_y = -70
        objects.append(desk)
        objects_x.append(desk_x)
        objects_y.append(desk_y)
        stay=False
    elif found_paper and stay:
        start_time = pygame.time.get_ticks()  # get current time in milliseconds
        elapsed_time = 0
        show_message("Nothing inside")
        while elapsed_time < 2000:  # 1000 milliseconds = 1 seconds
            elapsed_time = pygame.time.get_ticks() - start_time
            pygame.display.update()

    if show_tv:
        tv_open=True
        tv_x = (screen_width - tv_width) // 2
        tv_y = (screen_height - tv_height) // 2
        #screen.blit(tv_screen, (tv_x, tv_y))
        pygame.draw.rect(screen, (169,169,169), return_button)
        if show_tv_pass==True:
            new_tv_image = pygame.image.load('images/tv-view-done.png')
        else:
            new_tv_image = pygame.image.load('images/tv-view.png')
        original_width, original_height = new_tv_image.get_size()
        text = font.render("Ok", True, (0,0,0))
        text_x = button_x + (button_width - text.get_width()) // 2
        text_y = button_y + (button_height - text.get_height()) // 2
        screen.blit(text, (text_x, text_y))
        scale_factor = 8
        new_tv_width, new_tv_height = original_width * scale_factor, original_height * scale_factor
        new_tv_image = pygame.transform.scale(new_tv_image, (new_tv_width, new_tv_height))
        tv_x = (screen_width - new_tv_width) // 2
        tv_y = (screen_height - new_tv_height) // 2
        screen.blit(new_tv_image, (tv_x, tv_y))
    else:
        # Hide the TV screen
        tv_open=False
        tv_screen.fill((255, 255, 255))

    if show_comp:
        comp_open = True
        active=True
        if not show_comp_pass:
            computer = pygame.image.load("images/comp.png").convert_alpha()
            comp_x = (screen_width - computer.get_width()) // 2
            comp_y = (screen_height - computer.get_height()) // 2
            #screen.blit(comp_screen, (comp_x, comp_y))
            pygame.draw.rect(screen, (169,169,169), return_butt)
            original_width, original_height = computer.get_size()
            text = font.render("Ok", True, (0,0,0))
            text_x = button_x + (button_width - text.get_width()) // 2
            text_y = button_y + (button_height - text.get_height()) // 2
            screen.blit(text, (text_x, text_y))
            txt_surface = font.render(str(entered_text), True, color)
            pygame.draw.rect(screen, color, input_rect, 2)
            #screen.blit(txt_surface, (350, 195))

            if pass_correct:
                print(printer_on)
                do_not_draw=True
                if printer_on:
                    printer_on_so_display_last=True
                    computer = pygame.image.load("images/comp-printing.png").convert_alpha()
                    set_pass=True
                    printed=True
                    shower=True
                    computer = pygame.transform.scale(computer, (int(computer.get_width()*7), int(computer.get_height()*7)))
                    comp_x = (screen_width - computer.get_width()) // 2
                    comp_y = (screen_height - computer.get_height()) // 2
                    start_time = pygame.time.get_ticks()  # get current time in milliseconds
                    elapsed_time = 0
                    screen.blit(computer, (comp_x, comp_y))
                    while elapsed_time < 3500:  # 1000 milliseconds = 1 seconds
                        elapsed_time = pygame.time.get_ticks() - start_time
                        pygame.display.update()
                    pass_correct=False
                    entered_text=""
                    dones=True
                else:
                    set_pass=False
                    computer = pygame.image.load("images/comp-error.png").convert_alpha()
                    printed=False
                    start_time = pygame.time.get_ticks()  # get current time in milliseconds
                    elapsed_time = 0
                    shower=False
                    computer = pygame.transform.scale(computer, (int(computer.get_width()*7), int(computer.get_height()*7)))
                    comp_x = (screen_width - computer.get_width()) // 2
                    comp_y = (screen_height - computer.get_height()) // 2
                    screen.blit(computer, (comp_x, comp_y))
                    while elapsed_time < 3500:  # 1000 milliseconds = 1 seconds
                        elapsed_time = pygame.time.get_ticks() - start_time
                        pygame.display.update()
                    pass_correct=False
                    entered_text=""
                    dones=False
                print(printer_on)



        else:
            do_not_draw=False
            computer = pygame.image.load("images/comp-done.png").convert_alpha()
        if dones:
            computer = pygame.image.load("images/comp-done.png").convert_alpha()
            pass_correct=False
        computer = pygame.transform.scale(computer, (int(computer.get_width()*7), int(computer.get_height()*7)))
        comp_x = (screen_width - computer.get_width()) // 2
        comp_y = (screen_height - computer.get_height()) // 2
        screen.blit(computer, (comp_x, comp_y))
        pygame.draw.rect(screen, (169,169,169), return_butt)
        text = font.render("Ok", True, (0,0,0))
        text_x = button_x + (button_width - text.get_width()) // 2
        text_y = button_y + (button_height - text.get_height()) // 2
        screen.blit(text, (text_x, text_y))
        txt_surface = font.render(str(entered_text), True, color)
        #pygame.draw.rect(screen, color, input_rect, 2)
        screen.blit(txt_surface, (350,195))
    else:
        entered_text=""
        comp_open=False
        if set_pass:
            show_comp_pass=True
    if show_printer:
        if not printer_on:
            printer = pygame.image.load("images/printer.png").convert_alpha()
            print_x = (screen_width - printer.get_width()) // 2
            print_y = (screen_height - printer.get_height()) // 2
        else:
            printer = pygame.image.load("images/printer-open.png").convert_alpha()
            print_x = (screen_width - printer.get_width()) // 2
            print_y = (screen_height - printer.get_height()) // 2
        if printed:
            printer = pygame.image.load("images/printed.png").convert_alpha()
            print_x = (screen_width - printer.get_width()) // 2
            print_y = (screen_height - printer.get_height()) // 2
        #if printer_button
        printer = pygame.transform.scale(printer, (int(printer.get_width()*7), int(printer.get_height()*7)))
        print_x = (screen_width - printer.get_width()) // 2
        print_y = (screen_height - printer.get_height()) // 2
        screen.blit(printer, (print_x, print_y))
        pygame.draw.rect(screen, (169,169,169), return_butt)
        text = font.render("Ok", True, (0,0,0))
        text_x = button_x + (button_width - text.get_width()) // 2
        text_y = button_y + (button_height - text.get_height()) // 2
        screen.blit(text, (text_x, text_y))

    if door_click==True:
        if found_key==True:
            #unlock
            print("Game over(you won)")
            start_time = pygame.time.get_ticks()  # get current time in milliseconds
            elapsed_time = 0
            show_message("You won!")
            while elapsed_time < 550:  # 1000 milliseconds = 1 seconds
                elapsed_time = pygame.time.get_ticks() - start_time
                pygame.display.update()  # update screen during countdown
        else:
            start_time = pygame.time.get_ticks()  # get current time in milliseconds
            elapsed_time = 0
            show_message("You dont have the key")
            while elapsed_time < 4500:  # 1000 milliseconds = 1 seconds
                elapsed_time = pygame.time.get_ticks() - start_time
                pygame.display.update()  # update screen during countdown
            start_time = pygame.time.get_ticks()  # get current time in milliseconds
            elapsed_time = 0
            show_message("Find the key and try opening the door again")
            while elapsed_time < 4500:  # 1000 milliseconds = 1 seconds
                elapsed_time = pygame.time.get_ticks() - start_time
                pygame.display.update()  # update screen during countdown
        door_click=False


    pygame.display.flip()

    # Limit the game's frame rate to 60 FPS
    clock.tick(60)

# Clean up the game
pygame.quit()
