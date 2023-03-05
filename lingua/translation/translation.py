import locale
from datetime import datetime

from deep_translator import GoogleTranslator
from num2words import num2words


class SpanishTranslation:
    DATE_FORMATS = ["%Y-%m-%d", "%m/%d/%Y", "%m/%d/%y", "%m/%d"]

    SPANISH_MONTHS = [
        "enero",
        "febrero",
        "marzo",
        "abril",
        "mayo",
        "junio",
        "julio",
        "agosto",
        "septiembre",
        "octubre",
        "noviembre",
        "diciembre",
    ]
    SPANISH_NUMERIC_DAYS = [
        "primero",
        "dos",
        "tres",
        "cuatro",
        "cinco",
        "seis",
        "siete",
        "ocho",
        "nueve",
        "diez",
        "once",
        "doce",
        "trece",
        "catorce",
        "quince",
        "dieciséis",
        "diecisiete",
        "dieciocho",
        "diecinueve",
        "veinte",
        "veintiuno",
        "veintidós",
        "veintitrés",
        "veinticuatro",
        "veinticinco",
        "veintiséis",
        "veintisiete",
        "veintiocho",
        "veintinueve",
        "treinta",
        "treinta y uno",
    ]
    SPANISH_WEEKDAYS = [
        "lunes",
        "martes",
        "miércoles",
        "jueves",
        "viernes",
        "sábado",
        "domingo",
    ]

    # Define possible date formats with and without year
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

    def translate_date(self, input_string: str):
        is_year_included_in_input = False

        # Try to convert the date string to a date object using each possible format
        for format in self.DATE_FORMATS:
            try:
                date_obj = datetime.strptime(input_string, format).date()
                # check if the input string matches a format with a year
                if "%y" in format.lower():
                    is_year_included_in_input = True
                break
            except ValueError:
                pass
        else:
            # If none of the formats work, raise an error
            raise ValueError(
                f"Date string {input_string} does not match any supported formats"
            )

        # Print the date object
        # print(date_obj)

        translated_date_as_text_in_spanish = (
            f"el {self.SPANISH_NUMERIC_DAYS[date_obj.day-1]}"
            f" de {self.SPANISH_MONTHS[date_obj.month-1]}"
        )

        if is_year_included_in_input:
            try:
                year_spelled_out = num2words(date_obj.year)
                translated_year = GoogleTranslator(source="en", target="es").translate(
                    year_spelled_out
                )
                translated_date_as_text_in_spanish += f" de {translated_year}"
            except (
                TimeoutError,
                ConnectionError,
                GoogleTranslator.RequestError,
                GoogleTranslator.TooManyRequests,
                GoogleTranslator.TranslationNotFound,
            ):
                translated_date_as_text_in_spanish += " [year not translated]"
                pass

        return translated_date_as_text_in_spanish

    def translate_number(self, number_as_string: str):
        number = locale.atof(number_as_string)

        original_number_as_text_in_english = num2words(number)

        translated_number_in_spanish = GoogleTranslator(
            source="en", target="es"
        ).translate(original_number_as_text_in_english)

        # print(f"{number_as_string} -> {text}")
        # print(f"{translated}")
        return (translated_number_in_spanish, original_number_as_text_in_english)

    def string_to_float(self, input_string: str):
        return locale.atof(input_string)
