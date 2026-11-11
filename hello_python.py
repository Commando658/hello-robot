import time

class MechatronicsBot:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination

    def boot_system(self):
        print(f"⚡ [SYSTEM START] {self.name} is initializing firmware...")
        time.sleep(1) # Pause for 1 second
        print(f"📡 [CONNECTING] Terminal configured natively on Ubuntu Linux.")
        time.sleep(1)
        print(f"🚀 [MISSION] Global portfolio active. Target destination: {self.destination}!")

# --- EXECUTE THE ROBOT CODE ---
if __name__ == "__main__":
    # Building your robot object
    my_bot = MechatronicsBot(name="PhantomX_Rover", destination="Canada 🇨🇦")
    
    # Running the machine function
    my_bot.boot_system()
