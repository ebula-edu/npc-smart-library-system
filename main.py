from gui import LibraryApp
import tkinter as tk

def main():
    root = tk.Tk()
    
    window_width = 800
    window_height = 600
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    app = LibraryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
