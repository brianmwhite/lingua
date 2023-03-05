import locale


class UnitConversion:
    # Define possible date formats with and without year
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

    def string_to_float(self, input_string: str):
        return locale.atof(input_string)

    # temp
    def fahrenheit_to_celsius(self, fahrenheit: float):
        celsius = (fahrenheit - 32) / 1.8
        return celsius

    def celsius_to_fahrenheit(self, celsius: float):
        fahrenheit = (celsius * 1.8) + 32
        return fahrenheit

    # weight
    def kg_to_lb(self, weight_in_kg: float):
        weight_in_lb = weight_in_kg * 2.20462
        return weight_in_lb

    def lb_to_kg(self, weight_in_lb: float):
        weight_in_kg = weight_in_lb / 2.20462
        return weight_in_kg

    # dist
    def km_to_miles(self, km: float):
        miles = km / 1.60934
        return miles

    def miles_to_km(self, miles: float):
        km = miles * 1.60934
        return km

    # length
    def feet_to_meters(self, length):
        return length * 0.3048

    def meters_to_feet(self, length):
        return length / 0.3048
    
    def inches_to_cm(self, length):
        return length * 2.54

    def cm_to_inches(self, length):
        return length / 2.54
