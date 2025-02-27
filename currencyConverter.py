import tkinter as tk
from tkinter import ttk
import requests
from config import EXCHANGE_RATE_API_KEY

def convert_currency():
    #placeholder function for currency conversion logic
    try:
        #getting each of the amounts using .get()
        amount = float(amount_entry.get())
        from_currency = from_currency_combo.get()
        to_currency = to_currency_combo.get()

        #if both of the currencies are not selected then it returns a text message error asking to select both currencies
        if not from_currency or not to_currency:
            result_label.config(text="Please select both currencies")
            return
        #the exchange rate api key variable is used in config.py which has the secret key
        api_key = EXCHANGE_RATE_API_KEY
        #using the from currency and api key on the url to fetch results
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}?apikey={api_key}"
        #using requests to actually access the API
        response = requests.get(url)
        #in case anything goes wrong
        response.raise_for_status

        data = response.json()
        #since there are so many different currencies, we have to land on the proper currency to get the conversion right for the to_currency
        rate = data['rates'][to_currency]


        if rate:
            #we are saying the converted amount is the amount which the user inputs multiplied by the rate which we are fetching from the list for the designated currency chosen
            converted_amount = amount * rate
            #result label shows the conversion values first is the currency it is being converted from and the second is the one it is being converted to
            result_label.config(text=f"{amount} {from_currency} is {converted_amount} {to_currency}")
        else:
            result_label.config(text="Conversion rate not found")    
        #print(data)
    #exception if any error occurs
    except requests.exceptions.RequestException as e:
        result_label.config(text="An error occurred while fetching the conversion rate")
        print(f"An error occurred: {e}")

#set up a tkinter window
window = tk.Tk()
window.title("Currency Converter")

#create a label for the amount input field
amount_label = tk.Label(window, text="Amount: ")
amount_label.pack(pady=5)

#create an entry field from the input amount
amount_entry = tk.Entry(window)
amount_entry.pack(pady=5)

#create a label for the from currency dropdown
from_currency_label = tk.Label(window, text="From Currency: ")
from_currency_label.pack(pady=5)

#create a comboBox for the from currency
from_currency_combo = ttk.Combobox(window, values=["USD","INR", "EUR", "GBP", "CAD", "AUD"])
from_currency_combo.pack(pady=5)

#create a label for the to currency dropdown
to_currency_label = tk.Label(window, text="To Currency: ")
to_currency_label.pack(pady=5)

#create a comboBox for the to currency
to_currency_combo = ttk.Combobox(window, values=["USD", "INR", "EUR", "GBP", "CAD", "AUD"])
to_currency_combo.pack(pady=5)

#convert button which calls the convert_currency function
convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

result_label = tk.Label(window, text="Enter an amount and select the currencies to convert")
result_label.pack(pady=10)

#this allows to check the progress of the code when a function has not been defined yet
window.mainloop()