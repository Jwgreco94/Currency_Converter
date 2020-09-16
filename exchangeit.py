"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Jonathan Greco
Date:   9/6/2020
"""

import currency

# Prompt user for src input.
src = input('3-letter code for original currency: ')

# Promt user for the dst input.
dst = input('3-letter code for the new currency: ')

# Prompt user for the amt input.
amt = input('Amount of the original currency: ')

# Convert amt to a float
amt = float(amt)

# Call the exchange function to get the results.
results = currency.exchange(src, dst, amt)

# Display the results to the user.
print('You can exchange '+ str(amt) + ' ' + src + ' for '+ str(round(results,3)) + ' ' + dst + '.')