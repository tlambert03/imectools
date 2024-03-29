"""Tools for the core formerly known as the Nikon Imaging Center at HMS."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("imectools")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Talley Lambert"
__email__ = "talley.lambert@example.com"

from ._cleanup import iter_empty_dirs, iter_old_files

__all__ = ["iter_empty_dirs", "iter_old_files", "__version__"]
