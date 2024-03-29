# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Masashi Kamiya")
define u = Character("Usui")
define b = Character("Bob")
define c = Character("Big Chungus")
define a = Character("Asami, great leader of dumbasses temporary name")



# The game starts here.

label start:

    play music "bgm/chungus.mp3" fadeout (1.5)

    scene black

    pause 1.5
    
    show asami_neutral
    
    with Dissolve (1.5)
    
    a "So, you're here! Welcome to WACCLAND DaTING SIM 2, where the game isn't even started yet and I'm just here to test the character sprites"
    
    show asami_dumbass
    hide asami_neutral
    show miyuki_neutral with Dissolve(0.5):
        xpos -300
        ypos 100
    show bob_neutral with Dissolve(0.5):
        xpos 1000
        ypos -50
    
    b "Hello, it is me Bob"
    hide bob_neutral with Dissolve(0.5)
    
    show masashi_neutral with Dissolve(0.5):
        xpos 1000
        ypos -50
    a "Did you know that!"
    # This joke isn't funny!
    # It's so not funny I hid it in the code!
    m "My real name is Mathias Cockland!"

    # This ends the game.

    return
