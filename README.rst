****************
cookiecutter-kxg
****************
Cookiecutter template for games based on the KXG game engine.  See 
https://github.com/audreyr/cookiecutter.  The template includes:

* Free software: GPLv3 license
* Vanilla testing setup with `unittest` and `python setup.py test`
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 3.3, 3.4
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* Bumpversion: Pre-configured version bumping with a single command

Usage
=====
Run the following command to create a directory nicely setup to develop a new 
game using the KXG game engine::

    cookiecutter https://github.com/kxgames/cookiecutter-kxg.git

Then:

* Add the repo to your Travis CI account.
* Run the script `travis_pypi_setup.py` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
* Release your package the standard Python way. Here's a release checklist: 
  https://gist.github.com/audreyr/5990987
* (Optional) If you feel like pinning the requirements for your package, you can
  add a `requirements.txt` that specifies packages and version numbers.

Not Exactly What You Want?
==========================
If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.  It's up to you whether or not to rename your fork/own version. Do 
whatever you think sounds good.

We will also accept pull requests if they're small, atomic, and if they make 
our own development experiences better.

.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _`Nekroze/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
.. _`tony/cookiecutter-pypackage-pythonic`: https://github.com/tony/cookiecutter-pypackage-pythonic
.. _github comparison view: https://github.com/tony/cookiecutter-pypackage-pythonic/compare/audreyr:master...master
.. _`network`: https://github.com/audreyr/cookiecutter-pypackage/network
.. _`family tree`: https://github.com/audreyr/cookiecutter-pypackage/network/members
