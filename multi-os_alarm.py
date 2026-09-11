import time
import platform
import subprocess

seconds = int(input("Enter the time in seconds: "))
print("Alarm Set...")

time.sleep(seconds)

print("Time's up!")

os_name = platform.system()
#print(os_name)

if os_name == "Windows":
    import winsound
    winsound.Beep(1000, 1000)

elif os_name == "Darwin":
    subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])

elif os_name == "Linux":
    subprocess.run("paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga")

else:
    print("Unknown OS")
