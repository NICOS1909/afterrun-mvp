from app import main as app_main


def test_main_prints(capsys):
    app_main.main()
    captured = capsys.readouterr()
    assert "afterrun-mvp app entry" in captured.out
