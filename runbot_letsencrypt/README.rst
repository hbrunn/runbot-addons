.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

======================
Letsencrypt for runbot
======================

This module was written to allow users to request certificates for their runbot builds via letsencrypt. This is done manually because you'd max out the `rate limits <https://letsencrypt.org/docs/rate-limits>`_ quite fast otherwise. You can however configure some branches to request new certificates on every build.

Installation
============

To install this module, you need to have a working letsencrypt configuration (consult this module's documentation) for your nginx proxy. Emphasis on nginx because you really need the proxy, letsencrypt only works for port 443, and thus this module only work for modules with the ``nginx`` flag set.

Configuration
=============

To configure this module, you need to:

#. Go to *Settings / Configuration / Runbot* and review the rate limit for certificate requests
#. Add users to the group *Runbot / Request certificate*. But default, the public website user is a member of the group, so anyone can request certificates
#. In case you want to request a certificate for some branch's builds automatically, navigate to this branch in the backend and mark the appropriate checkbox

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/runbot-addons/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.
* https://helloworld.letsencrypt.org

Contributors
------------

* Holger Brunn <hbrunn@therp.nl>

Do not contact contributors directly about help with questions or problems concerning this addon, but use the `community mailing list <mailto:community@mail.odoo.com>`_ or the `appropriate specialized mailinglist <https://odoo-community.org/groups>`_ for help, and the bug tracker linked in `Bug Tracker`_ above for technical issues.

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
