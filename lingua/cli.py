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
        flag_value=datetime.today().strftime("%m/%d/%y"),
    ),
    option("--tz", help="US timezone to show UTC offset (ET,CT,MT,PT)"),
    option(
        "--dst",
        help="date that the time changes to or from daylight savings in the US",
        is_flag=True,
    ),
    option(
        "--utc",
        help="Outputs the current UTC date/time with an offset.",
        type=float,
    ),
    constraint=RequireExactly(1),
)
@option("--nocolor", default=False, is_flag=True, help="turn off colorized output")
@option(
    "--outputpanel",
    default=False,
    is_flag=True,
    help="surround the output in a panel to separate it from the rest of the console",
)
def run(**kwargs):
    console = Console()
    output = ""

    if kwargs.get("nocolor"):
        console.no_color = True

    if "number" in kwargs and kwargs["number"] is not None:
        output = create.number_output(kwargs["number"])
    elif "date" in kwargs and kwargs["date"] is not None:
        output = create.date_output(kwargs["date"])
    elif "temp" in kwargs and kwargs["temp"] is not None:
        output = create.temperature_output(kwargs["temp"])
    elif "distance" in kwargs and kwargs["distance"] is not None:
        output = create.distance_output(kwargs["distance"])
    elif "weight" in kwargs and kwargs["weight"] is not None:
        output = create.weight_output(kwargs["weight"])
    elif "length" in kwargs and kwargs["length"] is not None:
        output = create.length_output(kwargs["length"])
    elif "mmi" in kwargs and kwargs["mmi"] is not None:
        output = create.mmi_output(kwargs["mmi"])
    elif "imm" in kwargs and kwargs["imm"] is not None:
        output = create.imm_output(kwargs["imm"])
    elif "tz" in kwargs and kwargs["tz"] is not None:
        output = create.timezone_output(kwargs["tz"])
    elif "dst" in kwargs and kwargs["dst"]:
        output = create.timezone_next_time_change_output("ET")
    elif "utc" in kwargs and kwargs["utc"]:
        output = create.timezone_utc_output(kwargs["utc"])

    if kwargs.get("outputpanel"):
        console.print(
            Panel(
                output.strip(),
                box=box.SIMPLE_HEAD,
                border_style=Style(color="grey39"),
                highlight=True,
            )
        )
    else:
        console.print(output.strip())


if __file__ == "__main__" or __name__ == "__main__":
    run()
