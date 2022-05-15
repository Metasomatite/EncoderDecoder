import base64 
import sys


def encode_str(s:str, encoding:str)->str:
    """
    encode string s into a specified encoding. 
    
    Supported encodings:
    - hex
    - base64
    """

    if encoding.lower()=='hex':
        e = 'hex'
    elif encoding.lower()=='base64':
        e = 'base64'
    else:
        raise NotImplementedError(
            f"Encoding {encoding} not implemented yet."
            )
    
    return {
        'hex':      lambda s: s.encode('utf-8').hex(),
        'base64':   lambda s: base64.b64encode(
                        s.encode('utf-8')
                    ).decode('utf-8'),
    }[e](s)

def decode_str(s:str, encoding:str)->str:
    """
    decode s of a specified encoding into string.
    
    Supported encodings:
    - hex
    - base64
    """

    if encoding.lower()=='hex':
        e = 'hex'
    elif encoding.lower()=='base64':
        e = 'base64'
    else:
        raise NotImplementedError(
            f"Encoding {encoding} not implemented yet."
            )
    
    return {
        'hex':      lambda s: bytes.fromhex(s).decode('utf-8'),
        'base64':   lambda s: base64.b64decode(s).decode('utf-8'),
    }[e](s)

def save_file(fname:str, s:str)->None:
    with open(fname, 'w') as f:
        f.write(s)
    
def load_encoded_file(fname:str, encoding:str=None)->str:
    with open(fname, 'r') as f:
        fcontents = f.read()
    
    return decode_str(s=fcontents, encoding=encoding) if encoding is not None else fcontents

def _cli_sys():
    """
    decode an encoded file via
        python encoder_decoder decode [encoding] [fname] [new_fname]

        new_fname = "decoded"+ fname by default

    encode an text file via
        python encoder_decoder encode [encoding] [fname] [new_fname]

        new_fname = fname by default
    """
    if len(sys.argv)>=4:
        encoding = sys.argv[2]
        fname = sys.argv[3]

        if sys.argv[1]=='decode':
            new_fname = sys.argv[4] if len(sys.argv)==5 else "decoded"+fname
            save_file(
                fname = new_fname, 
                s     = load_encoded_file(fname=fname, encoding=encoding)
                )
        elif sys.argv[1]=='encode':
            new_fname = sys.argv[4] if len(sys.argv)==5 else fname
            save_file(
                fname = new_fname, 
                s     = encode_str(
                        s        = load_encoded_file(fname=fname), 
                        encoding = encoding)
                    )
        else:
            raise ValueError("Either encode or decode.") 
def main(): 
    # s = '\tasdf\n'
    # # #Hex test
    # # encoded_s = str(s.encode('utf-8').hex())
    # # decoded_s = bytes.fromhex(encoded_s).decode('utf-8')
    # # print("encoded: ", encoded_s)
    # # print("decoded: ", decoded_s)

    # test_fname = "testing.txt"
    # save_file(test_fname, encode_str(s, 'base64'))
    # output_s = load_encoded_file(test_fname, 'base64')
    # print(output_s)
    _cli_sys()
if __name__=="__main__": main()