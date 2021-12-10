dividendo, divisor = input().split()
dividendo, divisor = int(dividendo), int(divisor)

quociente = dividendo // divisor
resto = dividendo % divisor

print('dividendo -', dividendo)
print('divisor -', divisor)
print('quociente -', quociente)
print('resto -', resto)
