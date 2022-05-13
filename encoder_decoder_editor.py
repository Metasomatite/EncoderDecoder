

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import base64 

#edited from https://www.studytonight.com/tkinter/text-editor-application-using-tkinter
#TODO: make better GUI

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


def open_file():
    """Open a file for editing."""

    enc = encoding_var.get()

    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()

    if enc=='None':
        decoded_text = text
    else:
        try:
            decoded_text = decode_str(s=text, encoding = enc)
        except:
            tk.messagebox.showerror("error", f"Either loaded file is not of {enc} encoding, or something else happened.")
            return 

    txt_edit.insert(tk.END, decoded_text)
    window.title(f"Encoder Decoder - {filepath}")

def save_file():
    """Save the current file as a new file."""

    enc = encoding_var.get()

    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return

    text = txt_edit.get(1.0, tk.END)

    if enc==None:
        encoded_text = text 
    else:
        try:
            encoded_text = encode_str(s=text, encoding = enc)
        except:
            tk.messagebox.showerror("error", f"Either text cannot be encoded to {enc}, or something else happened.")
            return 

    with open(filepath, "w") as output_file:
        output_file.write(encoded_text)

    window.title(f"Encoder Decoder - {filepath}")

encodings = [
    'None',
    'base64', 
    'hex'
]

window = tk.Tk()
window.title("Encoder Decoder")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


encoding_var = tk.StringVar(window)
encoding_var.set(encodings[0]) # default value


txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

enclabel = tk.Label(fr_buttons, text="Encoding: ")
dropdown = tk.OptionMenu(fr_buttons, encoding_var, *encodings)


btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
enclabel.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
dropdown.grid(row=3, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


window.mainloop()