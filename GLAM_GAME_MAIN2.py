import random

#global varible 
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 20

ROWS = 3
COLS = 3

symbol_count = {
    'A' : 2,    
    'B' : 4,
    'C' : 6,
    'D' : 8
    }

symbol_value = {
    'A' : 5,    
    'B' : 4,
    'C' : 3,
    'D' : 2
    }


def get_slot_machine_spin(rows,cols,symbols):
    all_symbol = []
    for symbol , symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)
    
    colums =[]
    for _ in range(cols):
        column = []
        current_symbol =all_symbol.copy()
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove( value)
            column.append(value)

        columns.append(column)  

    return columns


def print_slot_machine(columns):
    for row in range (len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1 :
                print(column[row], end = '|')
            else:
                print(column[row] , end='')
        print()

def check_winnings(column , lines , bet , values):
    winnigs=0
    winnig_lines =[] 
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnigs += values[symbol] * bet
            winnig_lines.append(line + 1)
    return winnigs,winnig_lines





def depoist():
    #collecting the input
    while True:
        amount = input("Enter the amount you need to depoist? $")
        if amount.isdigit():
            amount = int(amount)
            if (amount >= 0):
                break
            else:
                print("Amount need to be greater than zero.")
        else:
            print("Amount need to be in the digit not either String or Symbol")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the no.of lines to bet on ( 1-"+ str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if (0 <= lines <= MAX_LINES):
                break
            else:
                print("enter the line number in the range of 1 to 3.")
        else:
            print("Line number need to be in the digit not either String or Symbol")
    return lines

def get_bet():
    while True:
        bet = input("Enter the Amount you need to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if (MIN_BET <= bet <= MAX_BET):
                break
            else:
                print(f"amount must be between ${MIN_BET } - ${MAX_BET}")
        else:
            print("Bet number need to be in the digit not either String or Symbol")
    return bet

def main():
    balance = depoist()
    while True:
        print(f"current balance is ${balance}")
        spin = input("Press enter to spin (q to quit)")
        if spin == 'q':
            break
        balance += rep_run()
    print (f"You left with ${balance}")



def rep_run( balance):
    line = get_number_of_lines()
    while True:
        bet = get_bet()
        tot_bet = bet * line
        if tot_bet > balance :
            print(" YOU donot have enough balance")
        else:
            break
    print(f"you are betting the amount of ${bet} rupees from a total amount of ${amount} rupees in a line of {line}.")
    print(f"total betting amount is {tot_bet}")
    slots = get_slot_machine_spin(ROWS , COLS , symbol_count)
    print_slot_machine(slots)
    winnigs = check_winnings( slots , lines, bet, symbol_value)
    print(f"You won ${winnigs} and you won on lines" *winnig_lines)
    

    return winnigs - tot_bet
