import mysql.connector
from datetime import datetime

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nightdespair22!",
    database="bank_app"
)
cursor = conn.cursor()

def get_balance():
    cursor.execute("""
        SELECT 
            IFNULL(SUM(CASE WHEN type='deposit' THEN amount ELSE -amount END), 0)
        FROM transactions
    """)
    result = cursor.fetchone()
    return result[0]

def show_balance():
    balance = get_balance()
    print(f"Your balance is ₱{balance:.2f}")

def deposit():
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount.")
            return
        cursor.execute("""
            INSERT INTO transactions (type, amount)
            VALUES (%s, %s)
        """, ('deposit', amount))
        conn.commit()
        print("Deposit successful.")
    except ValueError:
        print("Please enter a valid number.")

def withdraw():
    try:
        amount = float(input("Enter amount to withdraw: "))
        balance = get_balance()
        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            cursor.execute("""
                INSERT INTO transactions (type, amount)
                VALUES (%s, %s)
            """, ('withdraw', amount))
            conn.commit()
            print("Withdrawal successful.")
    except ValueError:
        print("Please enter a valid number.")

def show_transactions():
    print("\nTransaction History:")
    cursor.execute("SELECT type, amount, timestamp FROM transactions ORDER BY id DESC")
    for t_type, amount, time in cursor.fetchall():
        print(f"{t_type.capitalize():<10} ₱{amount:.2f} at {time}")

# Main menu
is_running = True
while is_running:
    print("\nWelcome to Bangko")
    print("*1: Show Balance")
    print("*2: Deposit")
    print("*3: Withdraw")
    print("*4: Show Transactions")
    print("*5: Exit")
    choice = input("What do you want to do? ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        show_transactions()
    elif choice == '5':
        is_running = False
    else:
        print("Invalid choice.")

print("Goodbye!")
cursor.close()
conn.close()
