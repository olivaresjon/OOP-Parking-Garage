class parkingG():
    def __init__(self):
        self.tickets = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parkingSpaces = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.currentTicket = {}

    def takeTicket(self):
        if len(self.parkingSpaces) == 0:
            print("sorry there are no more parking available")
        else:
            self.tickets.remove(self.tickets[-1])
            self.parkingSpaces.remove(self.parkingSpaces[-1])

    def payForParking(self):
        while True:
            display_message = input(
                "There are " + str(self.parkingSpaces[-1]) + " parking spaces available.\nType 'PAY' to pay now: ")
            if display_message.upper() == "PAY":
                self.currentTicket['paid'] = True
                print('Your ticket is now paid. Starting 10 minute timer now.')
                break

    def leaveGarge(self):

        if self.currentTicket['paid'] == True:
            print('Thank you for using the parking garage, drive safe!')

        self.tickets.append(self.tickets[-1]+1)
        self.parkingSpaces.append(self.parkingSpaces[-1]+1)


def final():
    complete = parkingG()
    print('Welcome, thanks for choosing us to park to beloved beloved vehicle!')
    message = input("Enter 'T' to take a ticket: ")

    if message.upper() == 'T':
        complete.takeTicket()
        complete.payForParking()

        while True:
            final = input("type 'QUIT' to exit the garage: ")
            if final.upper() == "QUIT":
                complete.leaveGarge()
                break
    else:
        print("invalid input, try again.")


final()
