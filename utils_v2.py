"""
Improved utility functions with proper error handling and Pythonic style.
"""
import os
import json
from pathlib import Path
from statistics import mean


def read_file(path: str) -> str:
    """Read file contents safely."""
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except PermissionError:
        raise PermissionError(f"Cannot read file: {path}")


def write_file(path: str, data: str) -> None:
    """Write data to file safely."""
    filepath = Path(path)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(data, encoding="utf-8")


def get_env(key: str, default: str = "") -> str:
    """Get environment variable with optional default."""
    return os.environ.get(key, default)


def parse_json(text: str) -> dict:
    """Parse JSON with proper error handling."""
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")


def validate_email(email: str) -> bool:
    """Basic email validation."""
    if not email or not isinstance(email, str):
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    return bool(local) and "." in domain and len(domain) > 2


def calculate_stats(numbers: list[float]) -> dict:
    """Calculate basic statistics for a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate stats for empty list")
    return {
        "average": mean(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "count": len(numbers),
    }
