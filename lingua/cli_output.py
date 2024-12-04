from lingua.spanish_translations import SpanishTranslation
from lingua.unit_conversion import UnitConversion
from lingua.timezone_helper import TimezoneHelper
import humanfriendly


def format_number(number: float):
    return humanfriendly.format_number(number)


def timezone_output(input_string: str):
    tz = TimezoneHelper()
    tz_full_name = tz.get_timezone_full_name(input_string)
    tz.set_timezone(tz_full_name)
    return tz.get_timezone_info()


def timezone_utc_output(offset: float):
    tz = TimezoneHelper()
    # sp = SpanishTranslation()
    # offset = sp.string_to_float(input_string)
    return tz.get_current_utc_time(offset).strftime("%Y-%m-%d %H:%M:%S")


def timezone_next_time_change_output(input_string: str):
    tz = TimezoneHelper()
    tz_full_name = tz.get_timezone_full_name(input_string)
    tz.set_timezone(tz_full_name)
    change_date = tz.get_next_timechange_date()
    date_string = change_date.strftime("%B %-d, %Y")  # Format as "Month Day, Year"
    return date_string


def number_output(input_string: str):
    sp = SpanishTranslation()
    number = sp.string_to_float(input_string)
    translation = sp.translate_number(number)
    return f"{format_number(number)} [[yellow]{translation[0]}[/yellow]]"


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
  = {format_number(c)}°C [[green]{c_translated} grados[/green]]

{input_temp_string}°C [[yellow]{input_temp_translated} grados[/yellow]]
  = {format_number(f)}°F [[green]{f_translated} grados[/green]]

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
  = {format_number(km)} km [[green]{km_translated} kilómetros[/green]]

{input_string} km [[yellow]{input_number_translated} km[/yellow]]
  = {format_number(m)} miles [[green]{m_translated} millas[/green]]

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
  = {format_number(kg)} kg [[green]{kg_translated} kilogramos[/green]]

{input_string} kg [[yellow]{input_number_translated} kilogramos[/yellow]]
  = {format_number(lbs)} lbs [[green]{lbs_translated} libras[/green]]

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

{input_string} inches = {format_number(cm)} cm or {format_number(cm*10)} mm
{input_string} mm = {format_number(inch/10)} inches or {format_number(inch/10/12)} feet
{input_string} cm = {format_number(inch)} inches or {format_number(inch/12)} feet
{input_string} ft = {format_number(m)} meters or {format_number(m*100)} cm
{input_string} meters = {format_number(ft)} feet or {format_number(ft*12)} inches

        """
    return output


def mmi_output(input_string: str):
    uc = UnitConversion()
    number = uc.string_to_float(input_string)
    inch = uc.cm_to_inches(number)
    output = f"""

{input_string} mm = {format_number(inch/10)} inches or {format_number(inch/10/12)} feet

         """
    return output


def imm_output(input_string: str):
    uc = UnitConversion()
    number = uc.string_to_float(input_string)

    cm = uc.inches_to_cm(number)

    output = f"""

{input_string} inches = {format_number(cm*10)} mm or {format_number(cm)} cm

        """
    return output
