##This is an example scene
##It teaches you about making mods, and is also a code example itself!

image bg cafetria ="BG cafeteria.png"

#Each section needs a label, this is how we will call the scene in or parts of the script
label monika_arc:
    stop music fadeout 2.0

    
    scene black
    with dissolve_scene_full

    "Welcome to Project Monika!"
    "This mod starts a year before the events of Doki Doki Literature Club."
    "This mod currently only supports a monika route and other routes may be implemented in the furture."
    "DISCLAMER: This mod is non-canon."
    
    scene bg class_day 
    with dissolve_scene_full
    play music t2
       
    "I sat silently leant over my desk as the teacher droned on about the importance of education."
    "As the teacher's lecture ends I hear the lunchbell go and notice something out of the corner of my eye."
    "Looking up I see the figure of a girl."
    "I sat up straight to take in the full view of who was in front of me."
    
    
    m "Hello [player]!"

    p "M-Monika!"
    show monika 1a at t11 zorder 2

    "Monika was probably the most popular girl in the class-smart, beautiful, athletic."
    "Basically completely out of my leauge."
    "I wondered why she would want to talk to me."

    p "So... Monika... What brings you here?"

    m 1j "Oh nothing~"
    m 2j "I was just wondering if you wanted to, you know..."
    m 5 "Have lunch together..."

    "I almost fell out of my chair."
    "I never thought that of all the people in this school Monika would be the one to ask me out for lunch."
    "My heart raced for a moment but I quickly dismissed the idea of Monika having any interest in me."

    p "S-sure."
    p "Beats eating lunch alone I guess..."

    m 1k "Great!"
    m "Let's get going!"

    "Monika grabs my hand and leads me towards the school cafeteria."

    scene bg cafeteria
    with dissolve_scene_full

    "Before I knew it I was having lunch with Monika."
    show monika 1a at t11 zorder 2
 
    m 1j "Thank you for having lunch with me today [player]!"
    p "Um... No problem."
    
    "I spent lunch break with Monika discussing many things."
    "And before we knew it lunch break was over and we headed back to class."
    
    scene bg corridor
    with dissolve_scene_full

    "Before we knew it we were right outside the classroom and before I could enter Monika stopped me and grabbed the end of my sleeve."

    show monika 1b at t11 zorder 2
 
    m "Hey [player]..."
    m 3k "Umm... Would you walk home with me today?"
show monika 5 at t11 zorder 2

default will_walk_home = False

menu:
    m "So... Will you?"
    "Yes":
        $will_walk_home = True
        m 2k "Yay!"
        m "Thank you so much [player]!"
    "No":
        m 2p "Aww... I was really looking forward to it..."

if not will_walk_home:
    scene white
    with dissolve(1.0)

    return

else:
    scene bg residential_day
    with dissolve_scene_full
    stop music fadeout 2.0
    play music "5_monika.ogg"

    ""
    

    return

