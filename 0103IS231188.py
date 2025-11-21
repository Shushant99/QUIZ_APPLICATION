from datetime import datetime
from random import shuffle
#note ( user name will be your emailm followed by your beanch and password will be "password123 by default" )
students = {}
def store_login_details():
    with open('student_login.txt', 'w') as file:
        for username in students:
            file.write(f"Username: {username}, Password: password123\n")
    print("Login details stored successfully!")

def register():
    name = input("Enter your name: ")
    branch = input("Enter your branch: ")
    age = input("Enter your age: ")
    fathers_name = input("Enter your father's name: ")
    mothers_name = input("Enter your mother's name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    tenth_percentage = input("Enter your 10th percentage: ")
    twelfth_percentage = input("Enter your 12th percentage: ")
    gender = input("Enter your gender: ")
    
# Create username using email prefix and a password default as 'password123'
    username = email.split('@')[0] +  branch
    password = "password123"
    students[username] = {
        'name': name,
        'age': age,
        'fathers_name': fathers_name,
        'mothers_name': mothers_name,
        'address': address,
        'phone': phone,
        'email': email,
        'tenth_percentage': tenth_percentage,
        'twelfth_percentage': twelfth_percentage,
        'gender': gender,
        'branch': branch
    }
    store_login_details()

    print(f"Student registered successfully! Your username is {username} and your default password is {password}")


def login():
    print("Login to your account")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        with open('student_login.txt', 'r') as file:
            for line in file:
                stored_username = line.split(',')[0].split(': ')[1]
                stored_password = line.split(',')[1].split(': ')[1].strip()
                if username == stored_username and password == stored_password:
                    print("Welcome to LNCT! You have successfully logged in")
                    return username
        print("Invalid username or password")
        return None
    except FileNotFoundError:
        print("No login details found. Please register first.")
        return None
def save_student_data():
        with open('student_data.txt', 'w') as file:
            for username, data in students.items():
                file_data = f"{username}|" + "|".join(f"{k}:{v}" for k,v in data.items())
                file.write(file_data + "\n")

def load_student_data():
        try:
            with open('student_data.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split('|')
                    username = parts[0]
                    data = {}
                    for item in parts[1:]:
                        key, value = item.split(':')
                        data[key] = value
                    students[username] = data
        except FileNotFoundError:
            pass
def show_profile(username):
    student = students[username]
    print("Profile Details:")
    for key, value in student.items():
        print(f"{key.capitalize()}: {value}")

def update_profile(username):
    student = students[username]
    print("Update Profile Details ")
    for key in student.keys():
        new_value = input(f"Enter new {key} (current: {student[key]}): ")
        if new_value:
            student[key] = new_value
    print("Profile updated successfully!")
def attempt_quiz(username):
    quiz_data = {
        'python': [],
        'dsa': [],
        'dbms': []
    }
    print("\nSelect subject for quiz:")

    print("1. Python\n2. DSA\n3. DBMS")
    choice = input("Enter choice (1-3): ")

    subject = {
        '1': 'python',
        '2': 'dsa',
        '3': 'dbms'
    }.get(choice)

    if not subject:
        print("Invalid choice")
        return
    
    quiz_data[subject] = []
    with open(f'{subject}_questions.txt', 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 3:
                question = parts[0]
                options = parts[1].split(' ')
                correct_answer = parts[2].strip()
                quiz_data[subject].append({
                    'question': question,
                    'answer': correct_answer
            })
            

    if not quiz_data[subject]:
        print(f"No questions available for {subject}")
        return

    score = 0
    total = len(quiz_data[subject])

    for entry in quiz_data[subject]:
        if len(entry) < 2:
            continue  
        question, correct_answer = entry
        print(f"\n{question}")
        print(f"\n{options}")
        answer = input("Your answer: ")
        if answer.lower() == correct_answer.lower():
            score += 1

    percentage = (score / total) * 100 if total > 0 else 0

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('quiz_results.txt', 'a') as file:
        file.write(f"{username}|{timestamp}|{subject}|{score}/{total}|{percentage}%\n")

    print(f"\nYour score: {score}/{total} ({percentage}%)")
def main():
    
    load_student_data()
    print("welcome to lnct regestation portal")
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register()
            store_login_details()
            save_student_data()
        elif choice == '2':
            
            username = login()
            
            if username:
                while True:
                    print("\n1. Show Profile\n2. Update Profile\n3. Logout\n4.Attempt test")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == '1':
                        show_profile(username)
                    elif sub_choice == '2':
                        update_profile(username)
                    elif sub_choice == '3':
                        print("Logged out successfully!")
                        break
                    elif sub_choice=='4':
                        attempt_quiz(username)
                    else:
                        print("Invalid choice, please try again.")
        elif choice == '3':
            print("Exiting")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
    

    