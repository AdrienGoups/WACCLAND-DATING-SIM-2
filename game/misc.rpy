# ASAMI

image asami_neutral:
    "char/asami_neutral.png"
    ypos 1200 xpos 900
    zoom 0.55
        
image asami_dumbass:
    "char/asami_dumbass.png"
    ypos 1200 xpos 900
    zoom 0.55

image asami_confused:
    "char/asami_confused.png"
    ypos 1200 xpos 900
    zoom 0.55

image asami_mad:
    "char/asami_mad.png"
    ypos 1200 xpos 900
    zoom 0.55

image asami_smug:
    "char/asami_smug.png"
    ypos 1200 xpos 900
    zoom 0.55

image asami_kill:
    "char/asami_kill.png"
    ypos 1200 xpos 900
    zoom 0.55
    
image asami_unsure:
    "char/asami_unsure.png"
    ypos 1200 xpos 900
    zoom 0.55

image asami_judge:
    "char/asami_judge.png"
    ypos 1200 xpos 900
    zoom 0.55

image asami_happy:
    "char/asami_happy.png"
    ypos 1200 xpos 900
    zoom 0.55

image asami_intrigued:
    "char/asami_intrigued.png"
    ypos 1200 xpos 900
    zoom 0.55

# MOMOKA

image momoka_neutral:
    "char/momoka_neutral.png"
    ypos 1200 xpos 900
    zoom 0.55

image momoka_cat:
    "char/momoka_cat.png"
    ypos 1200 xpos 900
    zoom 0.55

image momoka_confused:
    "char/momoka_confused.png"
    ypos 1200 xpos 900
    zoom 0.55

image momoka_happy:
    "char/momoka_happy.png"
    ypos 1200 xpos 900
    zoom 0.55

image momoka_intrigued:
    "char/momoka_intrigued.png"
    ypos 1200 xpos 900
    zoom 0.55

image momoka_panick:
    "char/momoka_panick.png"
    ypos 1200 xpos 900
    zoom 0.55

image momoka_serious:
    "char/momoka_serious.png"
    ypos 1200 xpos 900
    zoom 0.55

image momoka_surprised:
    "char/momoka_surprised.png"
    ypos 1200 xpos 900
    zoom 0.55

# MIYUKI
        
image miyuki_neutral:
    "char/miyuki_neutral.png"
    ypos 1200 xpos 900
    zoom 0.55

image miyuki_happy:
    "char/miyuki_happy.png"
    ypos 1200 xpos 900
    zoom 0.55

image miyuki_mad:
    "char/miyuki_mad.png"
    ypos 1200 xpos 900
    zoom 0.55

image miyuki_smug:
    "char/miyuki_smug.png"
    ypos 1200 xpos 900
    zoom 0.55

image miyuki_unimpressed:
    "char/miyuki_unimpressed.png"
    ypos 1200 xpos 900
    zoom 0.55
        
image bob_neutral:
    "char/bob_neutral.png"
    ypos 1100 xpos 900
    zoom 0.55

image usui_neutral:
    "char/usui_neutral.png"
    ypos 1200 xpos 900
    zoom 0.55

# Masashi
        
image masashi_neutral:
    "char/masashi_neutral.png"
    ypos 1100 xpos 900
    zoom 0.55
image masashi_neutral:
    "char/masashi_annoyed.png"
    ypos 1100 xpos 900
    zoom 0.55
image masashi_neutral:
    "char/masashi_confused.png"
    ypos 1100 xpos 900
    zoom 0.55
image masashi_neutral:
    "char/masashi_mew.png"
    ypos 1100 xpos 900
    zoom 0.55
image masashi_neutral:
    "char/masashi_suspicious.png"
    ypos 1100 xpos 900
    zoom 0.55
image masashi_neutral:
    "char/masashi_thinking.png"
    ypos 1100 xpos 900
    zoom 0.55
image masashi_neutral:
    "char/masashi_unsure.png"
    ypos 1100 xpos 900
    zoom 0.55

image yomki:
    "char/yomki.png"
    ypos 1100 xpos 900
    zoom 0.55

image yomki_mad:
    "char/yomki_mad.png"
    ypos 1100 xpos 900
    zoom 0.55

image yomki_smug:
    "char/yomki_smug.png"
    ypos 1100 xpos 900
    zoom 0.55

image gorou_neutral:
    "char/gorou_neutral.png"
    ypos 1100 xpos 900
    zoom 0.55

image gorou_smug:
    "char/gorou_smug.png"
    ypos 1100 xpos 900
    zoom 0.55

image gorou_yell:
    "char/gorou_yell.png"
    ypos 1100 xpos 900
    zoom 0.55

image gorou_surprised:
    "char/gorou_surprised.png"
    ypos 1100 xpos 900
    zoom 0.55

image izumi_neutral:
    "char/izumi_neutral.png"
    ypos 1200
    xpos 900
    zoom 0.55

image izumi_smoke:
    "char/izumi_smoke.png"
    ypos 1200
    xpos 900
    zoom 0.55

image chungus:
    "char/chungus.png"
        
image residential:
    "bg/residential.png"
    zoom 1.5
        
image classroom:
    "bg/classroom.png"
    zoom 1.5
        
image house:
    "bg/house.png"
    zoom 1.5

image black:
    "bg/black.jpg"

image white:
    "bg/white.png"

image destroyed_world:
    "bg/destroyed_world.png"
    zoom 1.5

image bedroom:
    "bg/bedroom.png"
    zoom 1.5

image waccdonald:
    "bg/waccdonald.png"
    zoom 1.5

image corridor:
    "bg/corridor.png"
    zoom 1.5

image club:
    "bg/club.png"
    zoom 1.5

image rooftop:
    "bg/rooftop.png"
    zoom 1.5

image gym:
    "bg/gym.png"
    zoom 1.5

image school:
    "bg/school.png"

image saul:
    "saul.png"

image billy:
    "char/billy.png"
    ypos 1700 xpos 900
    zoom 0.4

init -1 python:   #create sound channels for simultanious sfx playback
        renpy.music.register_channel("sound1", "sfx", False)
        renpy.music.register_channel("sound2", "sfx", False)
        renpy.music.register_channel("sound3", "sfx", False)
        renpy.music.register_channel("sound4", "sfx", False)
        renpy.music.register_channel("sound5", "sfx", False)
        renpy.music.register_channel("sound6", "sfx", False)
        renpy.music.register_channel("sound7", "sfx", False)
        renpy.music.register_channel("sound8", "sfx", False)
        renpy.music.register_channel("sound9", "sfx", False)