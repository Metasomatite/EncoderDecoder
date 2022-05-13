# Encoder Decoder

Transforms a file in some encoding into UTF-8, 
allows for the file to be edited, then transform
the edited file back into the original encoding.

Encodings proposed:
- base64
- hex
- quopri
- uuencode
- zip
- rot13

Proposed features:
- allow for arbituary encoders and decoders with the correct functional interface.


# Encoding and Decoding in python
The following examples have similar forms. For instance, from python string to binary string and back.
```
>>> '\tastf\n'.encode('utf-8')
b'\tastf\n'
>>> b'\tastf\n'.decode('utf-8')
'\tastf\n'
```


From UTF-8 to hex and back.
```
>>> s_str = "\tasdf\n"
>>> s_hex = s_str.encode('utf-8').hex()
>>> s_hex
'09617364660a'
>>> bytes.fromhex(s_hex).decode('utf-8')
'\tasdf\n'
```

From UTF-8 to base64 and back.
```
>>> import base64
>>> base64.b64encode('\tasdf\n'.encode('utf-8'))
b'CWFzZGYK'
>>> base64.b64decode('CWFzZGYK')
b'\tasdf\n'
```