from Database import get_connection
def get_user():
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM users ORDER BY id DESC LIMIT 1")
    return cursor.fetchone()

    conn.close()
    return row
def get_skills(user_id):
    conn = get_connection()
    

    cursor.execute("SELECT skill FROM skills WHERE user_id = ?", (user_id,))
    return [row[0] for row in cursor.fetchall()]

    conn.close()
    return skills

def generate_recommendations(name, age, main_goal, free_hours):
    user = get_user()
    if user is None:
        print("No profile found. Sign up first to create profile.")
        return
    
    user_id = user["id"]
    skills = get_skills(user_id)

    print(f"\nUser: {user['name']}, Age: {user['age']}, Main Goal: {user['main_goal']}, "
          f"Free Hours: {user['free_hours']}, Skills: {', '.join(skills)}")
    
    rec = []
    
    #Time suggestions
    if free_hours < 2:
        rec.append("Try microlearning to increase your free hours (5 minutes per day).")

    if free_hours >= 2:
        rec.append("You can handle a small weekly project.")

    #skill suggestions
    if "Python" in skills:
        rec.append("Build a python based code.")

    if "Java" in skills:
        rec.append("generate a Java code.")

    if "design" in skills:
        rec.append("Create 5 sample designs for different models.")

    if "writing" in skills:
        rec.append("create an article of atleast 250 words.")

    #goal suggestions
    if main_goal == "money":
        rec.append("select few job gigs (freelance, editing, correcting) according to your skill.")
    
    if main_goal == "skill":
        rec.append("join a free online course to enhance your preffered skill.")

    if main_goal == "discipline":
        rec.append("Create and start a daily tracker for your routines.")

    #Age setter and required skills
    if age < 18:
        rec.append("Request for schoolarships.")

    if age >= 18:
        rec.append("Try to learn a new skill or hobby.")

    #output expected
    print("\nRecommended Opportunities:\n")
    for r in rec:
        print("-",r)
        
    print()


    

    