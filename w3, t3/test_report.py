from pathlib import Path
from report import main
CSV_FILE = Path(__file__).parent / "tickets.csv"

def test_main_invalid_file(tmp_path, capsys):
    csv_file = tmp_path / "invalid.csv"
    csv_file.write_text(
        "id,category,priority,minutes\n"
        "101,network,45\n"
        "\n"
    )
    assert main(csv_file) == 1
    captured = capsys.readouterr()
    assert "There's a problem with file: " in captured.out

def test_main_missing_file(capsys, tmp_path):
    assert main(tmp_path / "missing.csv") == 1
    captured = capsys.readouterr()
    assert "Could not find the file" in captured.out

def test_main_working_file():
    assert main(CSV_FILE) == 0