DXL Client Python3.12 Patch
========================================
This outlines how to patch the dependencies of the opendxl-python client
for python3.12

Basic virtual env
-----------------
Set up your python virtual environment. Install setuptools using pip.

Edit collections init file
--------------------------
In ``[python_install_path]/collections/_init__.py``, change:

    .. code-block:: python

        import collections.abc as _collections_abc

to:
    .. code-block:: python

        import collections
        try:
            from collections.abc import Callable
            _collections_abc = collections.abc
        except ImportError:
            from collections import Callable
        import sys as _sys

    This change is made to deal with `_collections_abc` now being held in module `collections.abc`
    but still being referenced as `_collections_abc` frequently in code.

Libcrypto modification
----------------------
In ``[python_install_path]/site-packages/oscrypto-1.3.0-py1.12.egg/oscrypto/_openssl/_libscrypto_ctypes.py``
change these lines:

    .. code-block:: python

        version_match = re.search('\\b(\\d\\.\\d\\.\\d[a-z]*)\\b', version_string)
        if not version_match:
            version_match = re.search('(?<=LibreSSL )(\\d\\.\\d(\\.\\d)?)\\b', version_string)
        if not version_match:
            raise LibraryNotFoundError('Error detecting the version of libcrypto')
        version = version_match.group(1)
        version_parts = re.sub('(\\d)([a-z]+)', '\\1.\\2', version).split('.')
        version_info = tuple(int(part) if part.isdigit() else part for part in version_parts)


to:
    .. code-block:: python

        version_match = re.search(r'\b(\d+\.\d+\.\d+[a-z]*)\b', version_string)
        if not version_match:
            # Attempt to match LibreSSL version format
            version_match = re.search(r'(?<=LibreSSL )(\d+\.\d+(\.\d+)?)\b', version_string)
        if not version_match:
            raise RuntimeError(f'Error detecting the version of libcrypto from: {version_string}')
        version = version_match.group(1)
        version_parts = re.sub(r'(\d)([a-z]+)', r'\1.\2', version).split('.')
        version_info = tuple(int(part) if part.isdigit() else part for part in version_parts)

This change is needed to capture the new version output string format of LibreSSL.

Install dxlbootstrap
--------------------
Use pip to install dxlbootrap.

Conclusion
----------
With these steps, you should now be able to run ``dxlclient provisionconfig [SERVER_IP] [CLIENT_NAME]``
which is used to create a config file that can be used by the opendxl client.
