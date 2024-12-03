from mull import data as data
import re

pattern = r"mul\(\d{1,3},\d{1,3}\)"

matches = re.findall(pattern, data)

result = 0
for m in matches:
    pattern2 = r"mul\((\d+),(\d+)\)"
    a, b = map(int, re.match(pattern2, m).groups())
    result += a * b

print(result)
