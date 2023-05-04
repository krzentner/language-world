

After writing the program, press "Run" to check the answer, then press "Submit" to send your code to the server.
"""
[eod] [code]# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""Utilities for loading kernel images."""
import abc
import logging
import os
import sys
import typing

from framework import utils


class Kernel(object):
    """A Linux kernel."""

    def __init__(self, path: str, config: str) -> None:
        self._path = path
        self._config = config

    def path(self) -> str:
        """Return the path to the kernel."""
        return self._path

    def config(self) -> str:
        """Return the path to the kernel configuration."""
        return self._config

    @abc.abstractmethod
    def modules_path(self) -> str:
        """Return the path to the kernel modules."""
        ...

    @abc.abstractmethod
    def rootfs_path(self) -> typing.Optional[str]:
        """Return the path to the rootfs."""
        ...


class LocalKernel(Kernel):
    """A kernel stored in the file system."""

    def __init__(self, path: str, config: str, modules_path: str) -> None:
        super().__init__(path, config)
        self._modules_path = modules_path

    def modules_path(self) -> str:
        """Return the path to the kernel modules."""
        return self._modules_path

    def rootfs_path(self) -> typing.Optional[str]:
        """Return the path to the rootfs."""
        return None


class ArtifactKernel(Kernel):
    """An artifact-based kernel from an artifact image."""

    def __init__(self, path: str, config: str) -> None:
        super().__init__(path, config)

    def modules_path(self) -> str:
        """Return the path to the kernel modules."""
        return self.path() + "/lib/modules"

    def rootfs_path(self) -> typing.Optional[str]:
        """Return the path to the rootfs."""
        return None


class BundleKernel(Kernel):
    """An artifact-based kernel from a bundle."""

    def __init__(self, path: str, config: str, rootfs_path: str) 