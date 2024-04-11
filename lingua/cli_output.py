from lingua.spanish_translations import SpanishTranslation
from lingua.unit_conversion import UnitConversion


def number_output(input_string: str):
    sp = SpanishTranslation()
    number = sp.string_to_float(input_string)
    translation = sp.translate_number(number)
    return f"{number:g} [[yellow]{translation[0]}[/yellow]]"


def date_output(input_string: str):
    sp = SpanishTranslation()
    return f"{input_string} [[yellow]{sp.translate_date(input_string)}[/yellow]]"


def temperature_output(input_temp_string: str):
    sp = SpanishTranslation()
    uc = UnitConversion()

    input_temp = uc.string_to_float(input_temp_string)

    c = round(uc.fahrenheit_to_celsius(input_temp))
    f = round(uc.celsius_to_fahrenheit(input_temp))

    c_translated = sp.translate_number(c)[0]
    f_translated = sp.translate_number(f)[0]

    input_temp_translated = sp.translate_number(input_temp)[0]

    output = f"""

{input_temp_string}°F [[yellow]{input_temp_translated} grados[/yellow]]
  = {c:g}°C [[green]{c_translated} grados[/green]]

{input_temp_string}°C [[yellow]{input_temp_translated} grados[/yellow]]
  = {f:g}°F [[green]{f_translated} grados[/green]]

    """
    return output


def distance_output(input_string: str):
    sp = SpanishTranslation()
    uc = UnitConversion()

    number = uc.string_to_float(input_string)

    km = round(uc.miles_to_km(number), 1)
    m = round(uc.km_to_miles(number), 1)

    input_number_translated = sp.translate_number(number)[0]

    km_translated = sp.translate_number(km)[0]
    m_translated = sp.translate_number(m)[0]

    output = f"""

{input_string} miles [[yellow]{input_number_translated} millas[/yellow]]
  = {km:g} km [[green]{km_translated} kilómetros[/green]]

{input_string} km [[yellow]{input_number_translated} km[/yellow]]
  = {m:g} miles [[green]{m_translated} millas[/green]]

    """
    return output


def weight_output(input_string: str):
    sp = SpanishTranslation()
    uc = UnitConversion()

    number = uc.string_to_float(input_string)

    kg = round(uc.lb_to_kg(number), 1)
    lbs = round(uc.kg_to_lb(number), 1)

    kg_translated = sp.translate_number(kg)[0]
    lbs_translated = sp.translate_number(lbs)[0]

    input_number_translated = sp.translate_number(number)[0]

    output = f"""

{input_string} lbs [[yellow]{input_number_translated} libras[/yellow]]
  = {kg:g} kg [[green]{kg_translated} kilogramos[/green]]

{input_string} kg [[yellow]{input_number_translated} kilogramos[/yellow]]
  = {lbs:g} lbs [[green]{lbs_translated} libras[/green]]

      """
    return output


def length_output(input_string: str):
    uc = UnitConversion()

    number = uc.string_to_float(input_string)

    m = uc.feet_to_meters(number)
    ft = uc.meters_to_feet(number)
    inch = uc.cm_to_inches(number)
    cm = uc.inches_to_cm(number)

    output = f"""

{input_string} inches = {cm:g} cm or {cm*10:g} mm
{input_string} mm = {inch/10:g} inches or {inch/10/12:g} feet
{input_string} cm = {inch:g} inches or {inch/12:g} feet
{input_string} ft = {m:g} meters or {m*100:g} cm
{input_string} meters = {ft:g} feet or {ft*12:g} inches

        """
    return output


def mmi_output(input_string: str):
    uc = UnitConversion()
    number = uc.string_to_float(input_string)
    inch = uc.cm_to_inches(number)
    output = f"""

{input_string} mm = {inch/10:g} inches or {inch/10/12:g} feet

         """
    return output


def imm_output(input_string: str):
    uc = UnitConversion()
    number = uc.string_to_float(input_string)

    cm = uc.inches_to_cm(number)

    output = f"""

{input_string} inches = {cm*10:g} mm or {cm:g} cm

        """
    return output
