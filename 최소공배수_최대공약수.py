#최대공약수
import math

math.gcd(21, 14) #7

# 최소공배수 -> 두 수를 곱한것에 최대공약수를 나눈 값과 같다.
def lcm(x, y):
  return x*y//(math.gcd(x, y))