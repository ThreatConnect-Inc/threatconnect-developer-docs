.. hint:: The "^" character means "starts with". For example, this character would be used to find all URL Indicators that start with ``http://xn--`` or all Groups whose name starts with ``APT``.

.. note:: The ``=``, ``<``, ``>``, and ``^`` operators in any filters must be `URL encoded <https://en.wikipedia.org/wiki/Percent-encoding>`__ as follows:
    
    +-----------+------------------+
    | Character | URL Encoded Form |
    +===========+==================+
    | =         | ``%3D``          |
    +-----------+------------------+
    | <         | ``%3C``          |
    +-----------+------------------+
    | >         | ``%3E``          |
    +-----------+------------------+
    | ^         | ``%5E``          |
    +-----------+------------------+
