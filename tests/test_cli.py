from click.testing import CliRunner
import lingua.cli


def test_cli_number():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--number", "100"])
    assert result.exit_code == 0
    assert result.output == "cien\n"


def test_cli_weight():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--weight", "165"])
    assert result.exit_code == 0
    assert result.output == (
        "165 lbs > 74.8 kg (setenta y cuatro punto ocho kilogramos)\n"
        "165 kg > 363.8 lbs (trescientos sesenta y tres punto ocho libras)\n"
    )


def test_cli_date_without_year():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--date", "5/3"])
    assert result.exit_code == 0
    assert result.output == "el tres de mayo\n"


def test_cli_date_with_year():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--date", "5/3/2023"])
    assert result.exit_code == 0
    assert result.output == "el tres de mayo de dos mil veintitrés\n"


def test_cli_temperature():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--temp", "65"])
    assert result.exit_code == 0
    assert result.output == (
        "65°F > 18°C (dieciocho grados)\n"
        "65°C > 149°F (ciento cuarenta y nueve grados)\n"
    )


def test_cli_distance():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--distance", "5"])
    assert result.exit_code == 0
    assert result.output == (
        "5 miles > 8 km (ocho kilómetros)\n"
        "5 km > 3.1 miles (tres punto uno millas)\n"
    )


def test_cli_length():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--length", "13"])
    assert result.exit_code == 0
    assert result.output == (
        "13 inches > 33.02 cm or 3302 mm\n"
        "13 cm > 5.11811 inches or 0.426509 feet\n"
        "13 ft > 3.9624 meters or 396.24 cm\n"
        "13 meters > 42.6509 feet or 511.811 inches\n"
    )
