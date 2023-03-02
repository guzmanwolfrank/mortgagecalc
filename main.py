import tkinter as tk
from tkinter import font

# Create a new window
root = tk.Tk()

# Set the title and background color
root.title("Wolfrank's Mortgage Calculator")
root.configure(bg="black")

# Set the font style
helvetica = font.Font(family="Helvetica", size=12)

# Create the header label
header_label = tk.Label(root, text="Wolfrank's Mortgage Calculator", font=helvetica, fg="white", bg="black")
header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Create the mortgage amount label and entry box
mortgage_amount_label = tk.Label(root, text="Mortgage Amount:", font=helvetica, fg="white", bg="black")
mortgage_amount_label.grid(row=1, column=0, padx=5, pady=5)
mortgage_amount_entry = tk.Entry(root, font=helvetica, bg="black", fg="white")
mortgage_amount_entry.grid(row=1, column=1, padx=5, pady=5)

# Create the interest rate label and entry box
interest_rate_label = tk.Label(root, text="Interest Rate (%):", font=helvetica, fg="white", bg="black")
interest_rate_label.grid(row=2, column=0, padx=5, pady=5)
interest_rate_entry = tk.Entry(root, font=helvetica, bg="black", fg="white")
interest_rate_entry.grid(row=2, column=1, padx=5, pady=5)

# Create the loan term label and entry box
loan_term_label = tk.Label(root, text="Loan Term (years):", font=helvetica, fg="white", bg="black")
loan_term_label.grid(row=3, column=0, padx=5, pady=5)
loan_term_entry = tk.Entry(root, font=helvetica, bg="black", fg="white")
loan_term_entry.grid(row=3, column=1, padx=5, pady=5)

# Create the calculate button
def calculate():
    # Get the user inputs
    mortgage_amount = float(mortgage_amount_entry.get())
    interest_rate = float(interest_rate_entry.get()) / 100 / 12
    loan_term = float(loan_term_entry.get()) * 12

    # Calculate the monthly payment
    monthly_payment = (mortgage_amount * interest_rate * (1 + interest_rate) ** loan_term) / ((1 + interest_rate) ** loan_term - 1)

    # Display the result
    result_label.config(text="Monthly Payment: $%.2f" % monthly_payment)

calculate_button = tk.Button(root, text="Calculate", font=helvetica, command=calculate, bg="white", fg="black")
calculate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Create the result label
result_label = tk.Label(root, font=helvetica, fg="white", bg="black")
result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Run the window
root.mainloop()
