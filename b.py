# ============================= 
#     Bus Ticket System 
# ============================= 

class Bus:
    def __init__(self, bus_id, origin, destination, time, total_seats, ticket_price):
        self.bus_id = bus_id
        self.origin = origin
        self.destination = destination
        self.time = time
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.seats = [None] * total_seats  # None means seat is available

    def display_schedule(self):
        print(f"Bus ID: {self.bus_id} | {self.origin} -> {self.destination} | Time: {self.time} | Price: ${self.ticket_price}")

    def available_seats(self):
        return [i + 1 for i, seat in enumerate(self.seats) if seat is None]

    def reserve_seat(self, seat_number, passenger_name):
        if 1 <= seat_number <= self.total_seats:
            if self.seats[seat_number - 1] is None:
                self.seats[seat_number - 1] = passenger_name
                print(f"✅ Seat {seat_number} successfully reserved for {passenger_name}")
            else:
                print("❌ Seat already reserved!")
        else:
            print("❌ Invalid seat number!")

    def cancel_reservation(self, seat_number):
        if 1 <= seat_number <= self.total_seats:
            if self.seats[seat_number - 1] is not None:
                print(f"✅ Reservation for seat {seat_number} canceled.")
                self.seats[seat_number - 1] = None
            else:
                print("❌ Seat was not reserved.")
        else:
            print("❌ Invalid seat number!")

    def issue_ticket(self, seat_number):
        if 1 <= seat_number <= self.total_seats:
            passenger = self.seats[seat_number - 1]
            if passenger:
                print(f"""
🎫 Ticket Issued:
------------------------
Passenger Name : {passenger}
Bus ID         : {self.bus_id}
Route          : {self.origin} -> {self.destination}
Departure Time : {self.time}
Seat Number    : {seat_number}
Ticket Price   : ${self.ticket_price}
------------------------
""")
            else:
                print("❌ Seat not reserved yet.")
        else:
            print("❌ Invalid seat number!")


# ============================= 
#     Bus Management 
# ============================= 

# Sample buses with ticket prices
buses = [
    Bus("B101", "City A", "City B", "10:00 AM", 5, 25.0),
    Bus("B202", "City C", "City D", "2:30 PM", 4, 30.0),
    Bus("B303", "City E", "City F", "6:15 PM", 6, 35.0)
]

# Find bus by ID
def find_bus_by_id(bus_id):
    for bus in buses:
        if bus.bus_id.lower() == bus_id.lower():
            return bus
    return None


# ============================= 
#     Main Menu Loop 
# ============================= 

def main_menu():
    while True:
        print("\n=== 🚌 Bus Ticket Reservation System ===")
        print("1. View All Bus Schedules")
        print("2. View Available Seats")
        print("3. Reserve a Seat")
        print("4. Cancel Reservation")
        print("5. Issue Ticket")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("\n--- Bus Schedules ---")
            for bus in buses:
                bus.display_schedule()

        elif choice == '2':
            bus_id = input("Enter Bus ID: ")
            bus = find_bus_by_id(bus_id)
            if bus:
                seats = bus.available_seats()
                print(f"🪑 Available Seats in {bus.bus_id}: {seats if seats else 'No seats available.'}")
            else:
                print("❌ Bus not found!")

        elif choice == '3':
            bus_id = input("Enter Bus ID: ")
            bus = find_bus_by_id(bus_id)
            if bus:
                name = input("Enter passenger name: ")
                try:
                    seat = int(input("Enter seat number to reserve: "))
                    bus.reserve_seat(seat, name)
                except ValueError:
                    print("❌ Seat number must be a number.")
            else:
                print("❌ Bus not found!")

        elif choice == '4':
            bus_id = input("Enter Bus ID: ")
            bus = find_bus_by_id(bus_id)
            if bus:
                try:
                    seat = int(input("Enter seat number to cancel: "))
                    bus.cancel_reservation(seat)
                except ValueError:
                    print("❌ Seat number must be a number.")
            else:
                print("❌ Bus not found!")

        elif choice == '5':
            bus_id = input("Enter Bus ID: ")
            bus = find_bus_by_id(bus_id)
            if bus:
                try:
                    seat = int(input("Enter seat number to issue ticket: "))
                    bus.issue_ticket(seat)
                except ValueError:
                    print("❌ Seat number must be a number.")
            else:
                print("❌ Bus not found!")

        elif choice == '6':
            print("👋 Exiting system. Thank you!")
            break

        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")

# Run the program
main_menu()
