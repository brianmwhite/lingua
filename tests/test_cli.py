from click.testing import CliRunner
import lingua.cli


def test_dst():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--dst"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_tz():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--tz", "et"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_utc_zero():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--utc", "0"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_utc_negative():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--utc", "-5"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_utc_positive():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--utc", "5"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_number():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--number", "100"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_number_with_outputpanel_option():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--number", "100", "--outputpanel"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_weight():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--weight", "165"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_weight_with_nocolor_option():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--weight", "165", "--nocolor"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_date_without_year():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--date", "5/3"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_date_with_year():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--date", "5/3/2023"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_date_today():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--date"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_temperature():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--temp", "65"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_distance():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--distance", "5"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_length():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--length", "13"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_imm():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--imm", "13"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0


def test_cli_mmi():
    runner = CliRunner()
    result = runner.invoke(lingua.cli.run, ["--mmi", "13"])
    assert result.output is not None and result.output.strip() != ""
    assert result.exit_code == 0
