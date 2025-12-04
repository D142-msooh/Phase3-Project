from Database import get_connection

def create_profile():
    conn = get_connection()
    cursor = conn.cursor()


    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    main_goal = input("main goal (money/discipline/skill): ")
    free_hours = int(input("Enter the number of free hours: "))
    
    cursor.execute("INSERT INTO users (name, age, main_goal, free_hours) VALUES (?, ?, ?, ?)", 
                   (name, age, main_goal, free_hours))
    user_id = cursor.lastrowid

    skills_input = input("Enter skills (comma separated): ")
    skills_list = [s.strip() for s in skills_input.split(",")]

    for skill in skills_list:
        cursor.execute("INSERT INTO skills (user_id, skill) VALUES (?, ?)", (user_id, skill))

    conn.commit()
    print("\nProfile created successfully!\n")