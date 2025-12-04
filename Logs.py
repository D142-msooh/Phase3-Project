from Database import get_connection
from datetime import datetime
from Recommendation import get_user

#Add progress log
def add_log():
    user = get_user()
    if user == None:
        print("profile not found. Sign in to create profile.")
        return
    
    print("Welcome back", user["name"])

    log = input("what did you achieve today?.")
    date = datetime.now().strftime("%Y-%m-%d")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO logs (user_id, entry, date) VALUES (?, ?, ?)", 
                   (user["id"], log, date))
    
    conn.commit()
    conn.close()

    print("Log added successfully!:\n")


def view_logs():
    user = get_user()
    if user == None:
        print("profile not found. Sign in to create profile.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    #add user to database
    cursor.execute("SELECT entry, date FROM logs WHERE user_id = ?", (user["id"],))
    rows = cursor.fetchall()
        
    print("\nLogs:\n")
    for entry, date in rows:
            

    conn.close()
    print()


