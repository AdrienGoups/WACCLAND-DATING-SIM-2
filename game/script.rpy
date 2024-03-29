# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Masashi Kamiya")
define u = Character("Usui")
define b = Character("Bob")
define c = Character("Big Chungus")
define a = Character("Asami, great leader of dumbasses temporary name")
define unk = Character("???")



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

    pause 10

    "The time has cometh for the Wacclandeth of Dating SIM.... 2!!!!!!!!!!"
    "the revengeance of the electric boogaloo of CHUNGUS"
    "No adrien I ain't fixin' the goddamn script"

    # FR THIS TIME THIS IS THE start

    "NOVEMBER 21, 20XX"
    "The final day has finally arrived."
    "No one could have guessed what was coming."
    "But even then, we had to fight it..."

    # MET UNE IMAGE DE LA PLANETE QUI SE FAIT ATTACKER OR SOME SHIT

    pause 10

    unk "MC, the only way you can save this world is to go back in time."
    unk "I will send you back, 6 months back from now."
    unk "During these 6 months, you have one mission. One of the greatest importance"
    unk "Go get bitches. At any cost, no matter if it's one or a thousand... You must get a Girlfriend!"
    m "I understand..."
    m "I'll do it!"
    m "I will get a Girlfriend... and save this world!"

    scene black with Dissolve (1.5)
    scene white with Dissolve (3)

    play music ("bgm/god.mp3") fadeout (1.5)

    show chungus with Dissolve (3)

    c "Masashi Kamiya... Thoust grand quest begins here."
    c "Acquire a Maiden. That is thy task."
    c "Now, go forth with Wacc and Land, my child!"

    # This ends the game.

    return
