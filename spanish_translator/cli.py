import cloup
from cloup import option_group, option
from cloup.constraints import RequireExactly
from .spanish_translation import SpanishTranslation


@cloup.command()
@option_group(
    "translation options",
    option("--number", help="a numerical string to translate to spanish"),
    option(
        "--date",
        help="The date string to convert (in format "
        f'{", ".join(SpanishTranslation.DATE_FORMATS)})',
    ),
    constraint=RequireExactly(1),
)
def run(**kwargs):
    if kwargs.get("number"):
        sp = SpanishTranslation()
        print(sp.translate_number(kwargs.get("number"))[0])
    elif kwargs.get("date"):
        sp = SpanishTranslation()
        print(sp.translate_date(kwargs.get("date")))


if __file__ == "__main__":
    run()
