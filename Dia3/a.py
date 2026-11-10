
import re

def calculate_sum_with_conditions(input_text):
    # Regex pattern for valid mul(X,Y) instructions
    mul_pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
    # Regex pattern for do() and don't() instructions
    control_pattern = r"(do\(\)|don't\(\))"
    
    # Split input into tokens based on control and mul patterns
    tokens = re.split(control_pattern, input_text)
    
    enabled = True  # Initial state: mul instructions are enabled
    total = 0
    
    for token in tokens:
        token = token.strip()
        if token == "do()":
            enabled = True
        elif token == "don't()":
            enabled = False
        elif "mul" in token and enabled:
            # Find all valid mul instructions in the token
            matches = re.findall(mul_pattern, token)
            for x, y in matches:
                total += int(x) * int(y)
    
    return total

# Read entire input
input_text = open("pingo.txt").read()
result = calculate_sum_with_conditions(input_text)
print(result)
