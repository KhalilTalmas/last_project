import os

# Initialize the list of buses
buses = [{'name': 'Bus 1', 'destination_from': 'Gaza', 'destination_to': 'Jerusalem', 'capacity': 20, 'seats_taken': 0, 'booking':[]},
         {'name': 'Bus 2', 'destination_from': 'Jerusalem', 'destination_to': 'Ramallah', 'capacity': 30, 'seats_taken': 0, 'booking':[]},
         {'name': 'Bus 3', 'destination_from': 'Ramallah', 'destination_to': 'Hebron', 'capacity': 40, 'seats_taken': 0, 'booking':[]}]

# Function to display the available buses and destinations
def show_buses():
  print('\nAvailable buses:')
  for i, bus in enumerate(buses):
    print(f'{i+1}. {bus["name"]} from {bus["destination_from"]} to {bus["destination_to"]} , Seats available: {bus["capacity"] - bus["seats_taken"]}')


# Function to check the seat availability
def check_availability():
  show_buses()
  bus_number = int(input('\nEnter the bus number: '))

  bus = buses[bus_number-1]
  seats_available = bus['capacity'] - bus['seats_taken']
  print(f'\nSeats available on {bus["name"]}: {seats_available}')

# Function to book a seat
def book_seat():
  show_buses()
  bus_number = int(input('\nEnter the bus number: '))
  seat_number = int(input('\nEnter the seat number: '))
  bus = buses[bus_number-1]
  booking = bus['booking']
  if bus['seats_taken'] < bus['capacity'] and (seat_number not in bus['booking']):
    bus['seats_taken'] += 1
    bus['booking'].append(seat_number)

    print(f'\nSeat booked on {bus["name"]} from {bus["destination_from"]} to {bus["destination_to"]}')
  elif seat_number in bus['booking']:
    print('\nSorry, this seat is not available, choose another one.')
  else:
    print('\nSorry, this bus is full.')



# Function to book a seat
def specific_place():
  show_buses()
  bus_number = int(input('\nEnter the bus number: '))
  seat_number = int(input('\nEnter the seat number: '))
  bus = buses[bus_number-1]
  x = int(bus['capacity']/3)
  if seat_number < x:
      print('\nThe Seat in front.')
  elif seat_number < x*2:
      print('\nThe Seat in middle.')
  else:
      print('\nThe Seat in back.')


# Main function
def main():
  while True:
    print('\nWelcome to the Gaza Bus booking app!')
    print('\nPlease select an option:')
    print('1. View available buses , destinations and availability of seats')
    print('2. Availability of Seats')
    print('3. Book a seat')
    print('4. know the specific place of the seat')
    print('5. Exit')
    choice = int(input('\nEnter your choice: '))
    if choice == 1:
      show_buses()
    elif choice == 2:
      check_availability()
    elif choice == 3:
      book_seat()
    elif choice == 4:
      specific_place()
    elif choice == 5:
      break
    else:
      print('\nInvalid choice. Please try again.')

# Run the main function
main()