import time
import pygame
import tkinter

# Initialize Pygame
pygame.init()

# Set up the timer
timer = pygame.time.Clock()

# Set reminder interval to 30 minutes
inttime = int(input("The reminder repeats every(in minutes):"))
reminder_interval = inttime * 60  # Convert to seconds
if inttime < 1:
    print("Error, Wrong time! example: 30")
    quit()
elif inttime == 1:
    print("Ok, Will remind you in",inttime,"minute.")
else:
    print("Ok, Will remind you in",inttime,"minutes.")

# Set up the sound
stand_up_sound = pygame.mixer.Sound("stand_up_sound.mp3")

# Set up the popup
def show_popup():
    # Create the main window
    root = tkinter.Tk()

    # Create the pop-up window
    popup = tkinter.Toplevel(root)
    popup.wm_transient(root)  # Set the pop-up as transient
    popup.wm_geometry("+500+300")  # Position the pop-up window
    popup.wm_attributes("-topmost", True)  # Keep the pop-up on top

    # Add a label to the pop-up window
    label = tkinter.Label(popup, text="It's Been 30 Minutes. Stand up already!\n\nDon't you think It's essensial to stand up for a bit?")
    label.pack()

    # Create a button to close the pop-up window
    close_button = tkinter.Button(popup, text="Close", command=popup.destroy)
    close_button.pack()
    # Start the main event loop
    root.mainloop()

while True:
    # Set the current time as the start time
    start_time = time.time()

    # Wait for the reminder interval to elapse
    while time.time() - start_time < reminder_interval:
        # Check for events (e.g., quit button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Wait for a short period to avoid CPU overload
        time.sleep(0.1)

    # Play the reminder sound
    stand_up_sound.play()
    now = time.time()
    readable_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
    print("\nReminder ran on ",readable_time)
    # Play the reminder popup
    show_popup()

    # Wait for the sound to finish playing
    while pygame.mixer.music.get_busy():
        # Check for events (e.g., quit button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Wait for a short period to avoid CPU overload
        time.sleep(0.1)
