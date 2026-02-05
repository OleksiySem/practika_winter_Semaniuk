def custom_to_string(number):
    if isinstance(number, int):
        return int_to_string(number)

    if number < 0:
        return "-" + custom_to_string(-number)

    if number == 0:
        return "0.0"

    integer_part = int(number)
    fractional_part = number - integer_part

    result = int_to_string(integer_part) + "."

    precision = 6
    count = 0

    if fractional_part == 0:
        return result + "0"

    while fractional_part > 0 and count < precision:
        fractional_part *= 10
        digit = int(fractional_part)
        result += int_to_string(digit)
        fractional_part -= digit
        count += 1

    return result

def int_to_string(number):
    if number == 0: return "0"
    digits_map = "0123456789"
    res = ""
    while number > 0:
        res = digits_map[number % 10] + res
        number //= 10
    return res

f_num = 12.345
f_num_neg = -0.0056

print(f"Вхід: {f_num} -> Вихід: '{custom_to_string(f_num)}'")
print(f"Вхід: {f_num_neg} -> Вихід: '{custom_to_string(f_num_neg)}'")