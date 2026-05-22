#!/usr/bin/env python3

import os

from functions.get_verified_target_path import get_verified_target_path


def get_file_content(working_directory: str, file_path: str) -> str:
    target_file_path = get_verified_target_path(working_directory, file_path)


if __name__ == "__main__":
    get_file_content("calculator", "test")
