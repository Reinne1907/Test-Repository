# commands.py

profileExists = False
uName = None
coins = 0.00
# default amt of coins

def handleRNG():
    import random
    print(f"Your number is {random.randint(1, 10)}.")

def handleHelp():
    print("...")
    print("help - shows list of commands | rng - generates random number" \
          " | check - view your profile | search - gain coins | countdown (seconds) - make a countdown that earns you" \
          "coins")

def checkCoinBalance():
    global profileExists, uName, coins

    if not profileExists:
     print("You currently do not have an existing profile to continue this action.")
     while not profileExists:
         response1 = input("Do you want to create a new account? (Yes/No): ")
         if response1 == "Yes":
             uName = input("Enter a username here (12 characters or less): ")
             if len(uName) > 12:
                 uName = input("Your name exceeds 12 characters. Enter a username here: ")
             else:
                 print(f"Hello {uName}! You may now check profile commands.")
                 profileExists = True
         elif response1 == "No":
             print("Cancelled profile creation")
         else:
             print(f"{response1} is invalid.")
    else:
     print("--- PROFILE ---")
     print(f"Username: {uName}")
     print(f"Coin(s): {coins}")

def randomizedCoinGain():
    import random
    global coins
    rCoin = int(random.randint(1, 15))
    sentences = [
        "What a surprise! You gained coins.",
        "Coins is what you get.",
        "Wowzers! Coins are so cool!"
     ]
    print(random.choice(sentences))
    print(f"+ {rCoin} coins")
    coins = coins + rCoin

def doCountdown():
   import random
   import time
   global coins
   countDown = int(input("How long do you want the countdown to run for? (seconds): "))
   currentTime = 0
   while currentTime < countDown:
      if random.randint(1, 5) == 1:
          coins = coins + 1
          print("+ 1 coin")

      currentTime = currentTime + 1
      if currentTime == 1:
         print("Running...")
      time.sleep(1)
   if currentTime == countDown:
      print("Countdown finished")

# list of commands
commandlist = {
    "rng": handleRNG,
    "help": handleHelp,
    "check": checkCoinBalance,
    "search": randomizedCoinGain,
    "countdown": doCountdown
    # add more commands here
}
