import base64

def enc(chrs, n, ed):
    res = ""
    for c in list(chrs):
        b = (ord(c) ** ed) % n
        h = str(hex(b))[2:]
        res += ''.join(['0' for i in range(4-len(h))]) + h
    return base64.b64encode( res.encode() ).decode()

def dec(chrs, n, ed):
    res = ""
    try: chrs = base64.b64decode( chrs.encode() ).decode()
    except: pass
    for c in [ chrs[i:i+4] for i in range(0, len(chrs), 4) ]:
        b = (int(c, 16) ** ed) %  n
        res += chr(b)
    return res

if __name__ == "__main__":

    print( enc("Hello World!", 6731, 37) )
    print( dec("MGVlYjE3NDQwYWQ3MGFkNzEyNTkwZDZkMTMwOTEyNTkxMDNjMGFkNzEyZjMxNTVm", 6731, 2125) )
        
    pass
    
