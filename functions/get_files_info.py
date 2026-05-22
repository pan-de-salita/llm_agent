#!/usr/bin/env python3

import os

from functions.get_verified_target_dir import get_verified_target_dir


def get_files_info(working_directory: str, directory: str = ".") -> str:
    print(f"Result for {directory if directory != "." else "current"} directory:")
    try:
        return _format_files_info(get_verified_target_dir(working_directory, directory))
    except Exception as e:
        return f"    Error: {e}"


def _format_files_info(target_dir) -> str:
    contents = os.listdir(target_dir)
    return "\n".join([_format_file_metadata(c, target_dir) for c in contents])


def _format_file_metadata(file, target_dir):
    file_size = _format_file_size(file, target_dir)
    is_dir = _format_is_dir(file, target_dir)
    file_metadata = f"  - {file}: file_size={file_size}, is_dir={is_dir}"
    if is_dir:
        return f"{file_metadata}\n" + _format_files_info(os.path.join(target_dir, file))
    return file_metadata


def _format_file_size(file, target_dir) -> int:
    return os.stat(os.path.join(target_dir, file)).st_size


def _format_is_dir(file, target_dir) -> bool:
    return os.path.isdir(os.path.join(target_dir, file))
