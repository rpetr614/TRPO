import subprocess
import sys
from pathlib import Path

from feature_a import feature_a
from feature_b import feature_b

ROOT = Path(__file__).resolve().parent.parent


def test_feature_a_runs_without_error():
    assert feature_a() is None


def test_feature_b_runs_without_error():
    assert feature_b() is None


def test_file1_script_runs_without_error():
    result = subprocess.run(
        [sys.executable, str(ROOT / "file1.py")],
        capture_output=True, text=True
    )
    assert result.returncode == 0
    assert "Hello from file1" in result.stdout
