def incorrectPasscodeAttempts(passcode, attempts):
    locked = 0
    

    for attempt in attempts:
        if attempt != passcode:
            locked += 1
        else:
            locked = 0
        
        if locked >= 10:
            return True
            
    return False

attempts = ["1111", "4444",
            "9999", "3333",
            "8888", "2222",
            "7777", "0000",
            "6666", "7285",
            "5555", "1111"]
print(incorrectPasscodeAttempts("1111", attempts))
