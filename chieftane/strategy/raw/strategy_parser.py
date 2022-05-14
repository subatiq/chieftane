from pathlib import Path
from typing import Any

import yaml
from loguru import logger

from chieftane.strategy.models import Strategy
from chieftane.strategy.raw.models import RawStrategy


def parse_strategy_object(strategy: list[dict[str, Any]]) -> Strategy:
    raw = RawStrategy.parse_obj(strategy)

    return raw.to_strategy()


def parse_strategy_file(file_path: Path) -> Strategy:
    logger.info(f"Parsing strategy file {file_path}")
    configs = yaml.safe_load(file_path.read_text())

    return parse_strategy_object(configs)
