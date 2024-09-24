import pyttsx3

def text_to_voice(rate, volume, voice, text):
    engine = pyttsx3.init()

    # Set rate and volume properties
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    # Set voice property
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)

    # engine.say(text)
    # engine.runAndWait()
    # engine.stop()

    # Save voice to a file
    engine.save_to_file(text, 'test.mp3')
    engine.runAndWait()

def recognize(voice):
    voice_map = {
        'm': {'rate': 40, 'volume': 1.2},
        'f': {'rate': 55, 'volume': 0.6},
        'r': {'rate': 100, 'volume': 0.8}
    }
    return voice_map.get(voice, {'rate': 80, 'volume': 1.0})

def excepter(voice):
    voice_map = {
        'm': 0,
        'f': 1
    }
    return voice_map.get(voice, None)

voice = input("Enter the voice you required (m for male, f for female, r for robot): ")
rate, volume = recognize(voice)
sound = excepter(voice)
if sound is None:
    ask = input("So you want a robotic voice? Enter m for male robot voice or f for female robot voice: ")
    sound = excepter(ask)

text = """It was a busy night at my restaurant, Bella Vita, which my family had owned and operated for generations. I, Alessandro, had taken over the restaurant a few years ago and had worked hard to modernize it and attract a new clientele. As I was greeting customers at the entrance, a group of six women walked in, led by a woman who introduced herself as Alexandra.

Alexandra was a tall, blonde woman in her mid-20s, who seemed to be the leader of the group. She was accompanied by five other women, all in their early 20s, who seemed to be her friends or followers. As they approached me, Alexandra began to explain that she required a table for six, and that the owner of the restaurant was a personal friend of hers.

I responded by asking for the name on the reservation, and Alexandra stared at me, seemingly taken aback by my question. She then explained that she hadn't made a reservation, but that the owner always kept a few tables open for special guests. I politely informed her that we couldn't seat anyone without a reservation, and that we were fully booked for the night.

Alexandra became agitated and instructed one of her friends to take a picture of me. She then announced that she would speak with the owner and ensure that I was either scrubbing toilets or fired by the end of the week. The other women in the group began to chime in, making snide comments about my job and my appearance.

I decided to play along and offered Alexandra a table, but only if she agreed to pay for the meal and drinks. I also informed her that the first three rounds of drinks would be on the house. Alexandra agreed, and I seated them at one of our VIP tables, which normally costs a few thousand dollars to reserve.

As the night went on, the group ordered several rounds of expensive cocktails and a variety of dishes from our menu. They seemed to be enjoying themselves, but I could sense that they were trying to take advantage of me and the restaurant.

At one point, one of the women asked me if I thought my life was meaningless because I was just a waiter. I was taken aback by her question, but I tried to remain professional and polite. However, I couldn't help but feel a sense of annoyance and frustration towards the group.

As the night wore on, the group's behavior became more and more erratic. They were loud, rude, and demanding, and they seemed to be trying to push my buttons. I tried to remain calm and composed, but it was becoming increasingly difficult.

One of the women, who seemed to be Alexandra's closest friend, began to flirt with me shamelessly. She was touching my arm and making suggestive comments, and I could tell that she was trying to get a rise out of me. I politely but firmly told her to stop, but she just laughed and continued to flirt.

The group's behavior was starting to attract attention from the other customers, and I could tell that they were starting to get uncomfortable. I tried to intervene, but Alexandra and her friends were too far gone.

Finally, I presented Alexandra with the bill, which came out to be over $4,000. She was shocked and outraged, and she began to argue with me about the cost of the meal. She claimed that the food was poor and the service was terrible, and she demanded that I reduce the bill by half.

I politely informed her that I couldn't reduce the bill, and that she needed to pay for the meal and drinks. Alexandra became angry and aggressive, and she began to yell at me in front of the other customers. I tried to remain calm and professional, but it was clear that the situation was escalating.

Just as it seemed like things were going to get out of hand, Alexandra's father arrived at the restaurant. He was a tall, imposing man who seemed to be used to getting his way. He demanded to speak with me, and I showed him the security footage of the group's behavior.

The footage clearly showed the group's rude and abusive behavior, and Alexandra's father was shocked and embarrassed. He apologized for his daughter's behavior and promised to pay for the meal and drinks. Alexandra was furious and humiliated, and she stormed out of the restaurant with her friends.

But the story doesn't end there. Over the next few weeks, Alexandra and her friends began to post negative reviews of my restaurant on social media. They claimed that the food was terrible and the service was worse, and they encouraged their friends to boycott the restaurant.

I tried to respond to the reviews, but it seemed like no matter what I did, the negative reviews just kept coming. The restaurant's reputation was starting to suffer, and I was getting worried.

I decided to take matters into my own hands and started to investigate Alexandra and her friends. I discovered that they were a group of entitled rich kids who were used to getting their way. They had a history of bullying and harassing people, and they seemed to take pleasure in causing trouble.

I decided to take a stand and started to fight back against the negative reviews. I posted my own reviews, telling the true story of what had happened that night. I also started to reach out to other business owners in the area, warning them about Alexandra and her friends.

Slowly but surely, the tide started to turn. People began to see through Alexandra's lies and started to support my restaurant. The negative reviews started to dwindle, and the positive reviews started to pour in.

In the end, Alexandra and her friends were left looking foolish and entitled. They had tried to take down my restaurant, but they had failed. I had stood up for myself and my business, and I had come out on top.

Update:

The incident with Alexandra and her friends had a profound impact on my restaurant. It taught me the importance of standing up for myself and my business, and it showed me that I couldn't let entitled customers walk all over me.

I started to implement new policies and procedures to deal with difficult customers. I trained my staff to be more assertive and confident, and I made sure that we were always prepared for any situation that might arise.

The incident also taught me the importance of social media. I realized that social media could be a powerful tool for promoting my restaurant, but it could also be a powerful tool for destroying it. I started to take social media more seriously, and I made sure that I was always monitoring my online presence.

In the end, the incident with Alexandra and her friends was a blessing in disguise. It taught me valuable lessons and helped me to grow as a business owner. It also helped me to develop a thicker skin and to be more confident in my abilities.

The Visits

Over the next few months, my restaurant started to attract a lot of attention. People were curious about the incident with Alexandra and her friends, and they wanted to see the restaurant that had stood up to them.

The visits started to pour in, and my restaurant was soon flooded with customers. I was thrilled, but I was also a little overwhelmed. I had to hire more staff to keep up with the demand, and I had to make sure that I was always on top of things.

The visits continued to pour in, and my restaurant became one of the most popular in the area. I was proud of what I had accomplished, and I knew that I owed it all to the incident with Alexandra and her friends.

The Final Confrontation

A few months after the incident, I received a call from Alexandra's father. He wanted to meet with me and apologize for his daughter's behavior. I agreed, and we met at a coffee shop near my restaurant.

Alexandra's father was a tall, imposing man who seemed to be genuinely sorry for what his daughter had done. He explained that Alexandra had always been a difficult child, and that he had tried to teach her right from wrong. He apologized for not doing a better job, and he promised to make it right.

I accepted his apology, and we parted ways. I never saw or heard from Alexandra again, but I knew that she had learned a valuable lesson. She had learned that she couldn't always get her way, and that sometimes she had to face the consequences of her actions.

Update:

The incident with Alexandra and her friends left a lasting legacy on my restaurant. It taught me the importance of standing up for myself and my business, and it showed me that I couldn't let entitled customers walk all over me.

It also taught me the importance of social media, and how it could be used to promote my restaurant or destroy it. I made sure to always monitor my online presence, and I made sure that I was always prepared for any situation that might arise.

The incident also taught me the importance of being confident and assertive. I realized that I couldn't let difficult customers push me around, and that I had to stand up for myself and my business.

In the end, the incident with Alexandra and her friends was a valuable learning experience. It taught me valuable lessons, and it helped me to grow as a business owner. It also helped me to develop a thicker skin, and to be more confident in my abilities.

Update:

In the end, the story of Alexandra and her friends is a cautionary tale about the dangers of entitlement and the importance of standing up for oneself. It shows that even the most difficult customers can be dealt with, and that sometimes it takes a little bit of courage and confidence to stand up for what is right.

It also shows that social media can be a powerful tool, but it can also be a powerful weapon. It can be used to promote a business or destroy it, and it's up to the business owner to make sure that they are always on top of things.

The story of Alexandra and her friends is a reminder that we should always stand up for ourselves and our businesses, and that we should never let entitled customers walk all over us. It's a reminder that we should always be confident and assertive, and that we should never be afraid to speak up for what is right.

Final Update:

The story of Alexandra and her friends is a long and complicated one, but it's a story that needs to be told. It's a story about entitlement and the dangers of social media, and it's a story about standing up for oneself and one's business.

It's a story that I will never forget, and it's a story that I will always cherish. It's a reminder of the importance of being confident and assertive, and it's a reminder of the dangers of entitlement.

In the end, the story of Alexandra and her friends is a story about growth and development. It's a story about learning from one's mistakes, and it's a story about becoming a better person and a better business owner.

It's a story that I hope will inspire others to stand up for themselves and their businesses, and it's a story that I hope will serve as a reminder of the importance of being confident and assertive."""
text_to_voice(rate, volume, sound, text)

