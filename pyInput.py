# Console Input Wrapper
# Canterbury School
# 11 March 2003
# -------------------------------

def cons_input(strPrompt):
    temp = raw_input(strPrompt)

    try:
        if (float (temp) != int (temp)):
            return float(temp)
        else:
            return int(temp)
    except:
        return temp
    
