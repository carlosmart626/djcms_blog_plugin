=======
History
=======

0.2.0 (2026-07-21)
------------------

* Support Python 3.10-3.14, Django 5.2 LTS and django-cms 5.1.
* Replace ``ugettext_lazy`` with ``gettext_lazy`` and use bare ``super()``.
* Drop ``python_2_unicode_compatible``.
* Fix author avatar in the plugin template: use ``Author.profile_img_url``
  (the ``image`` field no longer exists in ``djcms_blog``).
* Move packaging to PEP 621 ``pyproject.toml``; require ``djcms_blog>=0.2.4``.
* Replace Travis CI with GitHub Actions (tests + PyPI Trusted Publishing).

0.1.0 (2018-09-08)
------------------

* First release on PyPI.
