
from pygame import *
from random import *
from math import *
import tkinter as tk
from tkinter import *
from tkinter import filedialog
init()
#-----------------------------------------------------------------------------------------------------------------------------------#    
screen = display.set_mode((1200,700),)              #Screen size is set
screen.blit(image.load("Images/Background.png") ,(0,0))
screen.blit(image.load("Images/Title.png") ,(175,5))
#-----------------------------------------------------------------------------------------------------------------------------------#
font = font.Font("ka1.ttf",15)
#-----------------------------------------------------------------------------------------------------------------------------------#
root = Tk()      #This is to get rid of the extra window that pops up when using tk
root.withdraw()
#-----------------------------------------------------------------------------------------------------------------------------------#
tool = "pencil"                #Beginning tool is assigned
old_tool = tool                #Used for detecting tool changes
mode = "select"                #Beginning mode is assigned           
background_swap = False        #Used to detect background changes
copy1 = True                   #First copy to set everything up
CordsTrigger = True            #Used to properly blit line, rect, and elipse tools
Fill = True                    #Decides wether to draw fillied or unfilled icons and shapes            
polygon = False                #Checks if polygon tool has been used but not completed
fill_change = True             #Indicates if there was a change to the fill variable
undo_copy = False              #Checks if an undo copy should be created
MusicPlaying = True        
SONG_END = False
colour = (0,0,0)
polygon_points = []
undo_list = []
redo_list = []
Background_list = []
thickness = 2
background = 0
old_background = background

mouse.set_pos(0,0)
#-----------------------------------------------------------------------------------------------------------------------------------#
canvasRect = Rect(125,100,855,500)             #Main Rects are assigned
greyscaleRect = Rect(1000,427,200,58)
coloursquareRect = Rect(1000,500,200,200)

pencilRect = Rect(37,25,50,50)
eraserRect = Rect(37,100,50,50)
brushRect = Rect(37,175,50,50)
sprayRect = Rect(37,250,50,50)
lineRect = Rect(37,325,50,50)
rectRect = Rect(37,400,50,50)
ellipseRect = Rect(37,475,50,50)
polygonRect = Rect(37,550,50,50)
eyedropperRect = Rect(37,625,50,50)

undoRect = Rect(892,6,41,41)
redoRect = Rect(939,6,41,41)

saveRect = Rect(892,53,41,41)
loadRect = Rect(939,53,41,41)

cordsRect = Rect(1000,225,125,50)
thicknessRect = Rect(1135,225,55,50)
cordxRect = Rect(1000,225,60,50)
cordyRect = Rect(1065,225,60,50)
    
colourdisplayRect = Rect(839,6,41,41)

fill_selectRect = Rect(792,53,88,41)
fill_trueRect = Rect(839,53,41,41)
fill_falseRect = Rect(792,53,41,41)

fillRect= Rect(1117,186,19,19)
background_back_Rect= Rect(1138,186,18,19)
background_next_Rect= Rect(1158,186,19,19)

Stamp1Rect = Rect(125,607,86,86)
Stamp2Rect = Rect(221,607,86,86)
Stamp3Rect = Rect(317,607,86,86)
Stamp4Rect = Rect(413,607,86,86)
Stamp5Rect = Rect(509,607,86,86)
Stamp6Rect = Rect(605,607,86,86)
Stamp7Rect = Rect(701,607,86,86)
Stamp8Rect = Rect(797,607,86,86)
Stamp9Rect = Rect(893,607,86,86)
#-----------------------------------------------------------------------------------------------------------------------------------#
MapTemplate = image.load("Images/TerrariaMinimap.png")                             #All images are loaded and blited

CanvasBackground1 = image.load("Images/CanvasBackground1.jpg")
CanvasBackground1 = transform.scale(CanvasBackground1 ,(855,500))
CanvasBackground1Preview = image.load("Images/CanvasBackground1Preview.png")

CanvasBackground2 = image.load("Images/CanvasBackground2.jpg")
CanvasBackground2 = transform.scale(CanvasBackground2 ,(855,500))
CanvasBackground2Preview = image.load("Images/CanvasBackground2Preview.jpg")

CanvasBackground3 = image.load("Images/CanvasBackground3.jpg")
CanvasBackground3 = transform.scale(CanvasBackground3 ,(855,500))
CanvasBackground3Preview = image.load("Images/CanvasBackground3Preview.jpg")

CanvasBackground4 = image.load("Images/CanvasBackground4.jpg")
CanvasBackground4 = transform.scale(CanvasBackground4 ,(855,500))
CanvasBackground4Preview = image.load("Images/CanvasBackground4Preview.jpg")
CanvasBackground4Preview = transform.scale(CanvasBackground4Preview ,(95,95))

InventoryBackground = image.load("Images/InventoryBackground.png")
InventoryBackgroundClicked = image.load("Images/InventoryBackgroundClicked.png")
InventoryBackgroundPreview = image.load("Images/InventoryBackgroundPreview.png")
#-----------------------------------------------------------------------------------------------------------------------------------#
screen.blit(CanvasBackground1Preview,(1005,5))
screen.blit(CanvasBackground2Preview,(1100,5))
screen.blit(CanvasBackground3Preview,(1005,100))
screen.blit(CanvasBackground4Preview,(1100,100))
screen.blit(MapTemplate ,(1000,0))

draw.rect(screen,(255,255,255),canvasRect)
draw.rect(screen,(255,255,255),(0,1040,40,40))

screen.blit(image.load("Images/Rgb Square.jpg") ,(1000,500))
screen.blit(image.load("Images/Greyscale.png") ,(1000,427))

PencilIcon = image.load("Images/Pencil Icon.png")
EraserIcon = image.load("Images/Eraser Icon.png")
BrushIcon = image.load("Images/Brush Icon.png")
SprayIcon = image.load("Images/Spray Icon.png")
LineIcon = image.load("Images/Line Icon.png")
Filled_Rect_Icon = image.load("Images/Rectangle filled Icon.png")
Unfilled_Rect_Icon = image.load("Images/Rectangle Unfilled Icon.png")
Filled_Ellipse_Icon = image.load("Images/Circle Filled Icon.png")
Unfilled_Ellipse_Icon = image.load("Images/Circle Unfilled Icon.png")
Filled_Polygon_Icon = image.load("Images/Polygon Filled Icon.png")
Unfilled_Polygon_Icon = image.load("Images/Polygon Unfilled Icon.png")
EyedropperIcon = image.load("Images/Eyedropper Icon.png")

PencilIconPreview = image.load("Images/Pencil Icon Preview.png")
EraserIconPreview = image.load("Images/Eraser Icon Preview.png")
BrushIconPreview = image.load("Images/Brush Icon Preview.png")
SprayIconPreview = image.load("Images/Spray Icon Preview.png")
LineIconPreview = image.load("Images/Line Icon Preview.png")
Filled_Rect_Icon_Preview = image.load("Images/Rectangle filled Icon Preview.png")
Unfilled_Rect_Icon_Preview = image.load("Images/Rectangle Unfilled Icon Preview.png")
Filled_Ellipse_Icon_Preview = image.load("Images/Circle Filled Icon Preview.png")
Unfilled_Ellipse_Icon_Preview = image.load("Images/Circle Unfilled Icon Preview.png")
Filled_Polygon_Icon_Preview = image.load("Images/Polygon Filled Icon Preview.png")
Unfilled_Polygon_Icon_Preview = image.load("Images/Polygon Unfilled Icon Preview.png")
EyedropperIconPreview = image.load("Images/Eyedropper Icon Preview.png")

StampBackground = image.load("Images/StampBackgroundPreview.png")
for i in range(0,864,96):
    screen.blit(StampBackground,(125+i,607))
    
Stamp1 = image.load("Images/Stamp 1.png")
Stamp2 = image.load("Images/Stamp 2.png")
Stamp3 = image.load("Images/Stamp 3.png")
Stamp4 = image.load("Images/Stamp 4.png")
Stamp5 = image.load("Images/Stamp 5.png")
Stamp6 = image.load("Images/Stamp 6.png")
Stamp7 = image.load("Images/Stamp 7.png")
Stamp8 = image.load("Images/Stamp 8.png")
Stamp9 = image.load("Images/Stamp 9.png")

Songs=["Audio/Audio 1.mp3","Audio/Audio 2.mp3","Audio/Audio 3.mp3","Audio/Audio 4.mp3"]#Audio variables and list are assigned. Music is also set to start playing
Song_Position = 0
Play_PauseRect = Rect(1078,328,44,44)
NextRect = Rect(1136,343,28,14)
BeforeRect= Rect(1037,343,28,14)
VolumeUpRect = Rect(1084,282,32,28)
VolumeDownRect = Rect(1084,390,32,28)

mixer.music.load(Songs[Song_Position])
mixer.music.play()
volume=mixer.music.get_volume()

SONG_END = USEREVENT + 1
mixer.music.set_endevent(SONG_END)

screen.blit(Stamp1 ,(145,610))
screen.blit(Stamp2 ,(239,610))
screen.blit(Stamp3 ,(327,610))
screen.blit(Stamp4 ,(436,610))
screen.blit(Stamp5 ,(529,610))
screen.blit(Stamp6 ,(625,610))
screen.blit(Stamp7 ,(710,610))
screen.blit(Stamp8 ,(817,610))
screen.blit(Stamp9 ,(913,610))

screen.blit(InventoryBackground ,(37,25))
screen.blit(InventoryBackground ,(37,100))
screen.blit(InventoryBackground ,(37,100))
screen.blit(InventoryBackground ,(37,175))
screen.blit(InventoryBackground ,(37,250))
screen.blit(InventoryBackground ,(37,325))
screen.blit(InventoryBackground ,(37,400))
screen.blit(InventoryBackground ,(37,475))
screen.blit(InventoryBackground ,(37,550))
screen.blit(InventoryBackground ,(37,625))

screen.blit(InventoryBackgroundPreview ,(792,6))
screen.blit(PencilIconPreview ,(796,10))

screen.blit(PencilIcon,(42,29))
screen.blit(EraserIcon,(42,106))
screen.blit(BrushIcon,(40,183))
screen.blit(SprayIcon,(48,256))
screen.blit(LineIcon,(42,331))
screen.blit(Filled_Rect_Icon,(42,405))
screen.blit(Filled_Ellipse_Icon,(42,480))
screen.blit(Filled_Polygon_Icon,(42,555))
screen.blit(EyedropperIcon,(42,630))

draw.circle(screen,(255,255,255),(912,26),20)
draw.circle(screen,(255,255,255),(959,26),20)
draw.rect(screen,(255,255,255),(940,53,39,38))
screen.blit(image.load("Images/Undo.png"),(892,6))
screen.blit(image.load("Images/Redo.png"),(939,6))
screen.blit(image.load("Images/Save.png"),(892,53))
screen.blit(image.load("Images/Load.png"),(939,53))

screen.blit(image.load("Images/MusicPlayer.png"),(1025,275))
                      
draw.rect(screen,colour,(colourdisplayRect))
draw.rect(screen,0,(colourdisplayRect),1)

draw.rect(screen,(255,255,255),fill_selectRect)
draw.rect(screen,(0,255,0),fill_trueRect)
#-----------------------------------------------------------------------------------------------------------------------------------#
copy = screen.copy()
running =True
click = False #Used for knowing when the save/load interfaces should be opened
while running:
    click = False
    for e in event.get():
        if e.type == QUIT:
            running = False
#-----------------------------------------------------------------------------------------------------------------------------------#
        if e.type == MOUSEBUTTONDOWN:    #Size controls
            if e.button == 4:
                if thickness < 40:
                    thickness += 1
            if e.button == 5:
                if thickness > 1:
                    thickness -= 1
#-----------------------------------------------------------------------------------------------------------------------------------#
        if e.type == MOUSEBUTTONUP:      #Variable to indicate tk needs to open
             if e.button == 1:
                 click = True
#-----------------------------------------------------------------------------------------------------------------------------------#
        if e.type == SONG_END:           #if song ends next song starts playing
            Song_Position += 1
            if Song_Position == 4:
                Song_Position = 0
            mixer.music.load(Songs[Song_Position])
            mixer.music.play()
#-----------------------------------------------------------------------------------------------------------------------------------#
    mb = mouse.get_pressed()             #Basic mouse info
    mx,my = mouse.get_pos()
#-----------------------------------------------------------------------------------------------------------------------------------#
    if tool == "eyedropper" and canvasRect.collidepoint(mx,my):
        mouse.set_visible(False)
    else:
        mouse.set_visible(True)
#-----------------------------------------------------------------------------------------------------------------------------------#
    screen.blit(InventoryBackground ,(37,25))             #Backgrounds and shapes are blited
    screen.blit(InventoryBackground ,(37,100))
    screen.blit(InventoryBackground ,(37,175))
    screen.blit(InventoryBackground ,(37,250))
    screen.blit(InventoryBackground ,(37,325))
    screen.blit(InventoryBackground ,(37,625))

    screen.blit(PencilIcon,(42,29))
    screen.blit(EraserIcon,(42,106))
    screen.blit(BrushIcon,(40,183))
    screen.blit(SprayIcon,(48,256))
    screen.blit(LineIcon,(42,331))
    screen.blit(EyedropperIcon,(42,630))
    if Fill:
            screen.blit(InventoryBackground ,(37,400))
            screen.blit(InventoryBackground ,(37,475))
            screen.blit(InventoryBackground ,(37,550))
            screen.blit(Filled_Rect_Icon,(42,405))
            screen.blit(Filled_Ellipse_Icon,(42,480))
            screen.blit(Filled_Polygon_Icon,(42,555))
    else:
            screen.blit(InventoryBackground ,(37,400))
            screen.blit(InventoryBackground ,(37,475))
            screen.blit(InventoryBackground ,(37,550))
            screen.blit(Unfilled_Rect_Icon,(42,405))
            screen.blit(Unfilled_Ellipse_Icon,(42,480))
            screen.blit(Unfilled_Polygon_Icon,(42,555))
#-----------------------------------------------------------------------------------------------------------------------------------#
    if fill_change:                                             #If the fill variable is swapped, this changes all the icons
        draw.rect(screen,(255,255,255),fill_selectRect)
        if Fill:
            draw.rect(screen,(0,255,0),fill_trueRect)
        else:
            draw.rect(screen,(255,0,0),fill_falseRect)
        if tool == "rectangle" or tool == "ellipse" or tool == "polygon":
            screen.blit(InventoryBackgroundPreview ,(792,6))
        if tool == "rectangle":
            screen.blit(Unfilled_Rect_Icon_Preview ,(796,10))
            if Fill:
                screen.blit(Filled_Rect_Icon_Preview ,(796,10))
        elif tool == "ellipse":
            if Fill:
                screen.blit(Filled_Ellipse_Icon_Preview ,(796,10))
            else:
                screen.blit(Unfilled_Ellipse_Icon_Preview ,(796,10))
        elif tool == "polygon":
            if Fill:
                screen.blit(Filled_Polygon_Icon_Preview ,(796,10))
            else:
                screen.blit(Unfilled_Polygon_Icon_Preview ,(796,10))
        copy = screen.copy()
        fill_change = False
    draw.rect(screen,colour,(colourdisplayRect))
    draw.rect(screen,0,(colourdisplayRect),1)
#-----------------------------------------------------------------------------------------------------------------------------------#
    if canvasRect.collidepoint(mx,my)and mb[0] == 1 and tool != "eyedropper" and tool != "polygon": #This makes sure to add a save everytime the canvas is interacted with
        undo_copy = True
    if undo_copy and mb[0] == 0: 
        redo_list = []     #Redo list is cleared
        undo_copy_add = screen.subsurface(canvasRect).copy() #Subsurface is saved then added to the list
        undo_list.append(undo_copy_add)
        undo_copy = False
    #-----------------------------------------------------------------------------------------------------------------------------------#
    if mode == "select":             # When hovering over the canvas, a "preview" is shown
        if tool == "pencil":
                if canvasRect.collidepoint(mx,my):
                    screen.set_clip(canvasRect)
                    if mb[0] == 1:
                        screen.blit(copy,(0,0))
                        copy = screen.copy()
                    if mb[0] == 0:
                        screen.blit(copy,(0,0))
                        draw.circle(screen,(colour),(mx,my),2)
                    screen.set_clip(None)
                else:
                    screen.blit(copy,(0,0))
        if tool == "eraser":
                if canvasRect.collidepoint(mx,my):
                    screen.set_clip(canvasRect)
                    if mb[0] == 1:
                        screen.blit(copy,(0,0))
                        copy = screen.copy()
                    if mb[0] == 0:
                        screen.blit(copy,(0,0))
                        draw.rect(screen,(0,0,0),(mx-thickness//2,my-thickness//2,thickness,thickness),1)
                    screen.set_clip(None)
                else:
                    screen.blit(copy,(0,0))
        if tool == "brush":
                if canvasRect.collidepoint(mx,my):
                    screen.set_clip(canvasRect)
                    if mb[0] == 1:
                        screen.blit(copy,(0,0))
                        copy = screen.copy()
                    if mb[0] == 0:
                        screen.blit(copy,(0,0))
                        draw.circle(screen,(colour),(mx,my),thickness)
                    screen.set_clip(None)
                else:
                    screen.blit(copy,(0,0))
        if tool == "spray":
                if canvasRect.collidepoint(mx,my):
                    screen.set_clip(canvasRect)
                    if mb[0] == 1:
                        screen.blit(copy,(0,0))
                        copy = screen.copy()
                    if mb[0] == 0:
                        screen.blit(copy,(0,0))
                        draw.circle(screen,(colour),(mx,my),thickness,1)
                    screen.set_clip(None)
                else:
                    screen.blit(copy,(0,0))
        if tool == "line":
            if canvasRect.collidepoint(mx,my):
                    screen.set_clip(canvasRect)
                    if mb[0] == 1:
                        screen.blit(copy,(0,0))
                        copy = screen.copy()
                    if mb[0] == 0:
                        screen.blit(copy,(0,0))
                        draw.rect(screen,(colour),(mx,my,thickness,thickness))
                    screen.set_clip(None)
        
            else:
                    screen.blit(copy,(0,0))
        if tool == "rectangle":
            if canvasRect.collidepoint(mx,my):
                    screen.set_clip(canvasRect)
                    if mb[0] == 1:
                        screen.blit(copy,(0,0))
                        copy = screen.copy()
                    if mb[0] == 0:
                        screen.blit(copy,(0,0))
                        draw.circle(screen,(colour),(mx,my),2)
                    screen.set_clip(None)
        
            else:
                    screen.blit(copy,(0,0))
        if tool == "ellipse":
            if canvasRect.collidepoint(mx,my):
                    screen.set_clip(canvasRect)
                    if mb[0] == 1:
                        screen.blit(copy,(0,0))
                        copy = screen.copy()
                    if mb[0] == 0:
                        screen.blit(copy,(0,0))
                        draw.circle(screen,(colour),(mx,my),2)
                    screen.set_clip(None)
        
            else:
                    screen.blit(copy,(0,0))
        if tool == "eyedropper":
                if canvasRect.collidepoint(mx,my):
                    screen.set_clip(canvasRect)
                    if mb[0] == 1:
                        screen.blit(copy,(0,0))
                        copy = screen.copy()
                    if mb[0] == 0:
                        screen.blit(copy,(0,0))
                        draw.circle(screen,screen.get_at((mx,my)),(mx,my),5)
                        draw.circle(screen,0,(mx,my),5,1)
                    screen.set_clip(None)
                else:
                    screen.blit(copy,(0,0))
            
    #-----------------------------------------------------------------------------------------------------------------------------------#
    if mb[0] == 1 and coloursquareRect.collidepoint(mx,my) and mode == "select" or mb[0] == 1 and greyscaleRect.collidepoint(mx,my) and mode == "select":
        mode = "colour"                                          #Colour is chosen here
    if mode == "colour":
        if mb[0] == 1 and coloursquareRect.collidepoint(mx,my): 
            screen.blit(image.load("Images/Greyscale.png") ,(1000,427))    #Images are blitted, then colour is taken and a circle is drawn around mx,my. Setclip is used to make sure this circle doesnt clip. 
            screen.set_clip(coloursquareRect)
            screen.blit(image.load("Images/Rgb Square.jpg") ,(1000,500))
            colour = screen.get_at((mx,my))
            draw.circle(screen,(0,0,0),(mx,my),6,1)
            screen.set_clip(None)
        elif mb[0] == 1 and greyscaleRect.collidepoint(mx,my):
            screen.blit(image.load("Images/Greyscale.png") ,(1000,427))    #Images are blitted, then coulour is taken and depending on theat valuse a rect is drawn around the selected colour
            screen.blit(image.load("Images/Rgb Square.jpg") ,(1000,500))
            colour = screen.get_at((mx,my))
            if colour[0] <= 255 and colour[0] > 234:
                draw.rect(screen,(0,255,0),(1001,429,int(28.5),53),2)
            elif colour[0] <= 234 and colour[0] > 192:
                draw.rect(screen,(0,255,0),(1030,429,int(28.5),53),2)
            elif colour[0] <= 192 and  colour[0] > 149:
                draw.rect(screen,(0,255,0),(1059,429,26,53),2)
            elif colour[0] <= 149 and  colour[0] > 106:
                draw.rect(screen,(0,255,0),(1085,429,26,53),2)
            elif colour[0] == colour[0] <= 106 and  colour[0] > 64:
                draw.rect(screen,(0,255,0),(1112,429,27,53),2)
            elif colour[0] == colour[0] <= 64 and  colour[0] > 21:
                draw.rect(screen,(0,255,0),(1141,429,27,53),2)
            else:
                draw.rect(screen,(0,255,0),(1167,429,29,54),2)
                
        if mb[0] == 0:
            copy = screen.copy()
            mode = "select"
    #-----------------------------------------------------------------------------------------------------------------------------------#
    if mode == "select":   #Makes sure you arent in the middle of drawing
    #-----------------------------------------------------------------------------------------------------------------------------------#
        if click:                                #Images can be saved and loaded   
            if saveRect.collidepoint(mx,my):
                if len(undo_list) > 1:           #Makes sure the screen is not white
                    result = filedialog.asksaveasfilename()     #Name of file is asked for
                    sav = screen.subsurface(canvasRect)         #Canvas is saved
                    image.save(sav,str(result) + ".png")        #Image is saved
                    print(image.tostring(sav,"RGBA")[:50])      #Image is dispalyed
            elif loadRect.collidepoint(mx,my):
                result = filedialog.askopenfilename(filetypes = [("Picture files", "*.png;*.jpg")]) #The file name is given
                if result != "": #Makes sure a file was selected
                    loadimage = image.load(result) #Image is assigned to a variabe
                    loadimage = transform.scale(loadimage,(855,500)) #Loaded images are scaled to fit the background
                    screen.blit(loadimage,(125,100))# Image is blited
                    copy = screen.copy() #Screen is coppied
                    undo_copy = True #An undo copy is created
    #-----------------------------------------------------------------------------------------------------------------------------------#
    
        if mb[0] == 1 and Play_PauseRect.collidepoint(mx,my): #Music controls
            if MusicPlaying:                                  #If music is playing its paused
                mixer.music.pause()
                MusicPlaying = False
            else:                                             #If music is possed it starts playing
                mixer.music.unpause()
                MusicPlaying = True
            time.wait(200)
        if mb[0] == 1 and NextRect.collidepoint(mx,my):       #1 is added to the song position unless its 3 then it goes back to 0
            Song_Position += 1
            if Song_Position == 4:
                Song_Position = 0
            mixer.music.load(Songs[Song_Position])
            mixer.music.play()
            time.wait(200)
        if mb[0] == 1 and BeforeRect.collidepoint(mx,my):     #1 is subtracted form the song position unless its 0 then it becomes 3
            Song_Position -= 1
            if Song_Position == -1:
                Song_Position = 3
            mixer.music.load(Songs[Song_Position])
            mixer.music.play()
            time.wait(200)
        if mb[0] == 1 and VolumeUpRect.collidepoint(mx,my):   #0.1 is added to the volume variable
            if volume < 1.0:
                volume += 0.1
            mixer.music.set_volume(volume)
            time.wait(200)
        if mb[0] == 1 and VolumeDownRect.collidepoint(mx,my): #-0.1 is added to the volume variable
            if volume > 0.1:
                volume -= 0.1
            mixer.music.set_volume(volume)
            time.wait(200)
            
    #-----------------------------------------------------------------------------------------------------------------------------------#
        if mb[0] == 1 and undoRect.collidepoint(mx,my):               #Undo and redo
            time.wait(200)
            undo_len = len(undo_list)-1
            if undo_len > 0:                                          #Makes sure white base background is kept in the loop
                undo_current = undo_list[undo_len]                    #This variable is the one being added and taken away from the lists
                redo_list.append(undo_current)                        #Variable is added to redo
                undo_list.remove(undo_current)                        #Variable is removed from the undo list
                screen.blit(undo_list[int(undo_len)-1],(125,100))     #Undo is blitted onto the screen
                copy = screen.copy()                                  #Screen is saved
        if mb[0] == 1 and redoRect.collidepoint(mx,my):
            time.wait(200)
            redo_len = len(redo_list)-1
            if redo_len >= 0:                                         #Makes sere the redo is not a negative number
                redo_current = redo_list[redo_len]                    #The variable that will be removed and added is assigned
                screen.blit(redo_list[int(redo_len)],(125,100))       #Redo is blitted
                undo_list.append(redo_current)                        #Variable is added to the undo list
                redo_list.remove(redo_current)                        #Variable is removed from the redo list
                copy = screen.copy()                                  #Screen is saved
    #-----------------------------------------------------------------------------------------------------------------------------------# 
        if mb[0] == 1 and fillRect.collidepoint(mx,my):        #This controls the background change
            background = 0
            background_swap = True
            time.wait(200)
        if mb[0] == 1 and background_back_Rect.collidepoint(mx,my):
            if background == 0 or background == 1:             #If background is 0 or 1 it becomes 4 not 0 or -1 otherwise 1 is taken away from the background variable
                background = 4
            else:
                background -= 1
            background_swap = True
            time.wait(200)
        if mb[0] == 1 and background_next_Rect.collidepoint(mx,my):
            if background == 4:                                 #There are only 5 background so this variable should not be more than 4. Otherwise 1 is added to the background variable                          
                background = 1
            else:
                background += 1
            background_swap = True
            time.wait(200)
    #-----------------------------------------------------------------------------------------------------------------------------------#
        if mb[0] == 1 and fill_selectRect.collidepoint(mx,my):#Able to control fill toggle
            time.wait(200)          #If the fill variable is true, it becomes  false and vise-versa
            if Fill: 
                Fill = False
            else:
                Fill = True
            fill_change = True
    #-----------------------------------------------------------------------------------------------------------------------------------#      
        if mb[0] == 1 and pencilRect.collidepoint(mx,my): #Tool select
            screen.blit(InventoryBackgroundClicked ,(37,25))
            screen.blit(PencilIcon,(42,29))
            tool = "pencil"
        if mb[0] == 1 and eraserRect.collidepoint(mx,my):
            screen.blit(InventoryBackgroundClicked ,(37,100))
            screen.blit(EraserIcon,(42,106))
            tool = "eraser"
        if mb[0] == 1 and brushRect.collidepoint(mx,my):
            screen.blit(InventoryBackgroundClicked ,(37,175))
            screen.blit(BrushIcon,(40,183))
            tool = "brush"
        if mb[0] == 1 and sprayRect.collidepoint(mx,my):
            screen.blit(InventoryBackgroundClicked ,(37,250))
            screen.blit(SprayIcon,(48,256))
            tool = "spray"
        if mb[0] == 1 and lineRect.collidepoint(mx,my):
            screen.blit(InventoryBackgroundClicked ,(37,325))
            screen.blit(LineIcon,(42,331))
            tool = "line"
        if mb[0] == 1 and rectRect.collidepoint(mx,my):
            screen.blit(InventoryBackgroundClicked ,(37,400))
            if Fill:
                screen.blit(Filled_Rect_Icon,(42,405))
            else:
                screen.blit(Unfilled_Rect_Icon,(42,405))
            tool = "rectangle"
        if mb[0] == 1 and ellipseRect.collidepoint(mx,my):
            screen.blit(InventoryBackgroundClicked ,(37,475))
            if Fill:
                screen.blit(Filled_Ellipse_Icon,(42,480))
            else:
                screen.blit(Unfilled_Ellipse_Icon,(42,480))
            tool = "ellipse"
        if mb[0] == 1 and polygonRect.collidepoint(mx,my):
            screen.blit(InventoryBackgroundClicked ,(37,550))
            if Fill:
                screen.blit(Filled_Polygon_Icon,(42,555))
            else:
                screen.blit(Unfilled_Polygon_Icon,(42,555))
            tool = "polygon"
            polygon = True
        if mb[0] == 1 and eyedropperRect.collidepoint(mx,my):
            screen.blit(InventoryBackgroundClicked ,(37,625))
            screen.blit(EyedropperIcon,(42,630))
            tool = "eyedropper"
    #-----------------------------------------------------------------------------------------------------------------------------------#  
    if mb[0] == 1 and canvasRect.collidepoint(mx,my) and mode == "select": #sets mode to drawing when canvas is being interacted with
        mode = "drawing"
    #-----------------------------------------------------------------------------------------------------------------------------------#
    if mode == "drawing":
            screen.set_clip(canvasRect)
        
            if tool == "pencil":
                draw.line(screen,(colour),(omx,omy),(mx,my),1)
                
            elif tool == "eraser": #Takes a sqaure of the image and blits it at mx my
                      screen.blit(Background_list[background],(mx-thickness//2,my-thickness//2,thickness,thickness),(mx-(125+thickness//2),my-(100+thickness//2),thickness,thickness)) 
                      dx = mx-omx
                      dy = my-omy
                      hyp =sqrt(dx**2+dy**2)
                      if hyp % 1 != 0:
                          hyp += 0.5
                      for i in range(0,int(hyp)):
                          circlex = int(omx-thickness//2+i*dx/hyp)
                          circley = int(omy-thickness//2+i*dy/hyp)
                          screen.blit(Background_list[background],(circlex,circley,thickness,thickness),(circlex-125,circley-100,thickness,thickness))
                          #Loop is to blit every certain distance so fast movements or lag dont create spaces in the erasing
                      copy = screen.copy()
                
            elif tool == "brush":
                  draw.circle(screen,colour,(mx,my),thickness)
                  if omx != mx or omy!= my:
                      dx = mx-omx
                      dy = my-omy
                      hyp =sqrt(dx**2+dy**2)
                      if hyp % 1 != 0:
                          hyp += 0.5
                      for i in range(0,int(hyp),1):
                          circlex = int(omx+i*dx/hyp)
                          circley = int(omy+i*dy/hyp)
                          draw.circle(screen,colour,(circlex,circley),thickness)
                          #loop is created for the same reason here 
                      copy = screen.copy()
                          
            elif tool == "spray" :
                for i in range(int(thickness**1.3)):
                    randx = randint(mx-thickness,mx+thickness)
                    randy = randint(my-thickness,my+thickness)
                    distance = hypot((randx-mx),(randy-my))
                    if thickness >= 10:
                        if distance <= thickness and mb[0] ==1:#eliminates the square shape and turns it into a circle then at random points in the circle radius, points are drawn
                            draw.circle(screen,colour,(randx,randy),int(0.5))
                    else:
                        randx = randint(mx-10,mx+10)
                        randy = randint(my-10,my+10)
                        distance = hypot((randx-mx),(randy-my))
                        if distance <= 10 and mb[0] ==1:
                            draw.circle(screen,colour,(randx,randy),int(0.5))
                            
            elif tool == "line":
                if CordsTrigger:#First points are saved until left clicked is not being clicked anymore
                    linemx = mx
                    linemy = my
                CordsTrigger = False
                screen.blit(copy,(0,0))
                draw.line(screen,colour,(linemx,linemy),(mx,my),thickness)
                
            elif tool == "rectangle":
                if CordsTrigger:#First points are saved until left clicked is not being clicked anymore
                    Rectanglemx = mx
                    Rectanglemy = my
                CordsTrigger = False
                screen.blit(copy,(0,0))
                if Fill:
                    draw.rect(screen,colour,(Rectanglemx,Rectanglemy,mx-Rectanglemx,my-Rectanglemy))
                else:
                    if Rectanglemy < my:#4 lines are drawn here to eliminate gaps in the corners
                        draw.line(screen,colour,(Rectanglemx,Rectanglemy-int(thickness//2.1)),(Rectanglemx,my+int(thickness//2)),thickness)
                        draw.line(screen,colour,(mx,Rectanglemy-int(thickness//2.1)),(mx,my+int(thickness//2)),thickness)
                        draw.line(screen,colour,(Rectanglemx,Rectanglemy),(mx,Rectanglemy),thickness)
                        draw.line(screen,colour,(Rectanglemx,my),(mx,my),thickness)
                    else:#4 lines are drawn here to eliminate gaps in the corners
                        draw.line(screen,colour,(Rectanglemx,Rectanglemy+int(thickness//2)),(Rectanglemx,my-int(thickness//2.1)),thickness)
                        draw.line(screen,colour,(mx,Rectanglemy+int(thickness//2)),(mx,my-int(thickness//2.1)),thickness)
                        draw.line(screen,colour,(Rectanglemx,Rectanglemy),(mx,Rectanglemy),thickness)
                        draw.line(screen,colour,(Rectanglemx,my),(mx,my),thickness)
                        
            elif tool == "ellipse":
                if CordsTrigger:#First points are saved until left clicked is not being clicked anymore
                    ellipsemx = mx
                    ellipsemy = my
                CordsTrigger = False
                screen.blit(copy,(0,0))
                ellipse_cords = Rect(ellipsemx,ellipsemy,mx-ellipsemx,my-ellipsemy)
                ellipse_cords.normalize()
                if Fill:
                    draw.ellipse(screen,colour,ellipse_cords)
                else:
                    if ellipse_cords.width < thickness*2 or ellipse_cords.height < thickness*2:#if assigned area is too small elipse is drawn filled
                        draw.ellipse(screen,colour,ellipse_cords)
                    else:
                        draw.ellipse(screen,colour,ellipse_cords,thickness)
                        
            elif tool == "polygon":
              if polygon:
                   polygon_copy = screen.subsurface(canvasRect).copy()#Cords are saved here but polygon is drawn seperate because right clicks arent registired in this specific loop
                   polygon = False
              if mb[0] == 1 and CordsTrigger:   #Points get added to a list fopr later use
                    CordsTrigger = False
                    polygon_points.append((mx,my))
                    draw.circle(screen,colour,(mx,my),int(0.5))
            elif tool == "eyedropper":
                colour = screen.get_at((mx,my))
                screen.blit(image.load("Images/Greyscale.png") ,(1000,427)) #These are blitted to get rid of the expired colour indication on them
                screen.blit(image.load("Images/Rgb Square.jpg") ,(1000,500))
                copy = screen.copy()
    #-----------------------------------------------------------------------------------------------------------------------------------#     
            if mb[0] ==  0:
                CordsTrigger = True    #This is done to be able to select new starting point for line,rect, and ellipse tool
                copy = screen.copy()   #Screen is coppied
                mode = "select"        #Mode is set to selct so you are now able to interact with things
            screen.set_clip(None)
            
    #-----------------------------------------------------------------------------------------------------------------------------------#
    if mode == "stamp" and canvasRect.collidepoint(mx,my): #Stamp movement
        screen.set_clip(canvasRect)
        if mb[0] == 0: #If left click is false, screen is saved and mode is set back to select
             copy = screen.copy()
             mode = "select"
        if stamp == 1:
             screen.blit(copy,(0,0))             #If left click is true, the select stamp is blitted after blitting the copy variable
             screen.blit(Stamp1,(mx-20,my-40))
        elif stamp == 2:
             screen.blit(copy,(0,0))
             screen.blit(Stamp2,(mx-20,my-40))
        elif stamp == 3:
             screen.blit(copy,(0,0))
             screen.blit(Stamp3,(mx-20,my-40))
        elif stamp == 4:
             screen.blit(copy,(0,0))
             screen.blit(Stamp4,(mx-20,my-40))
        elif stamp == 5:
             screen.blit(copy,(0,0))
             screen.blit(Stamp5,(mx-20,my-40))
        elif stamp == 6:
             screen.blit(copy,(0,0))
             screen.blit(Stamp6,(mx-20,my-40))
        elif stamp == 7:
             screen.blit(copy,(0,0))
             screen.blit(Stamp7,(mx-20,my-40))
        elif stamp == 8:
             screen.blit(copy,(0,0))
             screen.blit(Stamp8,(mx-20,my-40))
        elif stamp == 9:
             screen.blit(copy,(0,0))
             screen.blit(Stamp9,(mx-20,my-40))
                
                
            
        screen.set_clip(None)
    if mode == "select":            #Stamp select
        if mb[0] == 1 and Stamp1Rect.collidepoint(mx,my):    #mode is set to stamp and stamp variable indicates which stamp was selected
            mode = "stamp"
            stamp = 1
        elif mb[0] == 1 and Stamp2Rect.collidepoint(mx,my):
            mode = "stamp"
            stamp = 2
        elif mb[0] == 1 and Stamp3Rect.collidepoint(mx,my):
            mode = "stamp"
            stamp = 3
        elif mb[0] == 1 and Stamp4Rect.collidepoint(mx,my):
            mode = "stamp"
            stamp = 4
        elif mb[0] == 1 and Stamp5Rect.collidepoint(mx,my):
            mode = "stamp"
            stamp = 5
        elif mb[0] == 1 and Stamp6Rect.collidepoint(mx,my):
            mode = "stamp"
            stamp = 6
        elif mb[0] == 1 and Stamp7Rect.collidepoint(mx,my):
            mode = "stamp"
            stamp = 7
        elif mb[0] == 1 and Stamp8Rect.collidepoint(mx,my):
            mode = "stamp"
            stamp = 8
        elif mb[0] == 1 and Stamp9Rect.collidepoint(mx,my):
            mode = "stamp"
            stamp = 9
    if mode == "stamp" and mb[0] == 0: #This has to be after so the background is saved before stamp mode is disabled
        mode = "select"
    #-----------------------------------------------------------------------------------------------------------------------------------#
    if background_swap: #If there is a background alteration, this is where a background is chosen to be blited
            if background == 0:
                  draw.rect(screen,(255,255,255),canvasRect)
            elif background == 1:
                  screen.blit(CanvasBackground1,(125,100))
            elif background == 2:
                  screen.blit(CanvasBackground2,(125,100))
            elif background == 3:
                  screen.blit(CanvasBackground3,(125,100))
            elif background == 4:
                  screen.blit(CanvasBackground4,(125,100))
            background_swap = False                       #Background swap is set to false after 1 loop
            copy = screen.copy()
    #-----------------------------------------------------------------------------------------------------------------------------------#
    if copy1:
        draw.rect(screen,(255,255,255),canvasRect) #This is to get rid of the dot that likes to appear on first save from the pencil hovering effect
        copy = screen.copy()
        Background_list = [screen.subsurface(canvasRect).copy(),CanvasBackground1,CanvasBackground2,CanvasBackground3,CanvasBackground4]#Backround list sued for eraser is assigned here because i need to copy canvas in the first spot
        copy1 = False
        undo_copy = screen.subsurface(canvasRect).copy() #This is for the white background in the undo list
        undo_list.append(undo_copy)
        CordsBackgroundCopy = screen.subsurface(cordsRect).copy()          #Used for blitting cords without them overlapping
        ThicknessBackgroundCopy = screen.subsurface(thicknessRect).copy()  #Used for blitting thickness without overlapping
    #-----------------------------------------------------------------------------------------------------------------------------------#  
    if tool == "polygon":
        if mb[2] == 1  and len(polygon_points) > 2:                        #If u right click after having selected 2 points, the polygon is created
            if Fill:
                draw.polygon(screen,colour,polygon_points)
            else:
                draw.polygon(screen,colour,polygon_points,1)
            polygon_points = []
            copy = screen.copy()
            polygon_copy = screen.subsurface(canvasRect).copy()
            undo_copy = True
    if old_tool == "polygon" and tool != "polygon":   #if polyogn tool is changed this loop is activated
        polygon_points = []                           #Polygon list is cleared
        if polygon == False:                          #This is to indicate if there are unused polygon points on the canvas
            screen.blit(undo_list[int(len(undo_list))-1],(125,100)) #this blits a copy of the canvas before the unused points were there
            screen.blit(InventoryBackground ,(37,25))               #All icons and tool backgrounds are blitted because the selected 1 in the previos save would be green
            screen.blit(InventoryBackground ,(37,100))          
            screen.blit(InventoryBackground ,(37,175))
            screen.blit(InventoryBackground ,(37,250))
            screen.blit(InventoryBackground ,(37,325))
            screen.blit(InventoryBackground ,(37,400))
            screen.blit(InventoryBackground ,(37,475))
            screen.blit(InventoryBackground ,(37,550))
            screen.blit(InventoryBackground ,(37,625))

            screen.blit(PencilIcon,(42,29))
            screen.blit(EraserIcon,(42,106))
            screen.blit(BrushIcon,(40,183))
            screen.blit(SprayIcon,(48,256))
            screen.blit(LineIcon,(42,331))
            if Fill:
                screen.blit(Filled_Rect_Icon,(42,405))
                screen.blit(Filled_Ellipse_Icon,(42,480))
                screen.blit(Filled_Polygon_Icon,(42,555))
            else:
                screen.blit(Unfilled_Rect_Icon,(42,405))
                screen.blit(Unfilled_Ellipse_Icon,(42,480))
                screen.blit(Unfilled_Polygon_Icon,(42,555))
            screen.blit(EyedropperIcon,(42,630))
            copy = screen.copy()
    #-----------------------------------------------------------------------------------------------------------------------------------#              
    if tool == "eyedropper" and canvasRect.collidepoint(mx,my) and mb[0] == 1 and mode == "select":
                colour = screen.get_at((mx,my))
                screen.blit(image.load("Images/Greyscale.png") ,(1000,427))
                screen.blit(image.load("Images/Rgb Square.jpg") ,(1000,500))
                copy = screen.copy()
    #-----------------------------------------------------------------------------------------------------------------------------------#                  
    if old_tool != tool: #If tool is swapped, a preview icon is blited in the top right
        screen.blit(InventoryBackgroundPreview ,(792,6))#All icons and tool backgrounds are blitted because the selected 1 in the previos save would be green
        screen.blit(InventoryBackground ,(37,25))
        screen.blit(InventoryBackground ,(37,100))
        screen.blit(InventoryBackground ,(37,175))
        screen.blit(InventoryBackground ,(37,250))
        screen.blit(InventoryBackground ,(37,325))
        screen.blit(InventoryBackground ,(37,400))
        screen.blit(InventoryBackground ,(37,475))
        screen.blit(InventoryBackground ,(37,550))
        screen.blit(InventoryBackground ,(37,625))

        screen.blit(PencilIcon,(42,29))
        screen.blit(EraserIcon,(42,106))
        screen.blit(BrushIcon,(40,183))
        screen.blit(SprayIcon,(48,256))
        screen.blit(LineIcon,(42,331))
        if Fill:
                screen.blit(Filled_Rect_Icon,(42,405))
                screen.blit(Filled_Ellipse_Icon,(42,480))
                screen.blit(Filled_Polygon_Icon,(42,555))
        else:
                screen.blit(Unfilled_Rect_Icon,(42,405))
                screen.blit(Unfilled_Ellipse_Icon,(42,480))
                screen.blit(Unfilled_Polygon_Icon,(42,555))
        screen.blit(EyedropperIcon,(42,630))
        if tool == "pencil":
            screen.blit(PencilIconPreview ,(796,10))
        elif tool == "eraser":
            screen.blit(EraserIconPreview ,(796,10))
        elif tool == "brush":
            screen.blit(BrushIconPreview ,(794,12))
        elif tool == "spray":
            screen.blit(SprayIconPreview ,(802,10))
        elif tool == "line":
            screen.blit(LineIconPreview ,(795,10))
        elif tool == "rectangle":
            if Fill:
                screen.blit(Filled_Rect_Icon_Preview ,(796,10))
            else:
                screen.blit(Unfilled_Rect_Icon_Preview ,(796,10))
        elif tool == "ellipse":
            if Fill:
                screen.blit(Filled_Ellipse_Icon_Preview ,(796,10))
            else:
                screen.blit(Unfilled_Ellipse_Icon_Preview ,(796,10))
        elif tool == "polygon":
            if Fill:
                screen.blit(Filled_Polygon_Icon_Preview ,(796,10))
            else:
                screen.blit(Unfilled_Polygon_Icon_Preview ,(796,10))
        elif tool == "eyedropper":
            screen.blit(EyedropperIconPreview ,(796,10))
        copy = screen.copy()
    if old_background != background: #If background is swapped, an undo copy is saved
        undo_copy = True
    #-----------------------------------------------------------------------------------------------------------------------------------#    
    screen.blit(CordsBackgroundCopy,(1000,225))             #This is for cords and size bliting
    screen.blit(ThicknessBackgroundCopy,(1135,225))
    xtitle = "X"                                            #Variables are assigned and turned into strings
    ytitle = "Y"
    sizetitle = "Size"
    xPosition = str(mx)
    yPosition = str(my)
    Thickness_str = str(thickness)
    xPosition = font.render(xPosition,True,(0,0,0))         #Variables are rendered
    yPosition = font.render(yPosition,True,(0,0,0))
    Thickness_str = font.render(Thickness_str,True,(0,0,0))
    xtitle = font.render(xtitle,True,(0,0,0))
    ytitle = font.render(ytitle,True,(0,0,0))
    sizetitle = font.render(sizetitle,True,(0,0,0))
    screen.blit(xPosition,(1000,250))                       #Variables are blitted
    screen.blit(yPosition,(1075,250))
    screen.blit(Thickness_str,(1150,250))
    screen.blit(xtitle,(1000,230))
    screen.blit(ytitle,(1075,230))
    screen.blit(sizetitle,(1140,230))
    #-----------------------------------------------------------------------------------------------------------------------------------#
    omx,omy = mx,my
    old_tool = tool
    old_background = background
    display.flip()

quit()

