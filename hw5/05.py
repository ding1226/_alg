def will_stop():
    return 0  #立即停止

def will_infinite_loop():
    while True:
        pass  #無窮循環

def check_halt(program):
    try:
        program() 
        return True  
    except:
        return False 
        

print(check_halt(will_stop)) 
print(check_halt(will_infinite_loop))  
