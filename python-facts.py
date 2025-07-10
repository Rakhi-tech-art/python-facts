# 🐍 1. You can swap two variables without a third variable!
a, b = 5, 10
a, b = b, a
print(a, b)  # Output: 10 5
#💬 No temp variable needed! Python's tuple unpacking is magic ✨

# ⏱️ 2. You can create a delay using just one line
import time
time.sleep(3)  # pauses the program for 3 seconds
# 💬 Super useful for making timers, loading screens, or fake delays 😄

#🔁 3. Python has an else block with for and while loops
for i in range(5):
    if i == 6:
        break
else:
    print("Loop completed without break!")
# 💬 Yes! else runs only if the loop didn't break. Wild, right? 🧠

#🧪 4. You can run Python as a calculator directly in the terminal
>>> 2 ** 8
256
>>> round(3.14159, 2)
3.14
#💬 Python is literally a better calculator than Windows Calculator 😄

#🔥 5. You can write this in Python:
print("🔥" * 10)
#💬 Output? A line of 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
#Because strings can be multiplied!


