# src/app/gui/main_feed.py

import random
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QFrame
from PyQt6.QtCore import pyqtSignal
from app.posts.image_post import ImagePostWidget
from app.posts.text_post import TextPostWidget
from app.gui.tool_bar import ToolBar

# your pastel border‑colors
_FEED_COLORS = [
    "#8ED2D6", "#D6A8E8", "#A8E88E", "#E8B48E", "#F7C8E0",
    "#C8F7DC", "#F9F48E", "#B4E1FA", "#EFC8A8", "#D6F5A3",
]

_TEXT_SAMPLES = [
    "just microwaved my phone charger again. at this point i think it’s charging *me* back.",
    "my cat just knocked my water over, stared me in the eyes, then walked away. she owns this house.",
    "ever just open the fridge 6 times hoping anxiety turned into food? spoiler: it didn’t.",
    "was crying on the floor and my Roomba bumped into me like 'move loser'. even robots hate me.",
    "i told my mom i’m fine and she asked 'f-i-n-e or actually fine?' ...i'm not fine.",
    "why does kellen’s app need access to my flashlight and emotional trauma??",
    "accidentally sent 'ur cute' to the company group chat. brb moving to a new country.",
    "used Kellen’s app and now my calendar just says 'bad idea' every day at 3pm.",
    "people keep saying ‘touch grass’ like grass ever fixed my trust issues.",
    "ate a full pizza alone and now I’m lying on the floor like a crime scene outline.",
    "every time i try to be productive, my bed whispers 'but what if we just… didn’t?'",
    "the guy next to me on the bus is watching a documentary about serial killers and eating string cheese like it’s a thriller. should i be concerned or impressed?",
    "kellen told me the app was 'feature complete' but it crashes when i *think* about opening it.",
    "googled 'am i dying' and webmd just showed me a mirror. rude.",
    "tried meditation but my brain screamed 'remember that thing from 2009?' for 20 minutes straight.",
    "texted 'i miss u' to my ex. autocorrect changed it to 'i massaged u'. somehow worse?",
    "kellen said 'trust the process' but the process gave my phone PTSD.",
    "why does every man over 30 own a couch that looks like it came with the apartment and a mysterious towel no one uses?",
    "looked in the mirror and thought ‘damn who hurt you’ and it turns out it was mostly me.",
    "bought a candle labeled 'peaceful forest' and now my room smells like wet tree sadness and lies.",
    "why did i just apologize to the chair i bumped into. am i too polite or deeply broken?",
    "i just watched a raccoon steal someone's lunch at the park and honestly... he earned it.",
    "tried to flirt and accidentally said 'have a good meal' at a funeral. i’m never speaking again.",
    "the barista asked how my day was going and i said 'emotionally or logistically?'",
    "my therapist said 'let’s unpack that' and i literally screamed 'do we have to??'",
    "lil blaze dropped a track so fire my phone restarted. like full system reboot.",
    "got ghosted by someone who said 'i’m not like other people' and they were right. worse.",
    "why does every adult chore feel like defeating a miniboss? laundry. taxes. calling the dentist.",
    "me: i should go to bed early. also me at 3am: what’s the difference between a void and an abyss?",
    "accidentally liked a 2016 post while stalking. might as well send a carrier pigeon at this point.",
    "special k out here rapping about heartbreak like he personally invented disappointment.",
    "i sneezed and my air fryer turned off. this apartment is haunted or i’m the problem.",
    "you ever eat a meal so sad it feels like a breakup? like the sandwich knew i was down bad.",
    "i tried to meditate but my brain brought up that one time in 7th grade i called my teacher 'mom'.",
    "someone said 'you’re not ugly, you’re just not photogenic' and like... thanks?",
    "lil blaze said 'i never cry, just sweat from the soul' and i felt that in my organs.",
    "my plants are judging me. one of them literally turned away from me. i get it. i’m unstable.",
    "why do i have a favorite burner on the stove? why do i trust the front left more than the others?",
    "me: i’m doing great. also me: crying because the pizza delivery guy said 'enjoy your night' too sincerely.",
    "special k rhymed 'existential dread' with 'bread' and now i'm legally his fan forever.",
]

_COMMENT_SAMPLES = [
    "yo this hit too hard lmao",
    "not me reading this while crying in target",
    "kellen stay getting roasted and for what 😂",
    "nah cause why is this literally me",
    "someone tag kellen he needs to fix this mess",
    "uninstalling reality brb",
    "ok but why is this so true it hurts",
    "literally thought this was a cry for help at first",
    "can’t believe i’m laughing and spiraling at the same time",
    "tell me why my therapist said the exact same thing",
    "this app is giving emotional whiplash",
    "i read this in my anxiety voice",
    "kellen needs to be stopped",
    "was having a good day until i saw this",
    "this app knows too much",
    "just got personally attacked by a notification",
    "kellen’s app should come with a warning label",
    "i came here to relax and instead found trauma",
    "so we’re all collectively losing it huh",
    "delete this before it sees me",
    "i laughed, then cried, then laughed again",
    "if i had a dollar for every time i said 'same', i could retire",
    "this comment section is my therapy now",
    "why is this post my autobiography",
    "who gave you the right to be this accurate",
    "lowkey offended at how called out i feel",
    "this just summoned every intrusive thought i’ve ever had",
    "somehow this post made me hungry and sad",
    "i didn’t ask to be seen like this",
    "kellen owes me emotional damages",
    "stop making content based on my inner monologue",
    "the app just blinked and now i’m questioning everything",
    "this is why i don’t go outside",
    "honestly this explains everything and nothing",
    "i showed this to my plant and even it judged me",
    "sending this to my therapist with no context",
    "reading this felt like a targeted ad for depression",
    "how does this post have more self-awareness than me",
    "this unlocked a memory i repressed on purpose",
    "i’m both the post and the comment section",
    "if this was a movie it’d be a tragedy-comedy",
    "just gonna pretend i didn’t read that",
    "i opened the app and immediately regretted it",
    "you ever scroll and get emotionally mugged?",
    "this app is running a roast session in real time",
    "the way this dragged me out of denial",
    "i’m suing for emotional sabotage",
    "when i said ‘read me’ i didn’t mean like a book",
    "this post is holding a mirror up to my chaos",
    "every time i use this app it gets worse in the best way",
    "kellen built this app out of spite and emotional residue",
    "this feels like a meme and a cry for help simultaneously",
    "i’m only here for the comments tbh",
    "at this point, the app should offer a support hotline",
    "this is funnier if you haven’t slept in 36 hours",
    "you ever feel so seen you get uncomfortable?",
    "what kind of emotional horcrux is this?",
    "this comment section is just a group therapy circle",
    "i don’t remember subscribing to this chaos",
    "the app is sentient and it’s bullying me",
    "honestly just glad we’re all spiraling together",
]



class MainFeedWidget(QWidget):
    post_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        # dusty‑rose page background
        self.setStyleSheet("background-color: #C46A6A;")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        toolbar = ToolBar(self, title="Kellen's App", back=False)
        layout.addWidget(toolbar)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        layout.addWidget(scroll)

        container = QWidget()
        vbox = QVBoxLayout(container)
        vbox.setContentsMargins(16, 16, 16, 16)
        vbox.setSpacing(16)

        assets = Path(__file__).resolve().parents[3] / "assets"

        for idx in range(25):
            color = _FEED_COLORS[idx % len(_FEED_COLORS)]
            if random.choice([True, False]):
                post = ImagePostWidget(str(assets / f"image_{random.randint(1,9)}.jpg"),
                                       border_color=color)
            else:
                post = TextPostWidget(random.choice(_TEXT_SAMPLES),
                                      border_color=color)
            post.clicked.connect(self.post_clicked)
            vbox.addWidget(post)

        vbox.addStretch()
        scroll.setWidget(container)
