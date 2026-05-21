#!/usr/bin/env python3

import functools
import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    print(f"Result for {directory if directory != "." else "current"} directory:")
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )

        if not valid_target_dir:
            raise Exception(
                f'Cannot list "{directory}" as it is outside the permitted working directory'
            )

        if not os.path.isdir(directory):
            raise Exception(f'"{directory}" is not a directory')

        return _format_files_info(target_dir)
    except Exception as e:
        return f"    Error: {e}"


def _format_files_info(target_dir):
    contents = os.listdir(target_dir)
    return "\n".join([_format_file_metadata(c, target_dir) for c in contents])


def _format_file_metadata(file, target_dir):
    file_size = _format_file_size(file, target_dir)
    is_dir = _format_is_dir(file, target_dir)
    file_metadata = f"  - {file}: file_size={file_size}, is_dir={is_dir}"
    if is_dir:
        return f"{file_metadata}\n" + _format_files_info(os.path.join(target_dir, file))
    return file_metadata


def _format_file_size(file, target_dir):
    return os.stat(os.path.join(target_dir, file)).st_size


def _format_is_dir(file, target_dir):
    return os.path.isdir(os.path.join(target_dir, file))
