def convert_base(number, from_base, to_base):
    # Convert the number from the given base to base 10
    base10_number = int(number, from_base)

    # Convert the base 10 number to the desired base
    if to_base == 10:
        return str(base10_number)

    digits = "0123456789ABCDEF"
    result = ""

    while base10_number > 0:
        remainder = base10_number % to_base
        result = digits[remainder] + result
        base10_number //= to_base

    return result or "0"


while True:
    # Accept input from the user
    number = input("Enter the number to convert (or type 'end' to stop): ")
    if number.lower() == "end":
        break
    from_base = int(input("Enter the base of the input number: "))
    to_base = int(input("Enter the base to convert to: "))

    # Convert the number and print the result
    converted_number = convert_base(number, from_base, to_base)
    print(
        f"The number {number} in base {from_base} is {converted_number} in base {to_base}"
    )

# Explanation:
# 1. The convert_base function takes three arguments: the number to convert, the base of the input number, and the base to convert to.
# 2. The number is first converted to a base 10 integer using int(number, from_base).
# 3. If the target base is 10, the function returns the base 10 number as a string.
# 4. For other bases, the function converts the base 10 number to the desired base by repeatedly dividing the number by the target base and collecting the remainders.
# 5. The remainders are used to build the result string, which represents the number in the target base.
# 6. The code now runs in a loop, accepting input from the user until the user types "end".
