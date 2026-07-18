from __future__ import annotations

import argparse
from pathlib import Path

import yaml


def main() -> None:
    parser = argparse.ArgumentParser(prog="agent-tester")
    subparsers = parser.add_subparsers(dest="command", required=True)
    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("suite", type=Path)
    args = parser.parse_args()

    suite = yaml.safe_load(args.suite.read_text())
    print(f"Loaded {len(suite.get('scenarios', []))} scenarios from {args.suite}")
