import random # for generating random numbers
import sys # We wil use sys.exit to exit the program
import pygame
from pygame.locals import* # These are basic pygame imports used for every game

#  Global variables fot the game:
FPS = 32 # frames per seconds this means 32 images are shown to the user in One seconds so that usser doesnot feel any change
# Game is changing of the background bird is at same position but background is changing i.e iamges are changing
SCREENWIDTH = 289
SCREENHEIGHT = 511 # THIS  is mobile phone parameters You can customize it to get full screen flappy Bird Game
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT)) #Initialize a window or screen for display means it will give me screen of sizes as given by me
GROUNDY = SCREENHEIGHT*0.8 # GRAOUNDY  is that my ground image wil cover 80%
GAME_SPRITES = {}  # This is dictionary I am passing objects
GAME_SOUNDS = {}  # Images and the sound is the heart of game we ahve to paly music and render images
PLAYER = 'gallery/sprites/bird.png' # WE HAVE to give relative or absolute path of these
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'

# If You run program from this file then only it will run or else it will just give imports
if __name__ ==  "__main__":
    # this will be the main point from where our game will start
    pygame.init() # Intialize all pygame's module / jsut like applet program with lifecycle start sleep etc
    FPSCLOCK = pygame.time.Clock()  #it gives me the control of how amny images/frames I am rendering to the user , it wil be less than this number or equal to not greater than the ticker
    pygame.display.set_caption('Flappy Bird by Pooja Bhagat') # it will set caption for my game 
    # Game Sprites are numbers i.e it is tuple having images of numbers 
    GAME_SPRITES['numbers'] = (
        pygame.image.load('gallery/sprites/0.png').convert_alpha(), 
        pygame.image.load('gallery/sprites/1.png').convert_alpha(), # convert aplha will render iamges faster means it increase games optimisation/ Speed of images to visble on screen
        pygame.image.load('gallery/sprites/2.png').convert_alpha(), # Convert alpha will learn more in image processing
        pygame.image.load('gallery/sprites/3.png').convert_alpha(), # convert aplha paly will the pixels of the images on rendering to faster image blitering 
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),  # Biltering means showing faster showing iamges
        pygame.image.load('gallery/sprites/5.png').convert_alpha(), 
        pygame.image.load('gallery/sprites/6.png').convert_alpha(), 
        pygame.image.load('gallery/sprites/7.png').convert_alpha(), 
        pygame.image.load('gallery/sprites/8.png').convert_alpha(), 
        pygame.image.load('gallery/sprites/9.png').convert_alpha(), 

    )

    GAME_SPRITES['message'] = pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (
    pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180), # This will rotate the iamge in 180 i.e. Rotated Image
    pygame.image.load(PIPE).convert_alpha() # Straight Image
    ) # In game_spirtes['pipe'] we have tuple in that there are two images , One is Striaght pipe and other is rotated pipe

    # Game sounds # we use mixer so that we can use .play to qickly paly the music any audio
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert_alpha()
    GAME_SPRITES['palyer'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen() # when user clicks on any key then it will take user to the welcome page message page # show welcome screen to the user until he presses a button
        mainGame() # This is the main game function


