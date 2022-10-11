import pygame
pygame.init()
screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flight game")

sprite_sheet_image = pygame.image.load("heli1.png")
def get_image(sheet,width,height):
    sprite_sheet_image = pygame.Surface(width,height)
    sprite_sheet_image.blit(sheet,(0,0),(0,0,width,height))
    return sprite_sheet_image
BG = (255, 255, 255)
black = (0,0,0)

def get_image(sheet,frame,width,height,scale,colour):
    image = pygame.Surface((width,height))
    image.blit(sheet, (0,0), (frame * width,0,width,height))
    image = pygame.transform.scale(image,(width * scale,height * scale))
    image.set_colorkey(colour)
    return image

frame_0 = get_image(sprite_sheet_image,0, 64, 64,1,black)
frame_1 = get_image(sprite_sheet_image,0, 64, 64,1,black)

run = True
while run:
    #update background
    screen.fill(BG)

    #show frame image
    screen.blit(frame_0,(0,0))
    screen.blit(frame_1, (100,0))
    #display image
    screen.blit(sprite_sheet_image,(0,0))
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        pygame.display.update()

pygame.quit()
