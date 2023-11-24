import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()

app.title("Customtkinker App")
app.geometry("500x500")

frame = customtkinter.CTkFrame(master=app,
                               width=200,
                               height=200,
                               corner_radius=10,
                               bg_color="yellow")

frame.pack(padx=20, pady=20)

def button_func():
    print("The button is clicked")

button = customtkinter.CTkButton(master=app, text="Button", command=button_func)
button.place(relx=0.5, rely= 0.5, anchor = tkinter.CENTER)

app.mainloop()

