#!/usr/bin/env python3

import os


def get_verified_target_path(
    working_dir: str, dir: str = ".", ftype: str = "dir"
) -> str:
    working_dir_abs = os.path.abspath(working_dir)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, dir))
    valid_target_dir = (
        os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    )

    if not valid_target_dir:
        raise Exception(
            f'Cannot list "{dir}" as it is outside the permitted working directory'
        )

    if not os.path.isdir(dir):
        raise Exception(f'"{dir}" is not a directory')

    return target_dir
