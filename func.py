def checker(email):
    email = list(email)
    if '@' in email:
        
        if email[0] != '@' and email[-5] != '@':
        
            if email[-4] == '.' and email[-3] == 'o' and email[-2] == 'r' and email[-1] == 'g':
                return True
            if email[-4] == '.' and email[-3] == 'c' and email[-2] == 'o' and email[-1] == 'm':
                return True
            if email[-4] == '.' and email[-3] == 'g' and email[-2] == 'o' and email[-1] == 'v':
                return True
            if email[-4] == '.' and email[-3] == 'n' and email[-2] == 'e' and email[-1] == 't':
                return True
            if email[-4] == '.' and email[-3] == 'e' and email[-2] == 'd' and email[-1] == 'u':
                return True
            
    return False


            

