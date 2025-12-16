value = 1
result = 1
while result <= 1000: 
    result *= value
    print(f"value = {value} result ={result}")
    if result > 1000:
        break
    value += 1   

print(f"value : {value}, 곱한 값: {result}")


    