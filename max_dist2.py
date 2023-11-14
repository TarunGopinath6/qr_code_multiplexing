def find_equidistant_number(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 1:
        median = round(sorted_arr[n // 2], 0)
    else:
        median = round((sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2, 0)
    return int(median)


def calc(r, g, b, n):
    for i in range(n-7):
        r.append(find_equidistant_number(r))
        g.append(find_equidistant_number(g))
        b.append(find_equidistant_number(b))
    return r, g, b


def rgb_to_hex(r, g, b):
    # Use the format function to convert RGB to hex
    hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return hex_color


# Example usage:
r = [255, 255, 255, 0, 0, 75, 148]
g = [0, 165, 255, 255, 0, 0, 0]
b = [0, 0, 0, 255, 255, 130, 211]
# result1 = find_equidistant_number(r)
# result2 = find_equidistant_number(g)
# result3 = find_equidistant_number(b)
n = pow(2, 4)
new_r, new_g, new_b = calc(r, g, b, n)
print(r)
print(g)
print(b)
for i in range(n):
    print(rgb_to_hex(r[i], g[i], b[i]))
