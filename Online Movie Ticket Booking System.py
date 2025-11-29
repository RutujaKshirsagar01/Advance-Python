# -----------------------------
# Online Movie Ticket Booking System 
# -----------------------------

class Movie:
    def __init__(self,movie_id,name,showtimes_info):
        self.movie_id=movie_id
        self.name=name
        self.showtimes_info=showtimes_info #store data and exact time 
        #each showtime has its own seat layput 
        self.showtimes={label:self.create_seat_layout()for label in showtimes_info}

    def create_seat_layout(self):
        layout = {}
        rows = ['A','B','C','D']
        col = 5
        for r in rows :
            for c in range(1,col+1):

                seat_no = f"{r}{c}"
                if r == 'A' :
                    seat_type = 'VIP'
                    price = 300
                
                elif r == "B":
                    seat_type = 'Premium'
                    price = 250

                else:
                    seat_type = 'Regular'
                    price = 200

                layout[seat_no] = {'type': seat_type , "price" : price , 'customer' : None}
        return layout
    
    def show_seats(self , show_label):
        print(f"\n Seat Layout for {self.name} ({show_label})")
        rows = ['A','B','C','D']
        for r in rows:
            row_seats =[]
            for c in range(1,6):
                seat_no = f"{r}{c}"
                seat_info = self.showtimes[show_label][seat_no]
                if seat_info['customer'] is None:
                    row_seats.append(f"{seat_no}{seat_info['type'][0]}")
                else:
                    row_seats.append(f"{seat_no}(X)")
            print(" ".join(row_seats))

    def available_seats(self,show_label):
        return [seat for seat , info in self.showtimes[show_label].items() if info["customer" is None]]
    
    def book_ticket(self,show_label,seat_no,customer_name):
        if seat_no in self.showtimes[show_label]:
            seat_info =self.showtimes[show_label][seat_no]
            if seat_info['customer'] is None:
                seat_info['customer'] = customer_name
                print(f"Seat {seat_no} ({seat_info['type']}) Booked for {customer_name} at RS.{seat_info['price']}")

            else:
                print("Seat Already Booked..!")

        else:
            print("Invalid Seat Number..!")

    def cancel_ticket(self,show_label,seat_no):
        if seat_no in self.showtimes[show_label]:
            seat_info = self.showtimes[show_label][seat_no]
            if seat_info['customer'] is not None:
                print(f"Bokking cancelled for seat {seat_no}")
                seat_info['customer'] = None
            else:
                print("Seat was not Booked..!")
        else:
            print("Invalid Seat Number..!")

    def issue_ticket(self,show_label , seat_no):
        if seat_no in self.showtimes[show_label]:
            seat_info = self.showtimes[show_label][seat_no]
            if seat_info['customer']:
                show_date , exact_time = self.showtimes_info[show_label]
                print(f""" 
-----------------------------
        Movie Ticket 
-----------------------------
Customer Name : {seat_info['customer']} 
Movie         : {self.name}
Show Date     : {show_date}
Show Time     : {show_label} | {exact_time} 
Seat Number   : {seat_no}
Seat Type     : {seat_info['type']}
Ticket Price  : Rs.{seat_info['price']}
-----------------------------
""")
            else:
                print("Seat No Not Booked yet..!")
        else:
            print("Invalid Seat Number..!")

Movies = [ 
    Movie('M101','Animal(Hindi)',
          {'Morning':('2025-09-15','10:00 AM'),
           'Afternoon':('2025-09-15','01:00 PM'),
           'Evening':('2025-09-15','04:30 PM'),
            'Night' : ('2025-09-15','08:00 PM')}),

    Movie('M202','Baaghi 4 (Hindi)',
          {'Morning':('2025-09-16','09:30 AM'),
           'Afternoon':('2025-09-16','12:15 PM'),
           'Evening':('2025-09-16','05:00 PM'),
            'Night' : ('2025-09-16','09:00 PM')}),

    Movie('M303','The Bengal Files (Hindi)',
          {'Morning':('2025-09-19','10:30 AM'),
           'Afternoon':('2025-09-19','12:30 PM'),
           'Evening':('2025-09-19','05:30 PM'),
            'Night' : ('2025-09-19','09:15 PM')}),

    Movie('M404','Dashavatar (Marathi)',
          {'Morning':('2025-09-17','10:00 AM'),
           'Afternoon':('2025-09-17','12:30 PM'),
           'Evening':('2025-09-17','05:00 PM'),
            'Night' : ('2025-09-17','09:30 PM')}),

    Movie('M505','Azaad (Hindi)',
          {'Morning':('2025-09-25','10:00 AM'),
           'Afternoon':('2025-09-25','01:00 PM'),
           'Evening':('2025-09-25','04:30 PM'),
            'Night' : ('2025-09-25','09:30 PM')})
]

def find_movie(movie_id):
    for Movie in Movies:
        if Movie.movie_id.lower() == movie_id.lower():
            return Movie
    return None 

def search_movie(name):
    found = False
    print(f"\n ---- Search Results For '{name}' ----")
    for Movie in Movies:
        if name.lower() in Movie.name.lower():
            showtimes = ', '. join(Movie.showtimes_info.keys())
            print(f"{Movie.movie_id} | {Movie.name} | Show Times : {showtimes}")
            found = True
        if not found:
            print("No Movie Found with that Name..!")


#main function 
def main():
    while True:
        print(""" 
=== Online Movie Ticket Booking === 
    1. View All Movies
    2. View Available Seats 
    3. Book Ticket 
    4. Cancel Ticket 
    5. Issue Ticket 
    6. Search Movie by Name
    7. Exit 
""")
        try:
            ch = int(input("Enter Your Choice (1-7) : "))
        except ValueError:
            print("Invalid Input. Enter a Number..!")
            continue

        if ch == 1:
            print("\n ---- Movies & Show Times ---- ")
            for m in Movies:
                showtimes = ','.join(m.showtimes_info.keys())
                print(f"{m.movie_id}")