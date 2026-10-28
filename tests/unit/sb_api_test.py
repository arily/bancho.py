from __future__ import annotations

from pathlib import Path

import pytest

from app.sb import sb_api


def test_replay_available_checks_the_replay_directory(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(sb_api, "REPLAYS_PATH", tmp_path)

    assert sb_api.replay_available(42) is False

    (tmp_path / "42.osr").write_bytes(b"replay")

    assert sb_api.replay_available(42) is True
    assert sb_api.replay_available(43) is False
