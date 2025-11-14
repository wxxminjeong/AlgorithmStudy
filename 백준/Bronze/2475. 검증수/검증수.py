def verify_code(code):
    code_sum = 0

    for i in range(5):
        code_sum += code[i] * code[i]
    
    return code_sum % 10

code = list(map(int, input().split()))

print(verify_code(code))
