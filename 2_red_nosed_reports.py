from data import red_nosed_reports as data

result = {}
safe_reports = []
# split row on line
lines = data.split("\n")
# row to array
for line in lines:
    if line.strip():
        values = list(map(int, line.split(" ")))
        if values[0] < values[1]:
            i = 0
            while i < len(values) - 1:
                if (
                    values[i] > values[i + 1]
                    or values[i + 1] - values[i] > 3
                    or values[i] == values[i + 1]
                ):
                    result["unsafe"] = 1 + result.get("unsafe", 0)
                    break
                i += 1
                if i == len(values) - 1:
                    result["safe"] = 1 + result.get("safe", 0)
                    safe_reports.append(values)
        elif values[0] > values[1]:
            i = 0
            while i < len(values) - 1:
                if (
                    values[i] < values[i + 1]
                    or values[i] - values[i + 1] > 3
                    or values[i] == values[i + 1]
                ):
                    result["unsafe"] = 1 + result.get("unsafe", 0)
                    break
                i += 1
                if i == len(values) - 1:
                    result["safe"] = 1 + result.get("safe", 0)
                    safe_reports.append(values)
        else:
            result["unsafe"] = 1 + result.get("unsafe", 0)

print(f"result is: {result}")

# part 2
