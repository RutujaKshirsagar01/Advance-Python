# Bus Ticket Reservation System 

class Bus:
    def __init__(self,bus_id,start_city,destination,time,total_seats,ticket_price,travel_date):
        self.bus_id=bus_id
        self.start_city=start_city
        self.destination=destination
        self.time=time
        self.total_seats=total_seats
        self.ticket_price=ticket_price
        self.travel_date=travel_date
        self.seats = [None] * total_seats #none means available sets

    def schedule(self): #Prints schedule of a bus (ID, route, time, date, price).
        print(f"Bus ID : {self.bus_id}   |   {self.start_city} -> {self.destination}    |   Time : {self.time}  |   Date : {self.travel_date}   |   Ticket Price : Rs.{self.ticket_price}")
    
    def available_seats(self):  #Uses list comprehension to return seat numbers that are not reserved.
        return [i + 1 for i , seat in enumerate(self.seats) if seat is None]

# This is a list comprehension a concise way to create a list.
#  It's used here to return the available seat numbers on a bus.
    
    def reserve_seats(self,seat_number,passenger_name):
        if 1 <= seat_number <= self.total_seats: #check if seat number is valid
            if self.seats[seat_number - 1]is None: #check if seat is available
                self.seats[seat_number - 1]=passenger_name #for reserve seat
                print(f"Seat No : {seat_number}  reserved successfully for {passenger_name}") #msg for reserve seat
            else:
                print("Seat already reserved..!")
        else:
            print("Invalid seat number..!")
    
    def cancel_reservation(self,seat_number):  #cancel the reservation ticket 
        if 1 <= seat_number <= self.total_seats:  #check if seat number is valid
            if self.seats[seat_number -1] is not None: #Check if  Seat is Reserved
                print(f"Reservation for seat {seat_number} canceled .")
                self.seats[seat_number -1]=None #Cancel  Reservation
            else:
                print("Seat was not Reserved.")
        else:
            print("Invalid seat number.")

    def issue_ticket(self,seat_number): # for print ticket that we book
        if 1 <= seat_number <= self.total_seats:
            passenger = self.seats[seat_number - 1]
            if passenger:
                print(f""" 
Ticket Issued:
---------------------------------------
Passenger Name : {passenger}
Bus ID         : {self.bus_id}
Route          : {self.start_city} -> {self.destination}
Bus Leaves At  : {self.time} on {self.travel_date}
Seat Number    : {seat_number}
Ticket Price   : Rs.{self.ticket_price} 
---------------------------------------
""")
            else:
                print("Seat not Reserved yet.")
        else:
            print("Invalid Seat Number")

    @staticmethod
    def search_by_route(start_city , destination):
        print(f"\n --- Buses from {start_city} to {destination} ---")
        found = False
        for bus in buses:
            if bus.start_city.lower() == start_city.lower() and bus.destination.lower() == destination.lower():
                bus.schedule()
                found = True
        if not found:
            print("No Bus Found for this Route..!")
# This static method searches all buses in the system by start city and destination, 
# prints schedules if found, otherwise shows a "No Bus Found" message.
    
    def passenger_list(self):
        print(f"\n Passenger List for Bus {self.bus_id} : ")
        has_passengers = False
        for i , passenger in enumerate(self.seats):
            if passenger:
                print(f"Seat { i + 1} : {passenger}")
                has_passengers = True
        if not has_passengers:
                print("No Passengers Have Reserved Seats On This Bus..!")

# Loops over all seats.
# Prints only reserved ones.
# If no reservations → shows "No passengers".

buses= [ 
    Bus('B101' , 'Pune' , 'Mumbai' , '10:00 AM' , 20 , 650.00 , '2025-09-15'),
    Bus('B202' , 'Pune' , 'Panvel' , '12.30 PM' , 25 , 450.00 , '2025-10-01'),
    Bus('B303' , 'Pune' , 'Nagpur' , '02:15 PM' , 15 , 750.00 , '2025-09-25'),
    Bus('B404' , 'Pune' , 'Nashik' , '05:30 PM' , 25 , 250.00 , '2025-10-05'),
    Bus('B505' , 'Pune' , 'Satara' , '06:45 PM' , 15 , 530.00 , '2025-09-30')
] #available bus for travelling

def find_bus(bus_id , travel_date): # for find Bus by bus id 
    for bus in buses:
        if bus.bus_id.lower()==bus_id.lower() and bus.travel_date == travel_date:
            return bus
    return None
    
def main(): #main function for print choice 
    while True:
        print("""
\n === Bus Ticket Reservation System ===
1. view All Bus Schedules 
2. View Available Seats
3. Reserve A seat
4. Cancel Reservation 
5. Issue Ticket 
6. Search Buses by Route
7. Show Passenger List 
8. Exit""")
        ch=int(input("Enter your Choice(1-8): "))

        if ch == 1:
            print("\n --- Bus Schedules ---")
            for bus in buses:
                bus.schedule()
        
        elif ch == 2:
            bus_id = (input("Enter Bus ID : "))
            travel_date = input("Enter Travel Date (YYYY-MM-DD) : ")
            bus = find_bus(bus_id , travel_date)
            if bus:
                seats = bus.available_seats()
                print(f"Available Seats in {bus.bus_id} on {travel_date} : {seats if seats else 'No Seats available.'}")
            
            else:
                print("Bus Not Found..!")
        
        elif ch == 3:
            bus_id=(input("Enter Bus ID : "))
            travel_date = input("Enter Travel Date (YYYY-MM-DD) : ")
            bus = find_bus(bus_id , travel_date)
            if bus:
                available = bus.available_seats()
                if not available:
                    print("No seats available on this bus.")
                    continue
                print(f"Available seats : {available}")

                name = input("Enter Passenger Name : ")
                try:
                    seat = int(input("Enter seat number to reserve: "))
                    bus.reserve_seats(seat , name)
                except ValueError:
                    print("Seat number must be a Number.")
            else:
                print("Bus Not Found..!")
        
        elif ch == 4:
            bus_id= input("Enter Bus ID : ")
            travel_date = input("Enter Travel Date (YYYY-MM-DD) : ")
            bus = find_bus(bus_id , travel_date)
            if bus:
                try:
                    seat = int(input("Enter Seat Number to Cancel : "))
                    bus.cancel_reservation(seat)
                except ValueError:
                    print("Seat Number Must Be a Number..!")
            else:
                print("Bus not Found..!")

        elif ch == 5:
            bus_id = (input("Enter Bus ID : "))
            travel_date = input("Enter Travel Date (YYYY-MM-DD) : ")
            bus = find_bus(bus_id , travel_date)
            if bus:
                try:
                    seat = int(input("Enter Seat Number to Issue Ticket : "))
                    bus.issue_ticket(seat)
                except ValueError:
                    print("Seat Number Must Be a Number..!")
            else:
                print("Bus Not Found..!")

        elif ch == 6:
            start_city = input("Enter Start City : ")
            destination = input("Enter Destination City : ")
            Bus.search_by_route(start_city , destination)

        elif ch == 7:
            bus_id = input("Enter Bus ID : ")
            travel_date = input("Enter Travel Date (YYYY-MM-DD) : ")
            bus = find_bus(bus_id , travel_date)
            if bus:
                bus.passenger_list()
            else:
                print("Bus Not Found..!")

        elif ch == 8:
            print("Exiting System . Thank You..!")
            print("Visit Again..!")
            break
    
        else:
            print("Invalid Choice. Please Enter a Number between 1-8.")

main() # main function calling