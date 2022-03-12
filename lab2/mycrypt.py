import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    dump = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    elif len(s) < 1:
        raise ValueError
    if len(s.strip()) < len(s):
        raise ValueError
    tempStr = s.ljust(1000)
    i = 0
    for i in range(1000):
        if tempStr[i].isalpha():
            c = tempStr[i]
            # If character is å,ä or ö raises ValueError
            if ord(c) > 122:
                raise ValueError
            elif c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif tempStr[i] in digitmapping:
            crypted+=digitmapping[tempStr[i]]
        # Rot13 empty space for security against time attacks
        elif tempStr[i].isspace():
            dumbChars = ['a']
            delayChar = dumbChars[0]
            dump+=codecs.encode(delayChar,'rot13')
        else:
            raise ValueError
            
    return crypted
    
def decode(s):
    return encode(s).lower()
