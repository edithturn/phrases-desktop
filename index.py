from tkinter import ttk
from tkinter import *

import sqlite3

class Phrase:

    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title('Phrases Application')

        # Frame container
        frame = LabelFrame(self.wind, text = 'Register A new Phrase')
        frame.grid(row = 0, column = 0, columnspan = 4, pady = 20)

        # Name imput
        Label(frame, text = 'Phrase: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column =1)

        # Situation Input
        Label(frame, text = 'Situation').grid(row = 2, column = 0)
        self.situation = Entry(frame)
        self.situation.grid(row = 2, column = 1)

         # Phrase kind
        Label(frame, text = 'Phrase Kind').grid(row = 3, column = 0)
        self.kind = Entry(frame)
        self.kind.grid(row = 3, column = 1)

        # Button Add Phrase
        ttk.Button(frame, text = 'Save Phrase', command = self.add_phrase).grid(row = 4, columnspan = 2 , sticky = W + E)
        # Output Messages
        self.message = Label(text =  '', fg = 'red' )
        self.message.grid(row =4, column = 0, columnspan = 2, sticky = W + E )

        # Table
        self.tree = ttk.Treeview(height = 10, columns = 3)
        self.tree.grid(row =6, column = 0, columnspan = 2)        
        self.tree.heading('#0', text = 'Phrase', anchor = CENTER)
        self.tree.heading('#1', text = 'Situation', anchor = CENTER)
        #self.tree.heading('#2', text = 'kind', anchor = CENTER)

        ttk.Button(text = 'DELETE', command = self.delete_phrase).grid(row = 7, column =0 , sticky = W + E)
        ttk.Button(text = 'EDIT', command = self.edit_phrase).grid(row = 7, column =1 , sticky = W + E)


        self.get_phrases()

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_phrases(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
    
        query =  'SELECT * FROM phrase ORDER BY name DESC'
        db_rows = self.run_query(query)
        
        for row in db_rows:
            self.tree.insert('', 0, text = row[1],  values = row[2])
        print(db_rows)

    def validation(self):
        return len(self.name.get()) != 0 and len(self.situation.get()) != 0

    def add_phrase(self):
        if self.validation():
            query = 'INSERT INTO phrase VALUES(NULL, ?, ?, ?)'
            parameters = (self.name.get(), self.situation.get(), self.kind.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Product {} added Succefully'.format(self.name.get())
            self.name.delete(0, END)
            self.situation.delete(0, END)
            self.kind.delete(0, END)
        else:
            self.message['text'] = 'Name and Price are Requiered'
        self.get_phrases()


    def delete_phrase(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a record'
            return
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM phrase WHERE name = ?'
        self.run_query(query, (name, ))
        self.message['text'] = 'Record {} deleted Successfully'.format(name)
        self.get_phrases()

    def edit_phrase(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a record'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_name = self.tree.item(self.tree.selection())['text']
        #old_situation = self.tree.item(self.tree.selection())['values'][0]
        #old_kind = self.tree.item(self.tree.selection())['values'][2]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Phrase'


        Label(self.edit_wind, text = 'Old name: ').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_name), state = 'readonly').grid(row = 2, column =2)

        #Label(self.edit_wind, text = 'Old Kind: ').grid(row = 2, column = 1)
        new_situation = Entry(self.edit_wind)
        new_situation.grid(row = 3, column = 2)
        #Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_situation), state = 'readonly').grid(row = 1, column =2)
        #Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_kind), state = 'readonly').grid(row = 2, column =2)


if __name__ == '__main__' :
    window = Tk()
    application = Phrase(window)
    window.mainloop() 


