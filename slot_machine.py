import random

MAX_LINES = 3
MIN_LINES = 1
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3


symbol_count = {
  'A': 3,
  'B': 4,
  'C': 6,
  'D': 8
}

symbol_values = {
  'A': 10,
  'B': 8,
  'C': 6,
  'D': 4
}

def check_winnings(columns, lines, bet, values):
  winnings = 0
  winning_lines = []
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol != symbol_to_check:
        break
    else:
      winnings += values[symbol] * bet
      winning_lines.append(line + 1)    
  return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
  all_symbol = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbol.append(symbol)

  columns = []
  for _ in range(cols):
    column = []
    current_symbol = all_symbol[:]
    for _ in range(rows):
      value = random.choice(current_symbol)
      current_symbol.remove(value)
      column.append(value)

    columns.append(column)

  return columns 

def print_slot_machine(columns):
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i != len(column) - 1:
        print(column[row], end=' | ')
      else:
        print(column[row])

def deposit():
  while True:
    amount = input("How much money you want to deposit?")
    if amount.isdigit():
      amount = int(amount)
      break
    else:
      print("Please enter a number!") 
  return amount

def get_lines():
  while True:
    lines = input("How much lines you want to bet on? 1 - 3?")
    if lines.isdigit():
      lines = int(lines)
      if MIN_LINES <= lines <= MAX_LINES:
        break
      else:
        print("Please enter a valid line")
    else:
      print("Please enter a number!") 
  return lines

def get_bet():
  while True:
    bet = input("How much money you want to bet on each line?")
    if bet.isdigit():
      bet = int(bet)
      if MIN_BET <= bet <= MAX_BET:
        break
      else:
        print(f"Please bet between {MIN_BET} and {MAX_BET}")
    else:
      print("Please enter a number!") 
  return bet  

def spin(balance):
  lines = get_lines()
  while True:
    bet = get_bet()
    total_bet = bet * lines
    if total_bet <= balance:
      break
    else:
      print(f"Your total bet is {total_bet} but you only have {balance}")

  print(f"You bet {bet} on {lines} lines, your total bet is {total_bet}")  

  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)
  winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
  print(f"You have won {winnings}")
  print("You won on these line(s): ", *winning_lines)
  return winnings - total_bet

def main():
  balance = deposit()
  while True:
    print(f"Your current balance is ${balance}")
    answer = input("Press any key to start, 'q' or 'Q' to quit")
    if answer == 'q' or answer == 'Q':
      break
    balance += spin(balance)
  print(f"You left with ${balance}") 
  
main()
