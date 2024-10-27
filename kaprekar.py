def kaprekar_step(num):
    num_str = f"{num:04d}"  
    
    ascending = int("".join(sorted(num_str)))
    descending = int("".join(sorted(num_str, reverse=True)))
    
    return descending - ascending

def sub_by_kaprekar(num):
    steps = 0
    while num != 6174:
        num = kaprekar_step(num)
        steps += 1
        print(f"Step {steps}: Resulting number = {num}")
        if num == 0:
            print("Reached zero, further subtraction won't help.")
            return

    print(f"Reached Kaprekar's constant 6174 in {steps} steps.")

def main(num):
    if len(str(num)) != 4 or len(set(str(num))) == 1:
        print(f"{num} is not a valid four-digit number with at least two different digits.")
        return

    sub_by_kaprekar(num)

def count_till_infinity():
    for i in range(1000, 10000):  
        main(i)


if __name__ == "__main__":
    print("Started")
    count_till_infinity()

