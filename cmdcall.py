# cmdcall.py

from commands import commandlist 

def main():
    print("--- Welcome to Reinne's Testing Place!! ---")
    while True:
        pRequest = input("Enter command: ").lower()
        if pRequest in commandlist:
            commandlist[pRequest]()
        elif pRequest == "exit":
            print("Goodbye")
            break
        else:
            print(f"'{pRequest}' is an invalid command")

if __name__ == "__main__":
    main()
