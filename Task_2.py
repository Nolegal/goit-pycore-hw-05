import re
from typing import Callable
def generator_numbers(text: str):

  pattern = r"\d+\.\d+"
  sum=re.findall(pattern, text)
  for number in sum:
   yield number



 
def sum_profit(text: str, func: Callable):
  sum=0
  for s in func(text):
   slot=float(s)
   sum+=slot
  return sum
  

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")