#A ticket printing machine prints tickets on sheets of paper. Each sheet can print a fixed number of tickets (for example, 50 tickets per 
# sheet). Even if only one extra ticket is needed, the printer must use an entire extra sheet. Your task is to write a Python program that 
# calculates how many sheets of paper are needed to print a given number of tickets.
def ticket_master(ticket_no):  # function to check no of sheets to print 
    block_size = 50
    full_size = ticket_no // block_size # no of full size sheets
    partial_size = ticket_no % block_size # no of partial size sheet 
    if partial_size > 0:
        return full_size + 1
    else:
        return full_size
ticket_no = int(input("Enter the number of tickets: "))
print("The number of sheets required to print the tickets is: ")
print(ticket_master(ticket_no)) 