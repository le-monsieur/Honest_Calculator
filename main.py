# write your code here
'''
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
'''

msg_ = ["Enter an equation", 
        "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "Yeah... division by zero. Smart move...",
        "Do you want to store the result? (y / n):",
        "Do you want to continue calculations? (y / n):",
        " ... lazy",
        " ... very lazy",
        " ... very, very lazy",
        "You are",
        "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"
        ]
#print(msg_[msg_index])

memory = 0.0
result = 0.0

def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2) == True:
        msg = msg + msg_[6]
        
    if v1 == 1 or v2 == 1 and v3 == '*':
        msg = msg + msg_[7]
        
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_[8]
        
    if msg != '':
        msg = msg_[9] + msg
        
    print(msg)
    
def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer() == True:
        output = True
    else:
        output = False
    return output


while True:
    print(msg_[0])
    calc = input()
    x, oper, y = calc.split()
    
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory

#    try:
#        x = int(x)
#    except ValueError:
    try:
        x = float(x)
    except ValueError:
        print(msg_[1])
        continue
        
#    try:
#        y = int(y)
#    except ValueError:
    try:
        y = float(y)
    except ValueError:
        print(msg_[1])
        continue 

    b = ['+','-','/','*'] 
    if oper in b:
        pass
    else:
        print(msg_[2])
        continue
    
    check(x, y, oper)    
    
    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y
    elif oper == '/':
        if y == 0:
            print(msg_[3])
            continue 
        else:
            result = x / y
    print(float(result))
    
    while True:
        print(msg_[4])
        store_answer = input()
    
        if store_answer == 'y':
            
            if is_one_digit(result) == True:
                msg_index = 10
                while True:
                    print(msg_[msg_index])
                    oneDigit_answer = input()
                    if oneDigit_answer == 'y':
                        if msg_index < 12:
                            msg_index = msg_index + 1
                            continue
                        else:
                            memory = result
                            break
                    else:
                        if oneDigit_answer == 'n':
                            break
                        else:
                            continue
            else:
                memory = result
        else:
            if store_answer == 'n':
                pass
            else:
                continue
        break
        
    while True:
        print(msg_[5])    
        continue_answer = input()
        if continue_answer == 'y':
            break
    
        else:
            if continue_answer == 'n':
                pass
            else:
                continue
        break
    if continue_answer == 'y':
        continue            
    break


