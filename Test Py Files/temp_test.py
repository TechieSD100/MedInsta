import time

# The animation speed
animation_speed = 0.05

# The animation sequence
animation = "."
j = 0

for j in range(100):
    for i in range(3):
        # Add a dot
        animation += "."
        print(f"\rLoading{animation}", end="")
        time.sleep(animation_speed)
    # Reset the animation
    animation = "."
