import json
from translate import Translator

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False


def calculator():
    prompt(prompts['welcome'])

    prompt(prompts['first_number'])
    number1 = input()

    while invalid_number(number1):
        prompt(prompts['invalid_number'])
        number1 = input()

    prompt(prompts['second_number'])
    number2 = input()

    while invalid_number(number2):
        prompt(prompts['invalid_number'])
        number2 = input()

    prompt(prompts['operation_list'])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(prompts['option_list'])
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    prompt(f"{prompts['result']} {output}")

if __name__ == '__main__':
    # Open the JSON file for reading
    with open('calculator_messages.json', 'r') as file:
        prompts = json.load(file)

    # Get the users language of choice
    prompt(prompts['language'])
    lang = input()
    if lang:
        translator= Translator(to_lang=lang)
    else:
        translator= Translator(to_lang="en")

    for key, value in prompts.items():
        prompts[key] = translator.translate(value)

    another = True
    while another == True:
        calculator()
        prompt(prompts['another_calc'])
        another = (input() == 'True')