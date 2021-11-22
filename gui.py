import tkinter as tk
import tkinter.messagebox
import morse as m
import os

def gui():
    # todo odsud dal zrejme dat do noveho souboru guifuns
    def button_preloz():
        '''
        Algorytmus - dostane zpravu z input. Rozhodne jestli je morse nebo plaintext - var is_morse. Prevede na opacnou
        a ulozi do var output. Output vypise do okna output.
        '''
        input_text = inputbox.get(0.0,'end')
        input_ismorse = m.is_morse(input_text)
        input_text_list = input_text.split("\n")    # Textbox nechává na konci prázdý str, tohle ho smaže


        output=[]
        if input_ismorse:
            for line in input_text_list:
                output.append(m.Morse().dec(line))
        else:
            for line in input_text_list:
                output.append(m.Morse().enc(line))
                # todo Vymyslet nejake normalni oddelovani / (jak ma zacinat x koncit radek)
        disp_output('\n'.join(pretify_output(output)))     # Zobrazi vysledek ve spodnim okne
    
    def pretify_output(message: list):
        try:
            message.remove("")
        except ValueError:
            pass
        try:
            message.remove(".")
        except ValueError:
            pass
        return message

    def disp_output(message):
        outputbox.config(state='normal')    # Prepsani outputboxu
        outputbox.delete(0.0, 'end')
        outputbox.insert('end', message)

    def writefile(filename, content):     # zatim asi redundant
        with open(filename, 'w') as f:
            f.write(content)

    def uloz():
        text = outputbox.get(0.0,'end')
        filename = e_filename.get()
        if not filename.endswith('.txt'):   # prida priponu .txt
            filename += '.txt'

        # if file with given name exists: display warning window - proceed or not
        if os.path.isfile(filename):
            rewrite = tk.messagebox.askyesno('Warning', 'Tento soubor už existuje. Přejete si ho přepsat?',
                                             icon='warning')   # returns True or False
            if not rewrite:
                print('soubor ulozen nebude')
                return  # (else pokračuj)

        writefile(filename, text)
        tkinter.messagebox.showinfo('Info', message=f"Zpráva uložena jako '{filename}'")
    # dat do guifuns po sem



    label_font = ('Arial', 11)
    text_font = ('Calibri', 12)

    xstart=15   # Starting placing widgets at..
    ystart=0    # first frame starting

    root = tk.Tk()
    root.title('Morse')
    root.geometry('650x600') # WixHe

    # Todo - nahore lista s funkci nahrat soubor, ulozit, napoveda...

    # Prvni tretina appky
    frame1_height=220
    frame1=tk.Frame(root, bg='#bbbbbb', height=frame1_height)
    frame1.place(anchor='nw', relwidth=1, y=ystart)

    l_zprava=tk.Label(frame1, text='Zpráva:', font=label_font)
    l_zprava.place(x=xstart, y=10)

    inputbox=tk.Text(frame1, width=85, height=8, font=text_font)
    inputbox.place(x=xstart, y=30)

    frame11=tk.Frame(frame1, height=35, width=600, bg='#71d4fe')    # Todo - zmenit barvu na totoznou s pozadim
    frame11.place(x=xstart, y=188)

    b_preloz = tk.Button(frame11, text='Přelož', font=label_font, command=button_preloz)
    # b_preloz.place(anchor = 'nw')
    b_preloz.pack(side='left')  # Looks much better so far and is easier


    #Druha tretina appky
    frame2_height=240
    frame2 = tk.Frame(root, bg='#bbbbbb', height=frame2_height)
    frame2.place(anchor='nw', relwidth=1, y=frame1_height + 10)

    l_prelozeno=tk.Label(frame2, text='Přeloženo:', font=label_font)
    l_prelozeno.place(anchor='nw', y=10, x=xstart)

    outputbox=tk.Text(frame2, width=85, height=9, font=text_font)
    outputbox.place(anchor='nw', y=30, x=xstart)

    frame21 = tk.Frame(frame2, height=25, width=600, bg='#71d4fe')  # Todo - zmenit barvu na totoznou s pozadim
    frame21.place(x=xstart, y=210)

    l_ulozit = tk.Label(frame21, text='Ulozit jako  ', font=label_font)
    l_ulozit.pack(side='left')

    e_filename = tk.Entry(frame21)
    e_filename.pack(side='left')

    tk.Frame(frame21, width=20).pack(side='left')

    b_uloz = tk.Button(frame21, text='Uložit', font=label_font, command=uloz)
    b_uloz.pack(side='left')

    # Todo - posledni tretina na tvorbu audio souboru

    root.mainloop()

if __name__ == '__main__':
    gui()
