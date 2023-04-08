import tkinter as tk
import openai

# Вставьте свои значения OPENAI-API-KEY И YOUR-MODEL-NAME
openai.api_key = "OPEN-API-KEY"
model_name = "YOUR-MODEL-NAME"

# Определяем личность
persona ="Я - ресторанный критик в космосе. Я путешествую по галактикам, чтобы попробовать самые интересные и вкусные космические блюда. Моя миссия - помочь людям найти лучшие космические рестораны и насладиться великолепным гастрономическим опытом во время их космических путешествий."

def on_submit():
   # Get the prompt from the input field and add the persona
   prompt = f"Я - {persona}. {input_field.get()}"


   # Make the completion request
   completion = openai.Completion.create(model=model_name, prompt=prompt, max_tokens=500)


   # Clear the input field
   input_field.delete(0, "end")


   # Get the completion text from the first choice in the choices list
   text = completion.choices[0]["text"]


   # Display the completion in the result text area
   result_text.config(state="normal")
   result_text.delete("1.0", "end")
   result_text.insert("end", text)
   result_text.config(state="disabled")


# Create the main window
window = tk.Tk()
window.title("Fine-tuned @gptscience")
window.geometry("800x600")


# Create the input field and submit button
input_field = tk.Entry(window, width=120)
submit_button = tk.Button(window, text="Submit", command=on_submit)


# Create the result text area
result_text = tk.Text(window, state="normal", width=110, height=30)


# Add the input field, submit button, and result text area to the window
input_field.pack(pady=20)
submit_button.pack(pady=10)
result_text.pack()


# Run the main loop
window.mainloop()

# Сгенерировано с помощью @gptscience