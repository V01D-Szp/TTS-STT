import keyboard
import espeakng
import tkinter as tk 

class MainTTS: 
       
    Console = tk.Tk()
    Console.title("Marta will say this:")
    Console.geometry("400x50")

    Dialog = tk.Entry(Console, font=("Arial", 14))
    Dialog.pack(padx=10, pady=10, fill="x")
    Dialog.focus()

    Text = "" 

    while True:
        Console.update() 
        if keyboard.is_pressed('enter'):
                        
            Text = Dialog.get().strip()
            Martha2=espeakng.Speaker()
            Martha2.voice='mb-us1'
            Martha2.say(Text)           
            break

    Console.destroy()       

    print("\n")
    print("You typed:", Text)
    print("\n")

        

        