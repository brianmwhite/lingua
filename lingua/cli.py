from datetime import datetime

import cloup
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.style import Style

import lingua.cli_output as create
from lingua.spanish_translations import SpanishTranslation

settings = {"ignore_unknown_options": True}


@cloup.group()
@cloup.option("--colorized/--nocolor", default=True)
@cloup.option("--outputpanel/--nopanel", default=False)
@cloup.pass_context
def translations(ctx, colorized, outputpanel):
    ctx.ensure_object(dict)
    ctx.obj["ignore_unknown_options"] = True
    ctx.obj["colorized"] = colorized
    ctx.obj["outputpanel"] = outputpanel


@translations.command(
    context_settings=settings, help="a numerical string to translate to spanish"
)
@cloup.argument("numeric_input")
@cloup.pass_context
def number(ctx, **kwargs):
    output(ctx, create.number_output(kwargs["numeric_input"]))


@translations.command(
    context_settings=settings, help="temperature to convert between °C and °F"
)
@cloup.argument("numeric_input")
@cloup.pass_context
def temp(ctx, **kwargs):
    output(ctx, create.temperature_output(kwargs["numeric_input"]))


@translations.command(
    context_settings=settings, help="distance to convert between km and miles"
)
@cloup.argument("numeric_input")
@cloup.pass_context
def distance(ctx, **kwargs):
    output(ctx, create.distance_output(kwargs["numeric_input"]))


@translations.command(
    context_settings=settings,
    help="length to convert between feet/inches and meters/cm",
)
@cloup.argument("numeric_input")
@cloup.pass_context
def length(ctx, **kwargs):
    output(ctx, create.length_output(kwargs["numeric_input"]))


@translations.command(
    context_settings=settings, help="weight to convert between kg and lbs"
)
@cloup.argument("numeric_input")
@cloup.pass_context
def weight(ctx, **kwargs):
    output(ctx, create.weight_output(kwargs["numeric_input"]))


@translations.command(
    context_settings=settings, help="length to convert from mm to inches"
)
@cloup.argument("numeric_input")
@cloup.pass_context
def mmi(ctx, **kwargs):
    output(ctx, create.mmi_output(kwargs["numeric_input"]))


@translations.command(
    context_settings=settings, help="length to convert from inches to mm"
)
@cloup.argument("numeric_input")
@cloup.pass_context
def imm(ctx, **kwargs):
    output(ctx, create.imm_output(kwargs["numeric_input"]))


@translations.command(
    context_settings=settings,
    help="The date string to convert (in format "
    f'{", ".join(SpanishTranslation.DATE_FORMATS)})',
)
@cloup.argument("date_input", default=datetime.today().strftime("%m/%d/%y"))
@cloup.pass_context
def date(ctx, **kwargs):
    output(ctx, create.date_output(kwargs["date_input"]))


@translations.command(
    context_settings=settings, help="US timezone to show UTC offset (ET,CT,MT,PT)"
)
@cloup.argument("input", default="ET")
@cloup.pass_context
def tz(ctx, **kwargs):
    output(ctx, create.timezone_output(kwargs["input"]))


@translations.command(
    context_settings=settings,
    help="date that the time changes to or from daylight savings in the US",
)
@cloup.pass_context
def dst(ctx, **kwargs):
    output(ctx, create.timezone_next_time_change_output("ET"))


@translations.command(
    context_settings=settings, help="Outputs the current UTC date/time with an offset."
)
@cloup.argument("numeric_input", default=0)
@cloup.pass_context
def utc(ctx, **kwargs):
    output(ctx, create.timezone_utc_output(kwargs["numeric_input"]))


def output(ctx, output_string: str):
    console = Console()

    if not ctx.obj["colorized"]:
        console.no_color = True

    if ctx.obj["outputpanel"]:
        console.print(
            Panel(
                output_string.strip(),
                box=box.SIMPLE_HEAD,
                border_style=Style(color="grey39"),
                highlight=True,
            )
        )
    else:
        console.print(output_string.strip())


if __file__ == "__main__" or __name__ == "__main__":
    translations()
