# multiply.py
import sys

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
result = num1 * num2

print("Result is:", result)

# Save result to file
with open("result.txt", "w") as f:
    f.write(str(result))
