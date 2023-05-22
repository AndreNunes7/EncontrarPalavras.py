def mult(*args):
    total = 1 
    for num in args:
        total *= num
    return total
    
        


valor_mult = mult(1, 3, 4)
print(valor_mult)

