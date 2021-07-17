import phonenumbers

number2=input("Enter your number with your country code --> ")
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number2,"CH")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number2,"RO")
provider = carrier.name_for_number(service_number,"en")
print(provider)
