import pycountry

def get_country_id(phone_number):
  # Remove the plus sign if it exists
  if phone_number[0] == '+':
    phone_number = phone_number[1:]
  
  # Extract the first two digits of the phone number
  country_code = phone_number[:2]
  
  # Look up the country code in pycountry
  country = pycountry.countries.get(alpha_2=country_code)
  
  # Return the country name or ID
  if country:
    return country.name
  else:
    return "Country not found"

# Test the function
print(get_country_id("+1 555 555 5555"))  # Should print "United States"
print(get_country_id("+44 123 456 7890")) # Should print "United Kingdom"
print(get_country_id("+61 123 456 7890")) # Should print "Australia"
print(get_country_id("+99 123 456 7890")) # Should print "Country not found"
