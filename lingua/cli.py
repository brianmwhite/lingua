from datetime import datetime

import cloup
from cloup import option, option_group
from cloup.constraints import RequireExactly
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.style import Style

import lingua.cli_output as create
from lingua.spanish_translations import SpanishTranslation


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
        is_flag=False,
        flag_value=datetime.today().strftime("%m/%d/%y")
    ),
    constraint=RequireExactly(1),
)
@option("--nocolor", default=False, is_flag=True,
        help="turn off colorized output")
@option("--outputpanel", default=False, is_flag=True,
        help="surround the output in a panel to separate it from the rest of the console")
def run(**kwargs):
    console = Console()
    output = ""

    if kwargs.get("nocolor"):
        console.no_color = True

    if kwargs.get("number"):
        output = create.number_output(kwargs.get("number"))
    elif kwargs.get("date"):
        output = create.date_output(kwargs.get("date"))
    elif kwargs.get("temp"):
        output = create.temperature_output(kwargs.get("temp"))
    elif kwargs.get("distance"):
        output = create.distance_output(kwargs.get("distance"))
    elif kwargs.get("weight"):
        output = create.weight_output(kwargs.get("weight"))
    elif kwargs.get("length"):
        output = create.length_output(kwargs.get("length"))
    elif kwargs.get("mmi"):
        output = create.mmi_output(kwargs.get("mmi"))
    elif kwargs.get("imm"):
        output = create.imm_output(kwargs.get("imm"))

    if kwargs.get("outputpanel"):
        console.print(
            Panel(
                output.strip(), box=box.SIMPLE_HEAD,
                border_style=Style(color="grey39"),
                highlight=True
            ))
    else:
        console.print(output.strip())


if __file__ == "__main__" or __name__ == "__main__":
    run()
