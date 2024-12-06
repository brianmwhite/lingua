from click.testing import CliRunner
import lingua.cli


def test_dst():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, "dst")
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_tz():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["tz", "et"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_utc_zero():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["utc", "0"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_utc_negative():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["utc", "-5"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_utc_positive():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["utc", "5"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_number():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["number", "100"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_number_with_outputpanel_option():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["--outputpanel", "number", "100"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_weight():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["weight", "165"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_weight_with_nocolor_option():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["--nocolor", "weight", "165"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_date_without_year():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["date", "5/3"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_date_with_year():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["date", "5/3/2023"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_date_today():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["date"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_temperature():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["temp", "65"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_distance():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["distance", "5"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_length():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["length", "13"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_imm():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["imm", "13"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_mmi():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.translations, ["mmi", "13"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0
