import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Get", command=self.on_button)
        self.button.pack()
        self.entry.pack()

    def on_button(self):
        print(self.entry.get())
        data=self.entry.get()
        Excel(data)
def Excel(self,data):
        from openpyxl import Workbook
        from openpyxl.compat import range
        wb = Workbook()
        ws1 = wb.active
        from openpyxl import load_workbook
        wb = load_workbook(filename = 'empty_book.xlsx')
        sheet_ranges = wb['Data']
        print(sheet_ranges['A2'].value)
        ws = wb.worksheets[0]
        ws['A1'] = data
        wb.save('empty_book.xlsx')

        
app = SampleApp()
app.mainloop()
