import locale
from datetime import datetime

from num2words import num2words
import math


class SpanishTranslation:

    DATE_FORMATS = ["%Y-%m-%d", "%m/%d/%Y", "%m/%d/%y", "%m/%d",
                    "%m-%d-%Y", "%m-%d-%y", "%m-%d", "%d/%m/%Y"]

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
            # If none of the formats work, show an error
            return f"Date string {input_string} does not match any supported formats"

        # Print the date object
        # print(date_obj)

        translated_date_as_text_in_spanish = (
            f"el {self.SPANISH_NUMERIC_DAYS[date_obj.day-1]}"
            f" de {self.SPANISH_MONTHS[date_obj.month-1]}"
        )

        if is_year_included_in_input:
            try:
                translated_year = self.int_to_spanish(date_obj.year)
                translated_date_as_text_in_spanish = (
                    f"{self.SPANISH_WEEKDAYS[date_obj.weekday()]}, "
                    f"{translated_date_as_text_in_spanish}"
                    f" de {translated_year}"
                )
            except (
                TimeoutError,
                ConnectionError,
            ):
                translated_date_as_text_in_spanish += " [year not translated]"
                pass

        return translated_date_as_text_in_spanish

    def translate_number(self, number: float):
        original_number_as_text_in_english = num2words(number)

        # between 0 and less than a billion
        if number >= -1000000000000 and number <= 1000000000000:
            translated_number_in_spanish = self.float_to_spanish(number)
        else:
            translated_number_in_spanish = "[!]"

        return (translated_number_in_spanish, original_number_as_text_in_english)

    def string_to_float(self, input_string: str):
        return locale.atof(input_string)

    def split_float(self, num):
        is_negative = num < 0
        num = abs(num)
        whole_num = math.floor(num)
        decimal_part = round((num - whole_num) * 100)
        if decimal_part >= 95:
            whole_num += 1
            decimal_part = 0
        else:
            decimal_part = round((decimal_part) / 10)
        if is_negative:
            whole_num = whole_num * -1
        return whole_num, decimal_part

    def check_for_zero_ending(self, number_to_check: int,
                              base_integer: int,
                              translated_base: str):
        remainder = number_to_check % base_integer
        if remainder == 0:
            return translated_base
        else:
            return f"{translated_base} {self.int_to_spanish(remainder)}"

    def float_to_spanish(self, input_number: float):
        integer_part, decimal_part = self.split_float(input_number)
        if (decimal_part == 0):
            return f"{self.int_to_spanish(integer_part)}"
        else:
            return (
                f"{self.int_to_spanish(integer_part)} "
                f"punto {self.int_to_spanish(decimal_part)}"
            )

    def int_to_spanish(self, input_number: int):
        if input_number < 0:
            return 'menos ' + self.int_to_spanish(abs(input_number))

        if input_number == 0:
            return 'cero'
        elif input_number == 1:
            return 'uno'
        elif input_number == 2:
            return 'dos'
        elif input_number == 3:
            return 'tres'
        elif input_number == 4:
            return 'cuatro'
        elif input_number == 5:
            return 'cinco'
        elif input_number == 6:
            return 'seis'
        elif input_number == 7:
            return 'siete'
        elif input_number == 8:
            return 'ocho'
        elif input_number == 9:
            return 'nueve'
        elif input_number == 10:
            return 'diez'
        elif input_number == 11:
            return 'once'
        elif input_number == 12:
            return 'doce'
        elif input_number == 13:
            return 'trece'
        elif input_number == 14:
            return 'catorce'
        elif input_number == 15:
            return 'quince'
        elif input_number == 16:
            return 'dieciséis'
        elif input_number < 20:
            return 'dieci' + self.int_to_spanish(input_number - 10)
        elif input_number == 20:
            return 'veinte'
        elif input_number == 21:
            return 'veintiún'
        elif input_number == 22:
            return "veintidós"
        elif input_number == 23:
            return "veintitrés"
        elif input_number == 26:
            return "veintiséis"
        elif input_number < 30:
            return 'veinti' + self.int_to_spanish(input_number - 20)
        elif input_number == 30:
            return 'treinta'
        elif input_number == 40:
            return 'cuarenta'
        elif input_number == 50:
            return 'cincuenta'
        elif input_number == 60:
            return 'sesenta'
        elif input_number == 70:
            return 'setenta'
        elif input_number == 80:
            return 'ochenta'
        elif input_number == 90:
            return 'noventa'
        elif input_number < 100:
            return (
                f"{self.int_to_spanish(input_number - input_number % 10)} "
                f"y {self.int_to_spanish(input_number % 10)}"
            )
        elif input_number == 100:
            return 'cien'
        elif input_number < 200:
            return 'ciento ' + self.int_to_spanish(input_number % 100)
        elif input_number <= 299:
            return self.check_for_zero_ending(input_number, 200, "doscientos")
        elif input_number <= 399:
            return self.check_for_zero_ending(input_number, 300, "trescientos")
        elif input_number <= 499:
            return self.check_for_zero_ending(input_number, 400, "cuatrocientos")
        elif input_number <= 599:
            return self.check_for_zero_ending(input_number, 500, "quinientos")
        elif input_number <= 699:
            return self.check_for_zero_ending(input_number, 600, "seiscientos")
        elif input_number <= 799:
            return self.check_for_zero_ending(input_number, 700, "setecientos")
        elif input_number <= 899:
            return self.check_for_zero_ending(input_number, 800, "ochocientos")
        elif input_number <= 999:
            return self.check_for_zero_ending(input_number, 900, "novecientos")
        elif input_number == 1000:
            return 'mil'
        elif input_number < 2000:
            return 'mil ' + self.int_to_spanish(input_number % 1000)
        elif input_number < 1000000:
            remainder = input_number % 1000
            if remainder == 0:
                return self.int_to_spanish(input_number // 1000) + ' mil'
            else:
                return (
                    f"{self.int_to_spanish(input_number // 1000)}"
                    f" mil {self.int_to_spanish(remainder)}"
                )
        elif input_number == 1000000:
            return 'un millón'
        elif input_number < 2000000:
            return 'un millón ' + self.int_to_spanish(input_number % 1000000)
        elif input_number < 1000000000000:
            remainder = input_number % 1000000
            if remainder == 0:
                return self.int_to_spanish(input_number // 1000000) + ' millones'
            else:
                return self.int_to_spanish(input_number // 1000000) + ' millones ' \
                    + self.int_to_spanish(remainder)
        elif input_number == 1000000000000:
            return "un billón"
