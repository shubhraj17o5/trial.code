# Genre-Based Mad Libs Generator
# Choose your favorite genre and create stories based on it!

def choose_genre():
    """Let user choose their preferred genre"""
    print("🎭 CHOOSE YOUR STORY GENRE 🎭")
    print("1. Horror/Scary")
    print("2. Comedy/Funny") 
    print("3. Adventure/Action")
    print("4. Romance/Love")
    print("5. Sci-Fi/Space")
    print("6. Fantasy/Magic")
    print("7. School/College")
    print("8. Sports")
    print("-" * 40)
    
    choice = input("Enter your choice (1-8): ")
    return choice

def get_words_for_genre(genre):
    """Get words specific to the chosen genre"""
    print(f"\nGreat choice! Now I need some words for your story...")
    print("Don't overthink - just say the first thing that comes to mind!")
    print("-" * 50)
    
    if genre == "1":  # Horror
        adjective1 = input("Enter a scary adjective (creepy, haunted, dark): ")
        place = input("Enter a spooky place (cemetery, basement, forest): ")
        sound = input("Enter a scary sound (scream, howl, creak): ")
        object_item = input("Enter an object (candle, mirror, book): ")
        
    elif genre == "2":  # Comedy
        adjective1 = input("Enter a funny adjective (silly, ridiculous, goofy): ")
        place = input("Enter a place (kitchen, bathroom, mall): ")
        sound = input("Enter a funny sound (giggle, snort, burp): ")
        object_item = input("Enter an everyday object (banana, shoe, spoon): ")
        
    elif genre == "3":  # Adventure
        adjective1 = input("Enter an exciting adjective (dangerous, thrilling, epic): ")
        place = input("Enter an adventure location (jungle, mountain, cave): ")
        sound = input("Enter an action sound (crash, boom, splash): ")
        object_item = input("Enter a tool/weapon (sword, rope, map): ")
        
    elif genre == "4":  # Romance
        adjective1 = input("Enter a romantic adjective (beautiful, charming, lovely): ")
        place = input("Enter a romantic place (beach, cafe, garden): ")
        sound = input("Enter a gentle sound (whisper, sigh, melody): ")
        object_item = input("Enter a romantic object (flower, letter, ring): ")
        
    elif genre == "5":  # Sci-Fi
        adjective1 = input("Enter a futuristic adjective (advanced, alien, robotic): ")
        place = input("Enter a sci-fi place (spaceship, planet, laboratory): ")
        sound = input("Enter a tech sound (beep, zap, hum): ")
        object_item = input("Enter a tech object (laser, computer, robot): ")
        
    elif genre == "6":  # Fantasy
        adjective1 = input("Enter a magical adjective (enchanted, mystical, ancient): ")
        place = input("Enter a fantasy place (castle, forest, tower): ")
        sound = input("Enter a magical sound (chant, spell, roar): ")
        object_item = input("Enter a magical object (wand, potion, crystal): ")
        
    elif genre == "7":  # School
        adjective1 = input("Enter a school-related adjective (smart, confused, sleepy): ")
        place = input("Enter a school place (classroom, cafeteria, library): ")
        sound = input("Enter a school sound (bell, chatter, pencil): ")
        object_item = input("Enter a school object (book, calculator, backpack): ")
        
    else:  # Sports
        adjective1 = input("Enter a sports adjective (fast, strong, competitive): ")
        place = input("Enter a sports place (stadium, gym, field): ")
        sound = input("Enter a sports sound (cheer, whistle, thud): ")
        object_item = input("Enter sports equipment (ball, bat, helmet): ")
    
    # Common words for all genres
    name = input("Enter a character name: ")
    animal = input("Enter an animal: ")
    color = input("Enter a color: ")
    number = input("Enter a number (1-50): ")
    verb = input("Enter a past tense verb (ran, jumped, fell): ")
    food = input("Enter a food: ")
    
    return adjective1, place, sound, object_item, name, animal, color, number, verb, food

def create_genre_story(genre, words):
    """Create story based on chosen genre"""
    adj1, place, sound, obj, name, animal, color, number, verb, food = words
    
    if genre == "1":  # Horror
        story = f"""
        👻 THE {adj1.upper()} NIGHT 👻
        
        It was a {adj1} night when {name} decided to explore the old {place}. 
        As they walked deeper inside, they heard a strange {sound} coming from behind 
        a {color} door. When {name} opened it, they found a {adj1} {animal} holding 
        a mysterious {obj}!
        
        The {animal} suddenly {verb} and made the {sound} noise {number} times! 
        {name} was so scared that they dropped their {food} and ran out of the 
        {place} as fast as they could. They never returned to that {adj1} place again!
        
        Some say you can still hear the {sound} echoing from the {place} on {adj1} nights...
        """
        
    elif genre == "2":  # Comedy
        story = f"""
        😂 THE {adj1.upper()} DAY 😂
        
        {name} woke up feeling {adj1} and decided to go to the {place}. While there, 
        they accidentally {verb} into a {color} {animal} who was eating {food}! 
        
        The {animal} made a loud {sound} and started chasing {name} around with a {obj}! 
        Everyone in the {place} was laughing as {name} ran in circles {number} times, 
        still holding their {food}!
        
        From that day on, {name} became famous as "the person who {verb} into a {animal}" 
        and the {adj1} story is still told at the {place}!
        """
        
    elif genre == "3":  # Adventure
        story = f"""
        ⚔️ THE {adj1.upper()} QUEST ⚔️
        
        Explorer {name} embarked on a {adj1} journey to the legendary {place}. 
        Armed with only a {obj} and some {food}, they were ready for anything!
        
        Deep in the {place}, {name} encountered a {color} {animal} guarding a treasure. 
        The {animal} made a fierce {sound} and attacked! {name} {verb} {number} times 
        to dodge the creature's attacks.
        
        Using their {obj} skillfully, {name} defeated the {adj1} {animal} and claimed 
        the treasure. They returned home as a hero, and everyone at the {place} 
        celebrated their {adj1} victory!
        """
        
    elif genre == "4":  # Romance
        story = f"""
        💕 A {adj1.upper()} LOVE STORY 💕
        
        {name} was having a {adj1} evening at the {place} when they met the most 
        wonderful person. They were sitting by a {color} {animal}, sharing {food} 
        and listening to the gentle {sound} in the background.
        
        Their new love gave {name} a special {obj} and they {verb} together under 
        the stars. They promised to meet at the {place} again in {number} days.
        
        Every time {name} hears that {sound} or sees a {color} {animal}, they remember 
        that {adj1} night and smile. True love found at the {place}!
        """
        
    elif genre == "5":  # Sci-Fi
        story = f"""
        🚀 THE {adj1.upper()} MISSION 🚀
        
        Commander {name} was piloting their {adj1} ship to the {place} when they 
        received a strange {sound} signal. On the planet, they discovered a {color} 
        {animal} that had evolved to eat {food}!
        
        Using their advanced {obj}, {name} tried to communicate with the creature. 
        The {animal} {verb} {number} times and made the {sound} noise, which their 
        translator decoded as "Welcome to our world!"
        
        {name} spent days learning about this {adj1} species and their {place}. 
        This discovery would change space exploration forever!
        """
        
    elif genre == "6":  # Fantasy
        story = f"""
        🧙‍♂️ THE {adj1.upper()} SPELL 🧙‍♂️
        
        Wizard {name} was practicing magic in their {adj1} {place} when something 
        went wrong. They accidentally turned their {food} into a {color} {animal} 
        using their powerful {obj}!
        
        The {animal} started making a magical {sound} and {verb} around the room 
        {number} times. Every time it made the {sound}, more {food} appeared!
        
        Now {name} has a {adj1} pet {animal} and unlimited {food}. Other wizards 
        come from far away to learn this {adj1} spell at the famous {place}!
        """
        
    elif genre == "7":  # School
        story = f"""
        📚 THE {adj1.upper()} SCHOOL DAY 📚
        
        Student {name} was having a {adj1} day at school. During lunch in the {place}, 
        they accidentally {verb} and spilled {food} all over their {obj}!
        
        Suddenly, the school's pet {color} {animal} appeared and started eating the 
        {food}! The {animal} made a happy {sound} and followed {name} around for 
        {number} minutes.
        
        The teacher was so amused that they made {name} and the {animal} the official 
        {place} cleanup crew. Now every {adj1} day, they work together!
        """
        
    else:  # Sports
        story = f"""
        🏆 THE {adj1.upper()} GAME 🏆
        
        Athlete {name} was preparing for the most {adj1} game of their career at the 
        {place}. They had trained with their lucky {obj} and eaten their favorite 
        {food} for breakfast.
        
        During the game, a {color} {animal} ran onto the field and made a loud {sound}! 
        {name} {verb} {number} times trying to avoid the {animal}, but ended up 
        scoring the winning point!
        
        The crowd went wild! {name} became known as the player who won the {adj1} 
        game with help from a {animal}. The {place} retired their {obj} in honor!
        """
    
    return story

def main():
    """Main function to run the Genre-Based Mad Libs Generator"""
    
    while True:
        print("🎪 WELCOME TO GENRE-BASED MAD LIBS! 🎪")
        print("="*50)
        
        # Choose genre
        genre = choose_genre()
        
        # Get words based on genre
        words = get_words_for_genre(genre)
        
        # Create and display story
        story = create_genre_story(genre, words)
        
        print("\n" + "🌟"*20 + " YOUR STORY " + "🌟"*20)
        print(story)
        print("🌟"*52)
        
        # Ask if user wants another story
        again = input("\nWant to create another story? (yes/no): ").lower()
        if again not in ['yes', 'y']:
            print("\n🎭 Thanks for playing! Hope you enjoyed your stories! 🎭")
            break
        print("\n" + "="*60)

# Run the program
if __name__ == "__main__":
    main()