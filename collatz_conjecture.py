import matplotlib.pyplot as plt

# variables for ax+b, x/c
multiplier = 3
adder = 1
divisor = 2


# returns a list of a number's prime factors
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


# returns True if a nunmber is a power of the divisor
def power_of_divisor_tester(power_of_divisor_tester_input):
    if power_of_divisor_tester_input % divisor == 0:
        return power_of_divisor_tester(int(power_of_divisor_tester_input // divisor))
    elif power_of_divisor_tester_input == 1:
        return True
    else:
        return False


# classic collatz sequence
def unordered_collatz(collatz_input):
    collatz_output_list = [collatz_input]

    while collatz_input != 1:
        if collatz_input % 2 == 0:
            collatz_input = collatz_input // divisor
        else:
            collatz_input = multiplier * collatz_input + adder
        collatz_output_list.append(collatz_input)
    return collatz_output_list


# ordered collatz sequence
def ordered_collatz(collatz_input):
    collatz_output_list = [collatz_input]

    while collatz_input != 1:
        if power_of_divisor_tester(collatz_input):
            break
        else:
            collatz_input = multiplier * collatz_input + adder
        collatz_output_list.append(collatz_input)

    while collatz_input != 1:
        collatz_input = collatz_input // divisor
        collatz_output_list.append(collatz_input)

    return collatz_output_list


# choose between ordered and unordered Collatz Sequences
user_input = int(input("Enter 0 for an Unordered (Classic) Collatz Sequence or 1 for an Ordered Collatz Sequence: "))
if user_input == 0:
    collatz = unordered_collatz
    orderedFlag = "unordered"
else:
    collatz = ordered_collatz
    orderedFlag = "ordered"

# choose a starting number
user_input = int(input("Enter a starting number: "))
small_list = collatz(user_input)

big_list = []
max_len = 0

for i in small_list:
    i_index = small_list.index(i)
    current_step = "       "
    if i_index > 0:
        if small_list[i_index] > small_list[i_index - 1]:
            current_step = "* " + str(multiplier) + " + " + str(adder)
        else:
            current_step = "/ " + str(divisor) + "    "
    if len(str(i)) > max_len:
        max_len = len(str(i))

    big_list.append([i, prime_factors(i), current_step])

# print output nicely (there's definitely a better way to do this)
print("Odds:", "n*" + str(multiplier) + "+" + str(adder), " Evens:", "n/" + str(divisor))
for i in big_list:
    print("Step " + str(big_list.index(i)) + ":" + str(" " * (len(str(len(big_list))) - len(str(big_list.index(i))))),
          str(" " * (max_len - len(str(big_list[(big_list.index(i) - 1)][0])))) +
          str(big_list[(big_list.index(i) - 1)][0]), i[2], "=",
          str(i[0]) + str(" " * (max_len - len(str(i[0])))), "\t Prime Factors:", len(i[1]), i[1])
print("Loop", collatz(multiplier + adder))

# display and save chart
x = []
y = []
for count, data in enumerate(small_list):
    x.append(count)
    y.append(data)
plt.plot(x, y)
plt.xlabel("Iterations")
plt.ylabel("n")
file_name = "%i %inx%i %i " % (user_input, multiplier, adder, divisor) + str(orderedFlag) + ".jpg"
plt.savefig(file_name)
plt.show()
