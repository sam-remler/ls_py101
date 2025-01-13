def text_iteration(text : str, iterations : int):
    for i in range(iterations):
        dashes = "-"*(i+1)
        print(dashes+text)

text_iteration("The Flinstones", 10)

# -------

def factors(number):
    if number < 0:
        return None
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result