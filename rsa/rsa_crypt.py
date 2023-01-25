import base64
if __name__ == "__main__":

    print("""\
------------------------
RSA Encrypt / Decrypt
------------------------
    """)
    
    n = int( input("Enter RSA n paramter: ") )
    e = int( input("Enter RSA e/d parameter: ") )

    txt = input("Test encryption, enter some text: ")
    print("""
    Text received: {t}
    """.format(t=txt))
    enc = ""
    dec = ""
    # encryption public (e)
    for t in list(txt):
        b = (ord(t) ** e) % n
        print(b, end=" ")
        enc += chr( b )
        
    print("\nencrypted:",enc)
    print("\nencrypted (b64):", base64.b64encode( enc.encode() ).decode() )
    
    d = int( input("To test your input, enter RSA other e/d parameter (exit to skip): ") )
    
    if d != "exit":
        # decryption private (d)
        for t in list(enc):
            print("d", ord(t))
            dec += chr( (ord(t) ** d) % n )
            
        print("decrypted:",dec)

        print("Decryption", "successful!" if dec == txt else "")
    
    print("done")
