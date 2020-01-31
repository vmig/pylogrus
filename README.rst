PyLogrus
========

PyLogrus is a structured logger for Python which is inspired by Logrus
Golang library https://github.com/sirupsen/logrus. PyLogrus extends the
built-in ``logging`` module with the ability making a colorized records
in log and records in JSON format.

Features
--------

Using this package, you will be able to:

-  colorize output in console (Textual format)
-  switch off the colorization (Textual format)
-  add extra fields in a log record
-  add permanent extra fields in a log record
-  add permanent prefix for message
-  create a new contextual instance
-  save log records in the JSON format
-  override the names of logging levels
-  override colors of base elements (Textual format)
-  override name of keys (JSON format)
-  define only needed fields in records (JSON format)
-  create time of a record in Zulu format

.. figure:: https://github.com/vmig/pylogrus/blob/master/examples/screenshot.png?raw=true
   :alt: Colored


Initialization
--------------

.. code:: python

    import logging
    from pylogrus import PyLogrus

    logging.setLoggerClass(PyLogrus)


Formatters
----------

TextFormatter
~~~~~~~~~~~~~
TextFormatter class allows colorizing console output by setting a
``colorize`` argument. The colorization can be switched off. Time of log
record may be set in Zulu format (just set ``datefmt`` argument as 'Z') or
Unix epoch (set ``datefmt`` argument as 'U').

.. code:: python

    import logging
    from pylogrus import PyLogrus, TextFormatter

    logging.setLoggerClass(PyLogrus)

    logger = logging.getLogger(__name__)  # type: PyLogrus
    logger.setLevel(logging.DEBUG)

    formatter = TextFormatter(datefmt='Z', colorize=True)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)


Overriding name of levels
^^^^^^^^^^^^^^^^^^^^^^^^^
You can define only necessary changes:

.. code:: python

    formatter = TextFormatter(datefmt='Z', colorize=True)
    formatter.override_level_names({'CRITICAL': 'CRIT', 'ERROR': 'ERRO', 'WARNING': 'WARN', 'DEBUG': 'DEBU'})

or for instance:

.. code:: python

    formatter.override_level_names({'CRITICAL': 'FATAL'})


Overriding colors
^^^^^^^^^^^^^^^^^
TextFormatter has several base elements which can be colorized. You can
get them via ``color`` property:

::

    print(formatter.color)
    ...
    {
        'asctime':  '\x1b[2;37m',  # time of log record
        'prefix':   '\x1b[0;36m',  # message prefix
        'field':    '\x1b[0;32m',  # key of extra field
        'value':    '\x1b[0m',     # value of extra field
        'debug':    '\x1b[0;34m',
        'info':     '\x1b[0;32m',
        'warning':  '\x1b[0;33m',
        'error':    '\x1b[0;31m',
        'critical': '\x1b[2;31m'
    }

A color of elements can be changed using CL\_\* constants. You can
define new color only for those elements you need.

.. code:: python

    from pylogrus import PyLogrus, TextFormatter, CL_BLDYLW
    ...
    formatter = TextFormatter(colorize=True)
    formatter.override_colors({'prefix': CL_BLDYLW})


JsonFormatter
~~~~~~~~~~~~~
JsonFormatter class allows to save log records in the JSON format.
During class initialization, you can:

-  Set time of log record in Zulu format (set ``datefmt`` to 'Z') or
   Unix epoch format (set ``datefmt`` to 'U').
-  Define a list of enabled fields which will be present in a log record
   via ``enabled_fields`` argument. An enabled field is represented by
   original field name or by a tuple which contains the original name
   and new desirable name. The new name overrides the original one in an
   output.
-  For pretty print a JSON log record in a console, set the ``indent``
   and ``sort_keys`` arguments (optional).

.. code:: python

    import logging
    from pylogrus import PyLogrus, JsonFormatter

    logging.setLoggerClass(PyLogrus)

    logger = logging.getLogger(__name__)  # type: PyLogrus
    logger.setLevel(logging.DEBUG)

    enabled_fields = [
        ('name', 'logger_name'),
        ('asctime', 'service_timestamp'),
        ('levelname', 'level'),
        ('threadName', 'thread_name'),
        'message',
        ('exception', 'exception_class'),
        ('stacktrace', 'stack_trace'),
        'module',
        ('funcName', 'function')
    ]

    formatter = JsonFormatter(datefmt='Z', enabled_fields=enabled_fields, indent=2, sort_keys=True)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)


Overriding name of levels
^^^^^^^^^^^^^^^^^^^^^^^^^
Name of levels can be overridden in the same way as in case of using the
TextFormatter.

.. code:: python

    formatter = JsonFormatter()
    formatter.override_level_names({'WARNING': 'WARN'})


Usage
-----
Please, see the examples of usage in the ``examples`` directory.

Log message as usual:

.. code:: python

    import logging
    from pylogrus import PyLogrus, TextFormatter

    def get_logger():
        logging.setLoggerClass(PyLogrus)
        ...
        formatter = TextFormatter()
        ...
        return logger

    log = get_logger()
    log.debug("Using base logger")

Log message with an extra field:

.. code:: python

    log.withFields({'user': 'John Doe'}).debug("Message with an extra field")

Add permanent field(s) in logger and get a contextual instance:

.. code:: python

    log_ctx = log.withFields({'context': 1})
    log_ctx.info("Add permanent field into current logger")

Add permanent prefix to message for current logger instance:

.. code:: python

    log_ctx = log_ctx.withPrefix("[API]")
    log_ctx.info("Add prefix as a permanent part of a message")

Log message with extra fields:

.. code:: python

    log_ctx.withFields({
        'user': 'Admin',
        'transaction_id': str(uuid.uuid4())
    }).warning("Message with prefix and extra fields")
