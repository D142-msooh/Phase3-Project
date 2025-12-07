from Logs import add_log, view_logs
from profile import create_profile
from Recommendation import generate_recommendations, get_user
from Tables import create_table

def main():
    create_table()

    while True:
        print("1. Create Profile")
        print("2. view recommendations")
        print("3. Add Progress Log")
        print("4. View Logs")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_profile()
        elif choice == "2":
            profile = get_user()
            if profile:
                generate_recommendations(
                    profile["name"],
                    profile["age"],
                    profile["main_goal"],
                    profile["free_hours"]
                )
            else:
                print("No profile found. Please create a profile first.")
        elif choice == "3":
            add_log()
        elif choice == "4":
            view_logs()
        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
main()
