

def multiplyStrings(s1,s2):
    """
    Function that takes in 2 integers as strings and returns their product, also as a string.
    All inputs are assumed to be non-negative (0 or above).
    """
    if s1 == "0" or s2 == "0":
        return "0"
    elif s1 == '1':
        return s2
    elif s2 == '1':
        return s1
    else:
        return int_to_string(string_to_int(s1) * string_to_int(s2))


def string_to_int(str):
    """
    Helper function that converts strings to integers.
    All inputs are assumed to be non-negative.
    """
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    if len(str) == 1:
        return digits[str]
    else:
        str_rev = str[::-1]
        ret = 0
        for i in range(len(str_rev)):
            ret += digits[str_rev[i]] * (10**i)
        return ret

def int_to_string(int):
    """
    Helper function that converts integers back to strings.
    All inputs are assumed to be non-negative.
    """

    chars = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
    if int in chars.keys():
        return chars[int]
    else:
        ret = chars[int%10]
        counter = 0
        while int >= 10:
            int = int // 10
            dig = int%10
            ret = chars[dig] + ret
            counter += 1
        return ret