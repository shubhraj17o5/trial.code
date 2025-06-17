# Mad Libs Generator
# A fun game where users provide words to create silly stories!

def get_user_input():
    """Get all the words needed from the user"""
    print("Welcome to Mad Libs Generator!")
    print("I'll ask you for some words, and then create a funny story!")
    print("-" * 50)
    
    # Get words from user
    adjective1 = input("Enter an adjective (describing word): ")
    noun1 = input("Enter a noun (person, place, or thing): ")
    verb1 = input("Enter a verb (action word): ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    verb2 = input("Enter another verb: ")
    color = input("Enter a color: ")
    animal = input("Enter an animal: ")
    food = input("Enter a type of food: ")
    number = input("Enter a number: ")
    
    return adjective1, noun1, verb1, adjective2, noun2, verb2, color, animal, food, number

def create_story1(adj1, noun1, verb1, adj2, noun2, verb2, color, animal, food, number):
    """Create the first mad libs story"""
    story = f"""
    🎉 THE CRAZY SCHOOL DAY 🎉
    
    Yesterday was a {adj1} day at school! During lunch, I decided to {verb1} 
    to the {noun1} with my {adj2} friend. We saw a {color} {animal} eating 
    {food} near the {noun2}. It was so funny that we {verb2} for {number} 
    minutes straight! What a {adj1} adventure!
    """
    return story

def create_story2(adj1, noun1, verb1, adj2, noun2, verb2, color, animal, food, number):
    """Create the second mad libs story"""
    story = f"""
    🚀 SPACE ADVENTURE 🚀
    
    Captain {noun1} was on a {adj1} mission to planet {noun2}. The spaceship 
    could {verb1} at {number} miles per hour! On the planet, they discovered 
    {color} aliens who loved to eat {food}. The aliens were very {adj2} and 
    taught the captain how to {verb2} like a {animal}. What an amazing journey!
    """
    return story

def create_story3(adj1, noun1, verb1, adj2, noun2, verb2, color, animal, food, number):
    """Create the third mad libs story"""
    story = f"""
    🏰 MAGICAL KINGDOM 🏰
    
    In the {adj1} kingdom of {noun1}, there lived a {adj2} wizard who could 
    {verb1} anything into {food}! One day, a {color} {animal} came to the 
    {noun2} asking for help. The wizard decided to {verb2} a magic spell 
    exactly {number} times, and something incredible happened!
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