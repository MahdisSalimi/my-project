import tkinter as tk
from tkinter import messagebox 

class HotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel reservasion system")

        #دیتابیس اتاق ها 
        self.hotel_rooms = {
             101: {"status": "empty" , "guest": ""} ,
             102: {"status": "empty" , "guest": ""} ,
             201: {"status": "empty" , "guest": ""} ,
             202: {"status": "empty" , "guest": ""}
        } 
        # ایجاد ویجت ها
        self.creat_widgets()

    def creat_widgets(self):
        # فریم اصلی
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack()

        # عنوان
        tk.Label(main_frame, text="Hotel reservation managment", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # دکمه ها
        tk.Button(main_frame, text="show rooms", command=self.show_rooms, width=15).grid(row=1, column=0, pady=5)
        tk.Button(main_frame, text="room reservation", command=self.reserve_window, width=15).grid(row=2, column=0, pady=5)
        tk.Button(main_frame, text="cancel the reservation", command=self.cancel_window, width=15).grid(row=3, column=0, pady=5)
        tk.Button(main_frame, text="exit", command=self.root.quit, width=15).grid(row=4, column=0, pady=5)

        # ناحیه نمایش اطلاعات
        self.info_text = tk.Text(main_frame, width=40, height=10, state='disabled')
        self.info_text.grid(row=1, column=1, rowspan=4, padx=10)    

    def show_rooms(self):   
        self.info_text.config(state='normal')
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, "the condition of yhe hotels rooms:\n\n")


        for room, info in self.hotel_rooms.items():
            status = "free" if info["status"] == "empty" else f"reserved by {info['guest']}"
            self.info_text.insert(tk.END, f"room {room}: {status}\n")

        self.info_text.config(state= 'disabled')

    def reserve_window(self):
         # پنجره جدید برای رزرو
         reserve_win = tk.Toplevel(self.root)
         reserve_win.title("room reservation")

         tk.Label(reserve_win, text="number of room:").grid(row=0 , column=0, padx=5, pady=5)
         room_entry = tk.Entry(reserve_win)
         room_entry.grid(row=0, column=1, padx=5, pady=5)
        
         tk.Label(reserve_win, text="guset name:").grid(row=1, column=0, padx=5, pady=5)
         guest_entry = tk.Entry(reserve_win)
         guest_entry.grid(row=1, column=1, padx=5, pady=5)

         def do_reserve():
             try:
                 room_num = int(room_entry.get())
                 guest_name = guest_entry.get()

                 if room_num not in self.hotel_rooms:
                     messagebox.showerror("Error!""Room does not exist")
                     return
                 if self.hotel_rooms[room_num]["status"] == "reserved":
                     messagebox.showwarning("error!", "This room has already been booked")
                     return
                 self.hotel_rooms[room_num]["status"] = "reserved"
                 self.hotel_rooms[room_num]["guest"] = guest_name
                 messagebox.showinfo("successful" ,  f"room {room_num} booked successfully!")
                 reserve_win.destroy()
                 self.show_rooms()
             except ValueError:
                 messagebox.showerror("Error!" , "room number must be a number ⚠")

         tk.Button(reserve_win, text="confirmation of reservation", command=do_reserve).grid(row=2, columnspan=2, pady=10)
        
    def cancel_window(self):
        # پنجره جدید برای لغو رزرو

        cancel_win = tk.Toplevel(self.root)
        cancel_win.title("cancel the reservation")

        tk.Label(cancel_win, text="number of room:").grid(row=0, column=0, padx=5, pady=5)
        room_entry = tk.Entry(cancel_win)
        room_entry.grid(row=0, column=1, padx=5, pady=5)

        def do_cancel():
            try:
                room_num = int(room_entry.get())

                if room_num not in  self.hotel_rooms:
                    messagebox.showerror("error!", "there is no room❌")
                    return
                
                if self.hotel_rooms[room_num]["status"] == "empty":
                    messagebox.showwarning("Error!", f"room {room_num} is already empty ❗")
                
                self.hotel_rooms[room_num]["status"] = "empty"
                self.hotel_rooms[room_num]["guest"] = ""
                messagebox.showinfo("successful !", "canceled successfully ")
                cancel_win.destroy()
                self.show_rooms()

            except ValueError:
                messagebox.showerror("Error!", "the room number must be a number")

        tk.Button(cancel_win, text="cancel confirmation", command=do_cancel).grid(row=1, columnspan=2, pady=10)

# اجرای برنامه
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()