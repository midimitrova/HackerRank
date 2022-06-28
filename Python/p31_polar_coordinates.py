import cmath

number = complex(input())
result = cmath.polar(number)
print(f"{result[0]:.3f}\n{result[1]:.3f}")
