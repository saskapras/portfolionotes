# === Stage 50: Add unit tests for import and export behavior ===
# Project: PortfolioNotes
import json
from pathlib import Path
import pytest

from portfolio_notes.app import App

@pytest.fixture
def app():
    app = App()
    app.add_holding("AAPL", 10, 150.0, "Apple")
    app.add_note("AAPL", "Strong tech company")
    app.add_price_snapshot("AAPL", 155.0)
    app.add_reminder("AAPL", 152.0, "Check AAPL price")
    return app

def test_import_and_export(app, tmp_path):
    import io
    json_data = json.dumps(app.to_dict())
    out = io.StringIO(json_data)
    new_app = App()
    new_app.import_data(out)
    assert new_app.holdings == app.holdings
    assert new_app.notes == app.notes
    assert new_app.price_snapshots == app.price_snapshots
    assert new_app.reminders == app.reminders
    assert new_app.imported == True

def test_export_to_file(app, tmp_path):
    out_file = tmp_path / "export.json"
    app.export_to_file(str(out_file))
    assert out_file.exists()
    with open(out_file) as f:
        data = json.load(f)
    assert data["holdings"] == app.holdings
    assert data["notes"] == app.notes
    assert data["price_snapshots"] == app.price_snapshots
    assert data["reminders"] == app.reminders
    assert data["imported"] == True

def test_import_from_file(app, tmp_path):
    out_file = tmp_path / "import.json"
    app.export_to_file(str(out_file))
    new_app = App()
    new_app.import_data(str(out_file))
    assert new_app.holdings == app.holdings
    assert new_app.notes == app.notes
    assert new_app.price_snapshots == app.price_snapshots
    assert new_app.reminders == app.reminders
