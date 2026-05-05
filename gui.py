import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from data_manager import load_data, save_data, add_book, update_book, delete_book
from algorithm import binary_search, universal_search, merge_sort
from datetime import datetime
import os
import sys
import ctypes

BG_PAGE = "#F3F4F6"   
BG_PANEL = "#FFFFFF"    
PRIMARY_COLOR = "#4F46E5" 
ACCENT_COLOR = "#8B5CF6" 
SUCCESS_COLOR = "#10B981" 
DANGER_COLOR = "#EF4444"  
TEXT_COLOR = "#1F2937"
HEADER_COLOR = "#111827" 
FONT_MAIN = ("Inter", 10)
FONT_BOLD = ("Inter", 10, "bold")
FONT_TITLE = ("Inter", 26, "bold")
FONT_SUBTITLE = ("Inter", 12)
FONT_FOOTER = ("Inter", 9, "italic")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Library Search and Management System - NPC")
        self.root.geometry("1100x900")
        self.root.minsize(1000, 850)
        self.root.configure(bg=BG_PAGE)

        self.books = load_data()
        self.filtered_books = self.books

        self.npc_logo_path = resource_path("assets/npc-logo.webp")
        self.group_logo_path = resource_path("assets/group-one-logo.png")
        self.app_icon_path = resource_path("assets/final-logo-group-one.png")

        self.set_app_icon()

        self.setup_styles()
        self.setup_ui()

    def set_app_icon(self):
        if os.name == 'nt':
            myappid = 'npc.smartlibrary.system.v1' 
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        if os.path.exists(self.app_icon_path):
            try:
                icon_img = Image.open(self.app_icon_path)
                self.icon_photo = ImageTk.PhotoImage(icon_img)
                self.root.iconphoto(True, self.icon_photo)
            except Exception as e:
                print(f"Icon error: {e}")

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        
        style.configure("Treeview", 
                        background=BG_PANEL, 
                        foreground=TEXT_COLOR, 
                        rowheight=35, 
                        fieldbackground=BG_PANEL,
                        font=FONT_MAIN)
        style.map("Treeview", background=[('selected', PRIMARY_COLOR)], foreground=[('selected', 'white')])
        
        style.configure("Treeview.Heading", 
                        background="#E9ECEF", 
                        foreground=HEADER_COLOR, 
                        font=FONT_BOLD, 
                        relief="flat",
                        padding=10)

    def setup_ui(self):
        # --- HEADER ---
        header = tk.Frame(self.root, bg=BG_PANEL, pady=20, highlightthickness=1, highlightbackground="#DEE2E6")
        header.pack(fill="x", side="top")

        logo_container = tk.Frame(header, bg=BG_PANEL)
        logo_container.pack(expand=True)

        self.npc_logo = self.load_logo(self.npc_logo_path, (80, 80))
        if self.npc_logo:
            npc_label = tk.Label(logo_container, image=self.npc_logo, bg=BG_PANEL)
            npc_label.grid(row=0, column=0, rowspan=2, padx=20)

        title_frame = tk.Frame(logo_container, bg=BG_PANEL)
        title_frame.grid(row=0, column=1)
        
        title_label = tk.Label(title_frame, text="SMART LIBRARY SYSTEM", font=FONT_TITLE, fg=PRIMARY_COLOR, bg=BG_PANEL)
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Navotas Polytechnic College", 
                                font=FONT_SUBTITLE, fg=ACCENT_COLOR, bg=BG_PANEL)
        subtitle_label.pack(pady=2)
        
        self.group_logo = self.load_logo(self.group_logo_path, (80, 80))
        if self.group_logo:
            group_label = tk.Label(logo_container, image=self.group_logo, bg=BG_PANEL)
            group_label.grid(row=0, column=2, rowspan=2, padx=20)

        # --- MANAGEMENT ---
        input_parent = tk.LabelFrame(self.root, text=" 📚 Book Management", bg=BG_PANEL, font=FONT_BOLD, fg=PRIMARY_COLOR, padx=30, pady=20, borderwidth=1, relief="flat")
        input_parent.pack(padx=50, pady=20, fill="x")

        input_grid = tk.Frame(input_parent, bg=BG_PANEL)
        input_grid.pack(fill="x")

        # Two-column layout for inputs
        left_col = tk.Frame(input_grid, bg=BG_PANEL)
        left_col.pack(side="left", expand=True, fill="x")
        right_col = tk.Frame(input_grid, bg=BG_PANEL)
        right_col.pack(side="left", expand=True, fill="x")

        self.create_input_field(left_col, "Book ID:", "id_entry", 0)
        self.create_input_field(left_col, "Book Title:", "title_entry", 1)
        self.create_input_field(left_col, "Author Name:", "author_entry", 2)
        
        self.create_input_field(right_col, "Location:", "location_entry", 0)
        self.create_input_field(right_col, "Shelf/Section:", "shelf_entry", 1)
        
        # Availability Toggle
        avail_frame = tk.Frame(right_col, bg=BG_PANEL)
        avail_frame.grid(row=2, column=0, columnspan=2, sticky="w", padx=15, pady=8)
        
        tk.Label(avail_frame, text="Availability Status:", font=FONT_MAIN, bg=BG_PANEL, fg=TEXT_COLOR).pack(side="left")
        self.avail_var = tk.BooleanVar(value=True)
        self.avail_check = tk.Checkbutton(avail_frame, text="Available for Borrowing", variable=self.avail_var, 
                                        font=FONT_MAIN, bg=BG_PANEL, activebackground=BG_PANEL, fg=SUCCESS_COLOR,
                                        selectcolor=BG_PANEL)
        self.avail_check.pack(side="left", padx=10)

        btn_container = tk.Frame(input_parent, bg=BG_PANEL, pady=15)
        btn_container.pack()

        self.create_button(btn_container, "ADD BOOK", self.handle_add, 0)
        self.create_button(btn_container, "UPDATE", self.handle_update, 1)
        self.create_button(btn_container, "DELETE", self.handle_delete, 2, color=DANGER_COLOR)
        self.create_button(btn_container, "CLEAR", self.clear_inputs, 3, color="#6B7280")

        # --- SEARCH & SORT ---
        search_outer = tk.Frame(self.root, bg=BG_PAGE)
        search_outer.pack(fill="x", padx=50)

        search_frame = tk.Frame(search_outer, bg=BG_PANEL, pady=10, highlightthickness=1, highlightbackground="#DEE2E6")
        search_frame.pack(fill="x")
        
        search_label = tk.Label(search_frame, text="🔍 Search:", font=FONT_BOLD, bg=BG_PANEL, fg=TEXT_COLOR)
        search_label.pack(side="left", padx=(20, 5))
        
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self.on_search_change)
        
        self.search_entry = tk.Entry(search_frame, textvariable=self.search_var, font=("Segoe UI", 12), 
                                   bg="#F8F9FA", fg=TEXT_COLOR, relief="flat")
        self.search_entry.pack(side="left", padx=10, ipady=8, fill="x", expand=True)

        # Sorting Dropdown
        sort_label = tk.Label(search_frame, text="Sort By:", font=FONT_BOLD, bg=BG_PANEL, fg=TEXT_COLOR)
        sort_label.pack(side="left", padx=(20, 5))

        self.sort_var = tk.StringVar(value="ID (Asc)")
        self.sort_options = {
            "ID (Asc)": ("id", False),
            "ID (Desc)": ("id", True),
            "Title (A-Z)": ("title", False),
            "Title (Z-A)": ("title", True),
            "Author (A-Z)": ("author", False),
            "Author (Z-A)": ("author", True),
            "Date (Newest)": ("date_added", True),
            "Date (Oldest)": ("date_added", False)
        }
        
        self.sort_combo = ttk.Combobox(search_frame, textvariable=self.sort_var, 
                                     values=list(self.sort_options.keys()), 
                                     state="readonly", font=FONT_MAIN, width=15)
        self.sort_combo.pack(side="left", padx=10, ipady=5)
        self.sort_combo.bind("<<ComboboxSelected>>", self.on_search_change)
        
        clear_search_btn = tk.Button(search_frame, text="Clear Search", command=lambda: self.search_var.set(""),
                                   font=FONT_BOLD, bg=PRIMARY_COLOR, fg="white", borderwidth=0, padx=20, cursor="hand2")
        clear_search_btn.pack(side="right", padx=20, ipady=5)

        # --- TABLE ---
        table_container = tk.Frame(self.root, bg=BG_PANEL, highlightthickness=1, highlightbackground="#DEE2E6")
        table_container.pack(fill="both", expand=True, padx=50, pady=(20, 10))

        tree_scroll = ttk.Scrollbar(table_container)
        tree_scroll.pack(side="right", fill="y")

        self.tree = ttk.Treeview(table_container, columns=("ID", "Title", "Author", "Location", "Shelf", "Status", "Date"), show="headings", yscrollcommand=tree_scroll.set)
        
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="BOOK TITLE")
        self.tree.heading("Author", text="AUTHOR")
        self.tree.heading("Location", text="LOCATION")
        self.tree.heading("Shelf", text="SHELF")
        self.tree.heading("Status", text="STATUS")
        self.tree.heading("Date", text="DATE ADDED")

        self.tree.column("ID", width=80, anchor="center")
        self.tree.column("Title", width=250)
        self.tree.column("Author", width=180)
        self.tree.column("Location", width=120)
        self.tree.column("Shelf", width=100)
        self.tree.column("Status", width=100, anchor="center")
        self.tree.column("Date", width=150)

        self.tree.pack(fill="both", expand=True)
        tree_scroll.config(command=self.tree.yview)

        # Status Coloring Tags
        self.tree.tag_configure("borrowed", foreground=DANGER_COLOR)

        # Empty state label
        self.empty_label = tk.Label(self.tree, text="No books found matching your search.", 
                                   font=FONT_SUBTITLE, bg=BG_PANEL, fg="#9CA3AF")
        
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        
        # --- FOOTER ---
        footer_frame = tk.Frame(self.root, bg=BG_PAGE, pady=10)
        footer_frame.pack(side="bottom", fill="x")
        
        footer_label = tk.Label(footer_frame, text="Group 1 - Byte Me Maybe", 
                                font=FONT_FOOTER, fg="#7F8C8D", bg=BG_PAGE)
        footer_label.pack()
        
        self.refresh_display()

    def load_logo(self, path, size):
        if os.path.exists(path):
            try:
                img = Image.open(path)
                img = img.resize(size, Image.Resampling.LANCZOS)
                return ImageTk.PhotoImage(img)
            except: pass
        return None

    def create_input_field(self, parent, label_text, attr_name, row):
        label = tk.Label(parent, text=label_text, font=FONT_MAIN, bg=BG_PANEL, fg=TEXT_COLOR)
        label.grid(row=row, column=0, sticky="w", padx=15, pady=5)
        
        entry = tk.Entry(parent, font=("Inter", 11), bg="#F9FAFB", fg=TEXT_COLOR, relief="solid", borderwidth=1, width=35)
        entry.grid(row=row, column=1, padx=15, pady=5, ipady=8)
        setattr(self, attr_name, entry)

    def create_button(self, parent, text, command, col, color=PRIMARY_COLOR):
        btn = tk.Button(parent, text=text, command=command, font=FONT_BOLD,
                       bg=color, fg="white", activebackground=ACCENT_COLOR, 
                       activeforeground="white", width=15, pady=8, borderwidth=0, cursor="hand2")
        btn.grid(row=0, column=col, padx=8)

    def on_search_change(self, *args):
        query = self.search_var.get()
        # 1. Filter
        filtered = universal_search(self.books, query)
        
        # 2. Sort using Merge Sort
        sort_key, is_reverse = self.sort_options.get(self.sort_var.get(), ("id", False))
        self.filtered_books = merge_sort(filtered, sort_key, is_reverse)
        
        self.refresh_display()

    def refresh_display(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        if not self.filtered_books:
            if not self.books:
                self.empty_label.config(text="Library is empty. Add your first book above! 📚")
            else:
                self.empty_label.config(text="No books found matching your search. 🔍")
            self.empty_label.place(relx=0.5, rely=0.5, anchor="center")
        else:
            self.empty_label.place_forget()
            
        for book in self.filtered_books:
            date = book.get("date_added", "N/A")
            location = book.get("location", "N/A")
            shelf = book.get("shelf", "N/A")
            is_avail = book.get("available", True)
            status = "Available" if is_avail else "Borrowed"
            status_tags = ("borrowed",) if not is_avail else ()
            
            self.tree.insert("", "end", values=(
                book['id'], 
                book['title'], 
                book['author'], 
                location, 
                shelf, 
                status, 
                date
            ), tags=status_tags)

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            values = item['values']
            self.clear_inputs()
            self.id_entry.insert(0, values[0])
            self.title_entry.insert(0, values[1])
            self.author_entry.insert(0, values[2])
            self.location_entry.insert(0, values[3])
            self.shelf_entry.insert(0, values[4])
            self.avail_var.set(True if values[5] == "Available" else False)

    def handle_add(self):
        try:
            bid_str = self.id_entry.get().strip()
            title = self.title_entry.get().strip()
            author = self.author_entry.get().strip()

            if not bid_str or not title or not author:
                messagebox.showwarning("Warning", "Fill in all fields!")
                return
            
            bid = int(bid_str)
            if binary_search(self.books, bid):
                messagebox.showerror("Error", f"Book ID {bid} already exists!")
                return

            location = self.location_entry.get().strip() or "Main Hall"
            shelf = self.shelf_entry.get().strip() or "General"
            available = self.avail_var.get()

            date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
            new_book = {
                "id": bid, 
                "title": title, 
                "author": author, 
                "location": location,
                "shelf": shelf,
                "available": available,
                "date_added": date_str
            }
            
            self.books = add_book(self.books, new_book)
            save_data(self.books)
            self.on_search_change()
            self.clear_inputs()
            messagebox.showinfo("Success", "Book added to system database.")
        except ValueError:
            messagebox.showerror("Error", "ID must be numeric!")

    def handle_update(self):
        try:
            bid_str = self.id_entry.get().strip()
            if not bid_str: return
            bid = int(bid_str)
            
            title = self.title_entry.get().strip()
            author = self.author_entry.get().strip()

            if not binary_search(self.books, bid):
                messagebox.showerror("Error", "Book ID not found!")
                return

            updated_fields = {}
            if title: updated_fields["title"] = title
            if author: updated_fields["author"] = author
            
            location = self.location_entry.get().strip()
            shelf = self.shelf_entry.get().strip()
            
            if location: updated_fields["location"] = location
            if shelf: updated_fields["shelf"] = shelf
            updated_fields["available"] = self.avail_var.get()

            self.books = update_book(self.books, bid, updated_fields)
            save_data(self.books)
            self.on_search_change()
            messagebox.showinfo("Updated", "Book record has been updated.")
        except ValueError:
            messagebox.showerror("Error", "Invalid Book ID!")

    def handle_delete(self):
        try:
            bid_str = self.id_entry.get().strip()
            if not bid_str: return
            bid = int(bid_str)
            
            if not binary_search(self.books, bid):
                messagebox.showerror("Error", "Book ID not found!")
                return

            if messagebox.askyesno("Confirm", "Delete this book record permanently?"):
                self.books = delete_book(self.books, bid)
                save_data(self.books)
                self.on_search_change()
                self.clear_inputs()
        except ValueError:
            messagebox.showerror("Error", "Invalid Book ID!")

    def clear_inputs(self):
        self.id_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        self.shelf_entry.delete(0, tk.END)
        self.avail_var.set(True)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
