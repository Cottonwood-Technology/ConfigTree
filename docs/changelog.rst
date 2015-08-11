Changes
=======

0.5
---

Work in progress


0.4
---

*   Dropped Python 2.6 support.
*   Completely reworked loading process (see :ref:`migration03to04`):

    *   functions :func:`configtree.loader.load`, :func:`configtree.loader.loaderconf` are deprecated in favor of :class:`configtree.loader.Loader`;
    *   function :func:`configtree.loader.make_walk` is deprecated in favor of :class:`configtree.loader.Walker`;
    *   function :func:`configtree.loader.make_update` is deprecated in favor of :class:`configtree.loader.Updater`;
    *   module :mod:`configtree.conv` and its plugins (from entry point with
        the same name) is deprecated in favor or :mod:`configtree.formatter`;
    *   shell command ``configtree`` is deprecated in favor of ``ctdump``.

0.3
---

*   Dropped Python 3.2 support due to ``coverage`` package.  The code should
    still work OK, but it will not be tested anymore.
*   Added :func:`configtree.loader.loaderconf` function to be able to read loader configuration
    from ``loaderconf.py`` module in a clean way.


0.2
---

*   Added ``copy`` method into :class:`configtree.tree.Tree` and :class:`configtree.tree.BranchProxy` classes.
*   Added human readable representation of :class:`configtree.tree.BranchProxy` class.
*   Added rare iterators into :class:`configtree.tree.Tree` and :class:`configtree.tree.BranchProxy` classes.
*   Added :func:`configtree.tree.rarefy` function.
*   Added rare JSON converter.


0.1
---

*   Initial release.