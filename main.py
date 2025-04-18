from pet import Pet

def main():
    # Get pet name from user
    pet_name = input("What would you like to name your pet? ")
    
    # Create a pet object
    my_pet = Pet(pet_name)
    print(f"\nCongratulations! You've adopted {pet_name}!")
    
    # Main interaction loop
    while True:
        my_pet.get_status()
        
        print("\nWhat would you like to do with your pet?")
        print("1. Feed")
        print("2. Sleep")
        print("3. Play")
        print("4. Train a new trick")
        print("5. Show tricks")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            my_pet.eat()
        elif choice == '2':
            my_pet.sleep()
        elif choice == '3':
            my_pet.play()
        elif choice == '4':
            trick = input("What trick would you like to teach? ")
            my_pet.train(trick)
        elif choice == '5':
            my_pet.show_tricks()
        elif choice == '6':
            print(f"\nGoodbye! Take care of {pet_name}!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()