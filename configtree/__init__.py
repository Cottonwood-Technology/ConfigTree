import logging

from .tree import ITree, Tree, flatten, rarefy
from .loader import Loader, Walker, Updater, PostProcessor, Pipeline


__all__ = [
    "ITree",
    "Tree",
    "flatten",
    "rarefy",
    "Loader",
    "Walker",
    "Updater",
    "PostProcessor",
    "Pipeline",
]
__version__ = "0.5.3"
__author__ = "Dmitry Vakhrushev <self@kr41.net>"
__license__ = "BSD"


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
