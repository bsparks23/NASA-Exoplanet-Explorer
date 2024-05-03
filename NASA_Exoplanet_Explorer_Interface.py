import tkinter as tk
from ttkbootstrap import Style
from PIL import Image, ImageTk
from NASA_Exoplanet_Explorer import fetch_exoplanet_data, generate_story

# Function to generate a story when the button is clicked
def generate_button_clicked():
    exoplanet_data = fetch_exoplanet_data()
    planet_name, story = generate_story(exoplanet_data)
    story_text.delete("1.0", tk.END)  # Clear any existing text
    story_text.insert(tk.END, f"Exoplanet {planet_name}:\n\n{story}")
    
root = tk.Tk()
root.title("Exoplanet Generator")

root.resizable(False, False)

style = Style(theme="cyborg")

planet_image = Image.open("resources\\fractal_abstract.jpg")  
planet_image = planet_image.resize((860, 607))  
planet_photo = ImageTk.PhotoImage(planet_image)

image_label = tk.Label(root, image=planet_photo, bg="black")
image_label.pack()

# Create a text widget to display the story
story_text = tk.Text(root, wrap=tk.WORD, height=15, width=70)
story_text.pack()

# Create empty space 
empty_space_label = tk.Label(root, text="", height=1)
empty_space_label.pack()

generate_button = tk.Button(root, text="Generate Exoplanet", padx=15, pady=5, command=generate_button_clicked, width=25, height=3)
generate_button.pack()

empty_space_label = tk.Label(root, text="", height=1)
empty_space_label.pack()

root.mainloop()


