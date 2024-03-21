import math

x, y =map(int, input().split())

gcd_result = math.gcd(x , y)
lcm_result = math.lcm(x , y)

print(gcd_result)
print(lcm_result)