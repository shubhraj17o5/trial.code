# Mad Libs Generator
# A fun game where users provide words to create silly stories!

def get_user_input():
    """Get all the words needed from the user"""
    print("Welcome to Mad Libs Generator!")
    print("I'll ask you for some words, and then create a funny story!")
    print("Don't think too hard - just say the first thing that comes to mind!")
    print("-" * 50)
    
    # Get words from user with better examples
    adjective1 = input("Enter a FUNNY adjective (like crazy, silly, weird): ")
    person_name = input("Enter a person's name (friend, celebrity, or made-up): ")
    verb1 = input("Enter a verb ending in -ing (like running, dancing, singing): ")
    adjective2 = input("Enter an adjective describing size (huge, tiny, massive): ")
    place = input("Enter a place (school, park, kitchen, Mars): ")
    verb2 = input("Enter a past tense verb (jumped, screamed, laughed): ")
    color = input("Enter a color: ")
    animal = input("Enter an animal: ")
    food = input("Enter your favorite food: ")
    number = input("Enter a number between 1-100: ")
    
    return adjective1, person_name, verb1, adjective2, place, verb2, color, animal, food, number

def create_story1(adj1, name, verb1, adj2, place, verb2, color, animal, food, number):
    """Create the first mad libs story"""
    story = f"""
    🎉 THE WEIRD DAY 🎉
    
    My friend {name} had a {adj1} day yesterday! They were {verb1} to the 
    {place} when they saw a {adj2} {color} {animal}. The {animal} was eating 
    {food} and making weird noises! {name} got so surprised that they {verb2} 
    {number} times in a row. Everyone started laughing because it looked so {adj1}!
    
    From that day on, {name} always brings {food} whenever they go to the {place}.
    """
    return story

def create_story2(adj1, name, verb1, adj2, place, verb2, color, animal, food, number):
    """Create the second mad libs story"""
    story = f"""
    🚀 {name.upper()}'S ADVENTURE 🚀
    
    Captain {name} was {verb1} through space when their ship crashed on a {adj1} 
    planet. The planet was full of {adj2} {color} creatures that looked like {animal}s! 
    
    These alien-{animal}s only ate {food} and spoke by making {verb2} sounds. 
    Captain {name} had to learn their language by {verb1} around and eating 
    {food} for {number} days straight! 
    
    Finally, the {adj1} aliens helped fix the spaceship, and {name} returned home 
    with a stomach full of {food}!
    """
    return story

def create_story3(adj1, name, verb1, adj2, place, verb2, color, animal, food, number):
    """Create the third mad libs story"""
    story = f"""
    🏰 THE MAGIC RECIPE 🏰
    
    Wizard {name} lived in a {adj1} tower near the {place}. One day, while {verb1} 
    in the kitchen, they accidentally mixed {food} with {color} magic powder!
    
    POOF! A {adj2} {animal} appeared and started dancing around the room! 
    The {animal} {verb2} exactly {number} times before turning all the furniture 
    into {food}!
    
    Now wizard {name} has a pet {animal} and a house made entirely of {food}. 
    Visitors always leave the {place} feeling very {adj1} and very full!
    """
    return story

def main():
    """Main function to run the Mad Libs Generator"""
    
    while True:
        # Get user input
        words = get_user_input()
        
        print("\n" + "="*60)
        print("CHOOSE YOUR STORY:")
        print("1. The Crazy School Day")
        print("2. Space Adventure") 
        print("3. Magical Kingdom")
        print("="*60)
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        print("\n" + "*"*60)
        
        # Create story based on choice
        if choice == "1":
            story = create_story1(*words)
        elif choice == "2":
            story = create_story2(*words)
        elif choice == "3":
            story = create_story3(*words)
        else:
            print("Invalid choice! Using default story...")
            story = create_story1(*words)
        
        print(story)
        print("*"*60)
        
        # Ask if user wants to play again
        play_again = input("\nWould you like to create another Mad Libs story? (yes/no): ").lower()
        if play_again != "yes" and play_again != "y":
            print("\nThanks for playing Mad Libs! Have a great day! 🎉")
            break
        print("\n" + "="*60)

# Run the program
if __name__ == "__main__":
    main()