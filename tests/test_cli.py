from click.testing import CliRunner
import lingua.cli


def test_cli_number():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--number", "100"])
    assert result.exit_code == 0


def test_cli_weight():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--weight", "165"])
    assert result.exit_code == 0


def test_cli_date_without_year():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--date", "5/3"])
    assert result.exit_code == 0


def test_cli_date_with_year():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--date", "5/3/2023"])
    assert result.exit_code == 0


def test_cli_temperature():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--temp", "65"])
    assert result.exit_code == 0


def test_cli_distance():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--distance", "5"])
    assert result.exit_code == 0


def test_cli_length():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--length", "13"])
    assert result.exit_code == 0
