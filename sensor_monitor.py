import time
import random

# Simulating our physical temperature hardware sensor
def read_temperature_sensor():
    # Widening the range up to 55°C to test our emergency system
    return random.randint(25, 55)

print("🚀 Starting Smart Automation Monitoring Loop...")
time.sleep(1)

# The continuous monitoring loop
while True:
    current_temp = read_temperature_sensor()
    
    # 1. CRITICAL THRESHOLD: Check this first before anything else!
    if current_temp >= 50:
        print(f"🚨 CRITICAL ALARM! Temp is {current_temp}°C.")
        print("🛑 [EMERGENCY SYSTEM]: Triggering Main Breaker... Shutting down all power!")
        break  # <--- This instantly kills the loop and stops the program!
        
    # 2. HIGH THRESHOLD: Try to fix it with the cooling fans
    elif current_temp > 40:
        print(f"⚠️ DANGER! Temp is {current_temp}°C. [ACTUATOR ACTION]: Running cooling fans at 100%!")
        
    # 3. WARNING THRESHOLD: Alert the control room
    elif current_temp > 35:
        print(f"⚡ WARNING! Temp is {current_temp}°C. [SYSTEM LOG]: Monitoring closely...")
        
    # 4. SAFE THRESHOLD
    else:
        print(f"✅ NORMAL. Temp is {current_temp}°C. Machine running smoothly.")
        
    # Pause for 1 second before the next check
    time.sleep(1)

# This text only prints out if the loop is successfully broken by the emergency shutdown
print("\n🔒 System securely isolated. Please inspect hardware mechanics before manual reboot.")

