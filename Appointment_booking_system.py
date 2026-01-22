appointments = []

def book_appointment():
    name = input("Enter client name: ")
    date = input("Enter appointment date: ")
    time = input("Enter appointment time: ")
    appointments.append({"name": name, "date": date, "time": time})
    print("Appointment booked")

def view_appointments():
    if not appointments:
        print("No appointments available")
    else:
        for appt in appointments:
            print(appt["name"], "-", appt["date"], "-", appt["time"])

def main():
    while True:
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            book_appointment()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
