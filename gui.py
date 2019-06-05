import tkinter as tk
import tkinter.messagebox
import morse as m


def gui():
    def button_preloz():
        '''
        Algorytmus - dostane zpravu z input. Rozhodne jestli je morse nebo plaintext - var is_morse. Prevede na opacnou
        a ulozi do var output. Output vypise do okna output.
        '''
        print('button P pressed')
        input_text = inputbox.get(0.0,'end')

        input_ismorse = False
        if '.' and '-' and '/' in input_text:
            input_ismorse=True

        if input_ismorse:
            output = m.Morse().dec(input_text)
        else:
            output = m.Morse().enc(input_text)

        disp_output(output)     # Zobrazi vysledek ve spodnim okne


    def disp_output(message):
        outputbox.config(state='normal')    # Prepsani outputboxu
        outputbox.delete(0.0, 'end')
        outputbox.insert('end', message)

    def write_file():
        text = outputbox.get(0.0,'end')
        filename = e_filename.get()
        if not filename.endswith('.txt'):
            filename += '.txt'

        with open(filename, 'w') as f:  # todo - pridat varovani pred prepsanim existujiciho souboru
            f.write(text)

        tkinter.messagebox.showinfo('Info', message=f"Zpráva uložena jako '{filename}'")


    label_font = ('Arial', 11)
    text_font = ('Calibri', 12)

    xstart=15   # Starting placing widgets at..
    ystart=0    # first frame starting

    root = tk.Tk()
    root.title('Morse')
    root.geometry('650x600') # WixHe

    # Todo - nahore lista s funkci nahrat soubor

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

    b_uloz = tk.Button(frame21, text='Uložit', font=label_font, command=write_file)
    b_uloz.pack(side='left')



    root.mainloop()

if __name__ == '__main__':
    gui()
