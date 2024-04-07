import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Login:
    def __init__(self):
        self.loginw = Tk()
        self.loginw.title("Login")
        self.loginw.geometry("650x450")
        self.loginw.resizable(0,0)
        self.loginw.config(bg="#12171c")

        self.username = StringVar(value="Username")
        self.password = StringVar(value="Password")
        self.base = sqlite3.connect("./login.db")
        self.cur = self.base.cursor()

        self.loginw.protocol("WM_DELETE_WINDOW", self.on_closing)  # OVERRIDING CLOSE BUTTON
        self.obj()

    def obj(self):
        self.loginframe = LabelFrame(self.loginw, bg="#1d2329", bd=5, relief="groove", padx=25, pady=25, highlightbackground="black")
        self.loginframe.place(relx=0.5, rely=0.5, anchor=CENTER)

        
        self.toplabel = Label(self.loginframe, fg="white", bg="#1d2329", text="LOGIN", font=("Montserrat", 27, "bold"))
        self.toplabel.pack(pady=10)

        self.us = ttk.Entry(self.loginframe, width=30, textvariable=self.username, font=("Montserrat", 14,"bold"), foreground='black')
        self.us.pack(pady=10, padx=5)
        self.us.bind('<FocusIn>', self.clear_username)

        self.pa = ttk.Entry(self.loginframe, width=30, textvariable=self.password, show="*", font=("Montserrat", 14,"bold"), foreground='black')
        self.pa.pack(pady=10, padx=5)
        self.pa.bind('<FocusIn>', self.clear_password)

        self.signin = Button(self.loginframe, text="Sign in", bg="#32373d", fg="white", width=15, command=self.checkuser, font=("Montserrat", 14,"bold"), highlightbackground="black", highlightthickness=3)
        self.signin.pack(pady=20)


    def clear_username(self, event):
        if self.username.get() == "Username":
            self.username.set("")

    def clear_password(self, event):
        if self.password.get() == "Password":
            self.password.set("")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.loginw.destroy()

    def checkuser(self):
        s = self.username.get().upper()
        s1 = self.password.get().upper()
        self.cur.execute("select * from users where username=? and password=?", (s, s1))
        l = self.cur.fetchall()
        if len(l) > 0:
            self.success()
        else:
            self.fail()

    def success(self):
        messagebox.showinfo("Success", "Login successful")
        self.loginw.quit()

    def fail(self):
        messagebox.showerror("Error", "The username or password is incorrect")

if __name__ == "__main__":
    app = Login()
    app.loginw.mainloop()
