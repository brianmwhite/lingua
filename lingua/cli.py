import cloup
from cloup import option, option_group
from cloup.constraints import RequireExactly
from lingua.spanish_translations import SpanishTranslation
from lingua.unit_conversion import UnitConversion


@cloup.command()
@option_group(
    "translation types",
    option("--number", help="a numerical string to translate to spanish"),
    option("--temp", help="temperature to convert between °C and °F"),
    option("--distance", help="distance to convert between km and miles"),
    option("--length", help="length to convert between feet/inches and meters/cm"),
    option("--weight", help="weight to convert between kg and lbs"),
    option("--mmi", help="length to convert from mm to inches"),
    option("--imm", help="length to convert from inches to mm"),
    option(
        "--date",
        help="The date string to convert (in format "
        f'{", ".join(SpanishTranslation.DATE_FORMATS)})',
    ),
    constraint=RequireExactly(1),
)
@option("--googletrans", default=False, is_flag=True,
        help="an option to force use of google translate for all numbers")
def run(**kwargs):
    # print(kwargs)
    sp = SpanishTranslation(kwargs.get("googletrans"))
    uc = UnitConversion()

    if kwargs.get("number"):

        input_string = kwargs.get("number")
        number = sp.string_to_float(input_string)

        translation = sp.translate_number(number)

        print(translation[0])
    elif kwargs.get("date"):
        print(sp.translate_date(kwargs.get("date")))
    elif kwargs.get("temp"):
        input_temp_string = kwargs.get("temp")
        input_temp = uc.string_to_float(input_temp_string)

        c = round(uc.fahrenheit_to_celsius(input_temp))
        f = round(uc.celsius_to_fahrenheit(input_temp))

        c_translated = sp.translate_number(c)[0]
        f_translated = sp.translate_number(f)[0]

        print(
            f"{input_temp_string}°F > {c:g}°C ({c_translated} grados)\n"
            f"{input_temp_string}°C > {f:g}°F ({f_translated} grados)"
        )
    elif kwargs.get("distance"):
        input_string = kwargs.get("distance")
        number = uc.string_to_float(input_string)

        km = round(uc.miles_to_km(number), 1)
        m = round(uc.km_to_miles(number), 1)

        km_translated = sp.translate_number(km)[0]
        m_translated = sp.translate_number(m)[0]

        print(
            f"{input_string} miles > {km:g} km ({km_translated} kilómetros)\n"
            f"{input_string} km > {m:g} miles ({m_translated} millas)"
        )
    elif kwargs.get("weight"):
        input_string = kwargs.get("weight")
        number = uc.string_to_float(input_string)

        kg = round(uc.lb_to_kg(number), 1)
        lbs = round(uc.kg_to_lb(number), 1)

        kg_translated = sp.translate_number(kg)[0]
        lbs_translated = sp.translate_number(lbs)[0]

        print(
            f"{input_string} lbs > {kg:g} kg ({kg_translated} kilogramos)\n"
            f"{input_string} kg > {lbs:g} lbs ({lbs_translated} libras)"
        )
    elif kwargs.get("length"):
        input_string = kwargs.get("length")
        number = uc.string_to_float(input_string)

        m = uc.feet_to_meters(number)
        ft = uc.meters_to_feet(number)
        inch = uc.cm_to_inches(number)
        cm = uc.inches_to_cm(number)

        print(
            f"{input_string} inches > {cm:g} cm or {cm*10:g} mm\n"
            f"{input_string} mm > {inch/10:g} inches or {inch/10/12:g} feet\n"
            f"{input_string} cm > {inch:g} inches or {inch/12:g} feet\n"
            f"{input_string} ft > {m:g} meters or {m*100:g} cm\n"
            f"{input_string} meters > {ft:g} feet or {ft*12:g} inches"
        )
    elif kwargs.get("mmi"):
        input_string = kwargs.get("mmi")
        number = uc.string_to_float(input_string)

        inch = uc.cm_to_inches(number)

        print(
            f"{input_string} mm > {inch/10:g} inches or {inch/10/12:g} feet"
        )
    elif kwargs.get("imm"):
        input_string = kwargs.get("imm")
        number = uc.string_to_float(input_string)

        cm = uc.inches_to_cm(number)

        print(
            f"{input_string} inches > {cm*10:g} mm or {cm:g} cm"
        )


if __file__ == "__main__" or __name__ == "__main__":
    run()
