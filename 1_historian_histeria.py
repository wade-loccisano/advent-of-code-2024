from data import historian_histeria as data

lines = data.strip().split("\n")  # Split the input into lines
column_a, column_b = [], []  # Initialize empty lists for columns

for line in lines:
    if line.strip():  # Ignore empty lines
        a, b = map(int, line.split())  # Split the line and convert to integers
        column_a.append(a)
        column_b.append(b)

sorted_a = sorted(column_a)
sorted_b = sorted(column_b)


# print("Column A:", sorted_a)
# print("Column B:", sorted_b)


pairs = [[a, b] for a, b in zip(sorted_a, sorted_b)]
result = 0

for a, b in pairs:
    if a > b:
        # print(f"a: {a} is > then b: {b}")
        result += a - b
    else:
        result += b - a

print(f"result is: {result}")

b_map = {}
for _, b in pairs:
    b_map[b] = 1 + b_map.get(b, 0)
result = 0
for a, _ in pairs:
    if a in b_map:
        result += a * b_map[a]

print(f"result of part 2 is: {result}")
