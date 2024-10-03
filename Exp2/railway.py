import csv

trains=[]
passengers=[]

with open('trains.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        trains.append(row)


with open('passengers.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        passengers.append(row)

trains=trains[1:]
passengers=passengers[1:]

seat_capacity={}
bookings={}
fares={}

for train_list in trains:
    seat = train_list[0]
    number_of_seats = int(train_list[4])
    fares[seat]=50 
    if seat in seat_capacity:
        seat_capacity[seat] += number_of_seats
    else:
        seat_capacity[seat] = number_of_seats
        
        
for passenger in passengers:
    train_id = passenger[1]
    tickets = int(passenger[2])
    passenger_name=passenger[0]
    
    if not passenger_name.strip():
            print(f"Error: Passenger name cannot be empty.")
            continue
        
    if train_id in bookings:
        bookings[train_id] += tickets
    else:
        bookings[train_id] = tickets
        
        
for train_id, booked_tickets in bookings.items():
        if train_id not in seat_capacity:
            print(f"Error: Train ID {train_id} does not exist.")
            continue

        available_seats = seat_capacity[train_id] - booked_tickets
        if available_seats < 0:
            print(f"Error: Not enough seats available for Train ID {train_id}.")
        else:
            seat_capacity[train_id] -= booked_tickets
            print(f"Booking confirmed for Train ID {train_id}.")

print()
print("Report 1: Train Details")
for train in trains:
    train_id = train[0]
    train_name = train[1]
    source_station = train[2]
    destination_station = train[3]
    total_seats = seat_capacity.get(train_id, 0)
    print(f"Train ID: {train_id}")
    print(f"Train Name: {train_name}")
    print(f"Source Station: {source_station}")
    print(f"Destination Station: {destination_station}")
    print(f"Total Seats Available: {total_seats}")
    print()
    
print("Report 2: Revenue Report")
for train_id in bookings:
    revenue = bookings[train_id] * fares.get(train_id, 0)
    print(f"Train ID: {train_id}")
    print(f"Total Revenue Earned: ${revenue:.2f}")
    print()