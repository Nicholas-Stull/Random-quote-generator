import tkinter as tk
from random_quote_generator import get_random_quote




# Create tkinter window
window = tk.Tk()
window.title("Random Quote Generator")

# Create label to display quote
quote_label = tk.Label(window, text="", font=("Helvetica", 18), wraplength=500)
quote_label.pack(pady=20)



def generate_quote():
    quote_text = get_random_quote(wordcount=20)
    quote_label.config(text=quote_text)


# Create "Generate Quote" button
generate_button = tk.Button(
    window, text="Generate Quote", command=generate_quote)
generate_button.pack(pady=10)

# Start the tkinter event loop
window.mainloop()
