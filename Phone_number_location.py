import phonenumbers

from test import number

from phonenumbers import geocoder

countryname = phonenumbers.parse(number, "ch")

print(geocoder.description_for_number(countryname, "en"))

from phonenumbers import carrier


sim_company = phonenumbers.parse(number , "co")
print(carrier.name_for_number(sim_company , "en"))

