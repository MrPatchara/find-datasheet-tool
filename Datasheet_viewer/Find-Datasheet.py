import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import webbrowser
import sqlite3
import os

# Initialize the database
def init_db():
    conn = sqlite3.connect('datasheets.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS datasheets (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        type TEXT NOT NULL,
                        filepath TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

# Add datasheet to the database
def add_datasheet(name, type, filepath):
    conn = sqlite3.connect('datasheets.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO datasheets (name, type, filepath) VALUES (?, ?, ?)''', (name, type, filepath))
    conn.commit()
    conn.close()

# Update datasheet in the database
def update_datasheet(datasheet_id, name, type):
    conn = sqlite3.connect('datasheets.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE datasheets SET name = ?, type = ? WHERE id = ?''', (name, type, datasheet_id))
    conn.commit()
    conn.close()

# Remove datasheet from the database
def remove_datasheet(datasheet_id):
    conn = sqlite3.connect('datasheets.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM datasheets WHERE id = ?''', (datasheet_id,))
    conn.commit()
    conn.close()

# Fetch all datasheets from the database
def fetch_datasheets():
    conn = sqlite3.connect('datasheets.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM datasheets''')
    datasheets = cursor.fetchall()
    conn.close()
    return datasheets

# Search datasheets in the database
def search_datasheets(keyword):
    conn = sqlite3.connect('datasheets.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM datasheets WHERE name LIKE ?''', ('%' + keyword + '%',))
    datasheets = cursor.fetchall()
    conn.close()
    return datasheets

# Fetch datasheets by type from the database
def fetch_datasheets_by_type(type):
    conn = sqlite3.connect('datasheets.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM datasheets WHERE type = ?''', (type,))
    datasheets = cursor.fetchall()
    conn.close()
    return datasheets

class DatasheetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Datasheet Viewer")

        self.create_menu()
        self.create_widgets()
        self.populate_datasheet_list()

    def create_menu(self):
        # Create menu bar
        menubar = tk.Menu(self.root)
        
        # Create 'File' menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Create 'Help' menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Contact Developer", command=self.contact_developer)
        menubar.add_cascade(label="Help", menu=help_menu)
        
        # Attach menu bar to the root window
        self.root.config(menu=menubar)

    def create_widgets(self):
        # Frame for component input and search
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        self.label = tk.Label(input_frame, text="Name:")
        self.label.grid(row=0, column=0, padx=5)

        self.entry = tk.Entry(input_frame, width=30)
        self.entry.grid(row=0, column=1, padx=5)

        self.type_label = tk.Label(input_frame, text="Type:")
        self.type_label.grid(row=1, column=0, padx=5, pady=5)

        self.type_var = tk.StringVar()
        self.type_combo = ttk.Combobox(input_frame, textvariable=self.type_var, width=28)
        self.type_combo['values'] = ('IC', 'Transistor', 'Resistor', 'Capacitor', 'Diode', 'Other')
        self.type_combo.current(0)
        self.type_combo.grid(row=1, column=1, padx=5, pady=5)

        # Frame for action buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.search_button = tk.Button(button_frame, text="Search Online", command=self.search_datasheet_online)
        self.search_button.grid(row=0, column=0, padx=5)

        self.open_button = tk.Button(button_frame, text="Open Local", command=self.open_file)
        self.open_button.grid(row=0, column=1, padx=5)

        self.add_button = tk.Button(button_frame, text="Add to Database", command=self.add_to_database)
        self.add_button.grid(row=1, column=0, padx=5, pady=5)

        self.remove_button = tk.Button(button_frame, text="Remove from Database", command=self.remove_from_database)
        self.remove_button.grid(row=1, column=1, padx=5, pady=5)

        self.edit_button = tk.Button(button_frame, text="Edit Selected", command=self.edit_datasheet)
        self.edit_button.grid(row=2, column=0, padx=5, pady=5)

        self.view_button = tk.Button(button_frame, text="View Details", command=self.view_details)
        self.view_button.grid(row=2, column=1, padx=5, pady=5)

        # Frame for search and filter
        search_filter_frame = tk.Frame(self.root)
        search_filter_frame.pack(pady=10)

        self.search_local_label = tk.Label(search_filter_frame, text="Search in Database:")
        self.search_local_label.grid(row=0, column=0, padx=5)

        self.search_local_entry = tk.Entry(search_filter_frame, width=30)
        self.search_local_entry.grid(row=0, column=1, padx=5)

        self.search_local_button = tk.Button(search_filter_frame, text="Search", command=self.search_local_database)
        self.search_local_button.grid(row=0, column=2, padx=5)

        self.filter_label = tk.Label(search_filter_frame, text="Filter by Type:")
        self.filter_label.grid(row=1, column=0, padx=5, pady=5)

        self.filter_var = tk.StringVar()
        self.filter_combo = ttk.Combobox(search_filter_frame, textvariable=self.filter_var, width=28)
        self.filter_combo['values'] = ('All', 'IC', 'Transistor', 'Resistor', 'Capacitor', 'Diode', 'Other')
        self.filter_combo.current(0)
        self.filter_combo.grid(row=1, column=1, padx=5, pady=5)

        self.filter_button = tk.Button(search_filter_frame, text="Filter", command=self.filter_by_type)
        self.filter_button.grid(row=1, column=2, padx=5, pady=5)

        # Frame for datasheet list
        list_frame = tk.Frame(self.root)
        list_frame.pack(pady=10)

        self.datasheet_list_label = tk.Label(list_frame, text="Available Datasheets:")
        self.datasheet_list_label.pack(pady=5)

        self.datasheet_listbox = tk.Listbox(list_frame, width=80)
        self.datasheet_listbox.pack(pady=5)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=10)

    def populate_datasheet_list(self):
        self.datasheet_listbox.delete(0, tk.END)
        datasheets = fetch_datasheets()
        for ds in datasheets:
            self.datasheet_listbox.insert(tk.END, f"{ds[0]}: {ds[1]} ({ds[2]}) - {ds[3]}")

    def search_datasheet_online(self):
        component = self.entry.get()
        if component:
            url = f"https://www.datasheetarchive.com/{component}-datasheet.html"
            webbrowser.open(url)
        else:
            messagebox.showwarning("Input Error", "Please enter a component name.")

    def open_file(self):
        selected = self.datasheet_listbox.curselection()
        if selected:
            datasheet_id = self.datasheet_listbox.get(selected).split(':')[0]
            conn = sqlite3.connect('datasheets.db')
            cursor = conn.cursor()
            cursor.execute('''SELECT filepath FROM datasheets WHERE id = ?''', (datasheet_id,))
            filepath = cursor.fetchone()[0]
            conn.close()
            if os.path.exists(filepath):
                webbrowser.open(f"file://{filepath}")
            else:
                messagebox.showerror("File Error", "File not found.")
        else:
            messagebox.showwarning("Selection Error", "Please select a datasheet from the list.")

    def add_to_database(self):
        component = self.entry.get()
        component_type = self.type_var.get()
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
        if component and component_type and file_path:
            add_datasheet(component, component_type, file_path)
            self.populate_datasheet_list()
        else:
            messagebox.showwarning("Input Error", "Please enter all details and select a file.")

    def remove_from_database(self):
        selected = self.datasheet_listbox.curselection()
        if selected:
            datasheet_id = self.datasheet_listbox.get(selected).split(':')[0]
            remove_datasheet(datasheet_id)
            self.populate_datasheet_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a datasheet from the list.")

    def search_local_database(self):
        keyword = self.search_local_entry.get()
        if keyword:
            self.datasheet_listbox.delete(0, tk.END)
            datasheets = search_datasheets(keyword)
            for ds in datasheets:
                self.datasheet_listbox.insert(tk.END, f"{ds[0]}: {ds[1]} ({ds[2]}) - {ds[3]}")
        else:
            messagebox.showwarning("Input Error", "Please enter a search keyword.")

    def filter_by_type(self):
        selected_type = self.filter_var.get()
        self.datasheet_listbox.delete(0, tk.END)
        if selected_type == 'All':
            datasheets = fetch_datasheets()
        else:
            datasheets = fetch_datasheets_by_type(selected_type)
        for ds in datasheets:
            self.datasheet_listbox.insert(tk.END, f"{ds[0]}: {ds[1]} ({ds[2]}) - {ds[3]}")

    def view_details(self):
        selected = self.datasheet_listbox.curselection()
        if selected:
            datasheet_id = self.datasheet_listbox.get(selected).split(':')[0]
            conn = sqlite3.connect('datasheets.db')
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM datasheets WHERE id = ?''', (datasheet_id,))
            datasheet = cursor.fetchone()
            conn.close()
            details = f"ID: {datasheet[0]}\nName: {datasheet[1]}\nType: {datasheet[2]}\nFilepath: {datasheet[3]}"
            messagebox.showinfo("Datasheet Details", details)
        else:
            messagebox.showwarning("Selection Error", "Please select a datasheet from the list.")

    def edit_datasheet(self):
        selected = self.datasheet_listbox.curselection()
        if selected:
            datasheet_id = self.datasheet_listbox.get(selected).split(':')[0]
            conn = sqlite3.connect('datasheets.db')
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM datasheets WHERE id = ?''', (datasheet_id,))
            datasheet = cursor.fetchone()
            conn.close()

            edit_window = tk.Toplevel(self.root)
            edit_window.title("Edit Datasheet")

            edit_label = tk.Label(edit_window, text="Edit Datasheet Information")
            edit_label.pack(pady=10)

            name_label = tk.Label(edit_window, text="Name:")
            name_label.pack(pady=5)
            name_entry = tk.Entry(edit_window, width=50)
            name_entry.insert(0, datasheet[1])
            name_entry.pack(pady=5)

            type_label = tk.Label(edit_window, text="Type:")
            type_label.pack(pady=5)
            type_var = tk.StringVar(value=datasheet[2])
            type_combo = ttk.Combobox(edit_window, textvariable=type_var)
            type_combo['values'] = ('IC', 'Transistor', 'Resistor', 'Capacitor', 'Diode', 'Other')
            type_combo.pack(pady=5)

            def save_changes():
                new_name = name_entry.get()
                new_type = type_var.get()
                if new_name and new_type:
                    update_datasheet(datasheet_id, new_name, new_type)
                    self.populate_datasheet_list()
                    edit_window.destroy()
                else:
                    messagebox.showwarning("Input Error", "Please enter all details.")

            save_button = tk.Button(edit_window, text="Save Changes", command=save_changes)
            save_button.pack(pady=10)
        else:
            messagebox.showwarning("Selection Error", "Please select a datasheet from the list.")

    def contact_developer(self):
        contact_info = "Developer: Patchara Al-umaree \nEmail: Patcharaalumaree@gmail.com\nGithub: https://github.com/MrPatchara"
        messagebox.showinfo("Contact Developer", contact_info)

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = DatasheetApp(root)
    root.mainloop()
