"""
E.g 1
"""

file_size = 5 # in MB
file_type = "exe"

if file_size == 0:
    print("No file uploaded")
elif file_size > 5:
    print("File too large")
elif file_size not in ["jpg", "png", "pdf"]:
    print("invalid file type")
elif file_type == "exe":
    print("Executable file not allowed")
else:
    print("File uploaded successfully")


"""
TASK 1. BASIC PAYMENT PROCESSING SYSTEM
Write a python code that ask the user to enter the amount he wants to widthdraw

Conditions
1. If the amount is <= the balance, print("Payment successful")
2. If the amount is greater than the balance, print("Insufficient funds")
3. If the balance is <= 0, print("Invalid account balance")
4. If there is no network, print("Service temporary unavailable")
"""

"""
E.g 2. Scenerio: System Processing Multiple Users with Roles
"""

users = ["admin", "editor", "guest", "unknown"]
for user in users:
    if user == "admin":
        print("Full access granted")
    elif user == "editor":
        print("Edit access granted")
    elif user == "guest":
        print("Limited access granted")
    else:
        print("No access granted")



def welcome_message():
    print(f"Welcome, Emmmanuel!")

welcome_message()

"""
E.g 3. Scenerio: Order Notification System
"""

def notify_user(name, status):
    if status == "Paid":
        print(f"Hello {name}, your order is being processed.")

    elif status == "Pending":
        print(f"Hello {name}, your payment is pending.")

    elif status == "Cancelled":
        print(f"Hello {name}, your order was cancelled.")

    else:
        print(f"Hello {name}, invalid order status.")

notify_user("Emmanuel", "Paid")
notify_user("John", "Pending")
notify_user("Jane", "Cancelled")



"""
TASK 2.
write a python code for a student grading system that takes a parameter: student_score, attendance and the assignment_score.
CONDITIONS:
if the student_score is >= 70, print("Excellent. Grade: A"):
if the student_score is >= 60 and < 70, print("Good. Grade: B")
"""