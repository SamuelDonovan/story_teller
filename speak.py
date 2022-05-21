from gtts import gTTS

message = """**Four big guys** left their table to hustle over and pay their respects to the two celebrities. No words were exchanged. But there was ample backslapping and bro hugs.

Sky had been there enough to be able to predict Sam's response to the pregreeting session. Sam would say, "Hang on, fellas," and drudge himself up to a swaying, foam-pegged grin as he reached across the table to give each of the young athletes cuttingly hard handshakes.

One of the men, a hulking youth named Cotton who'd gone from a modest school in East Brunswick, New Jersey to a junior college and eventually to the pros, said to Sam and Sky, "Hey, this is who you should draft. C'mon, c'mon." And that was the ritual, too: Sam and Sky would play along for a moment, then laughingly push him away. Real comedians, the kids here.

Samantha, perhaps being overserved and feeling properly ready to roll, also said, "Hey, this is who you should draft." She giggled and tried to punctuate Cotton's pitch. "C'mon, we'll all come to camp."

That did it! Cotton, and his two friends, were so delighted they were reeling with laughter. They were trying to articulate something when the booze finally got to Cotton. His pals both stepped back and let him try to deliver the pitch.

"What the man said, Sam. We'll come to you. But not in camp. How you doin'?"

"I'm doing fine, Cotton."

"Whyn't y'all summa us up at draft-time?"

"Okay," Sam said. "Have a seat, Cotton. Think about where you'd like to live and go to college. And what all kind of experiences you'd like to have."

That did it. Cotton was melting, but one of the other young men was able to recount what was very, very funny. Cotton stayed on his feet. But that did it! Cotton staggered back to his young Saturday night pals flexing his tremendous biceps as he laughed, sparking the rest of the group.

Then the place went about its boisterous Saturday night routine. An NFL bass player was supposed to be playing later, too, but the band was afraid to cut into the pregame flavor by booking him too early. So the keyboard player worked both the
"""

def speak(msg):
    tts = gTTS(text=msg, lang="en")            
    tts.save("message.mp3")

speak(message)