# -*- coding: utf-8 -*-

import logging
import uuid

from pylogrus import PyLogrus, TextFormatter, CL_BLDYLW


def get_logger():
    logging.setLoggerClass(PyLogrus)

    logger = logging.getLogger(__name__)  # type: PyLogrus
    logger.setLevel(logging.DEBUG)

    formatter = TextFormatter(datefmt='Z', colorize=True)
    # formatter.override_level_names({'CRITICAL': 'CRIT', 'ERROR': 'ERRO', 'WARNING': 'WARN', 'DEBUG': 'DEBU'})
    # formatter.override_colors({'prefix': CL_BLDYLW})

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


if __name__ == "__main__":
    log = get_logger()

    # Log message with the enabled and renamed fields
    log.debug("Using base logger")

    # Log message with extra field
    log.withFields({'user': 'John Doe'}).debug("Message with an extra field")

    # Add permanent field in logger (context)
    log_ctx = log.withFields({'context': 1})
    log_ctx.info("Add permanent field into current logger")

    # Add prefix to message
    log_ctx = log_ctx.withPrefix("[API]")
    log_ctx.info("Add prefix as a permanent part of a message")
    log_ctx.withFields({
        'user': 'Admin',
        'transaction_id': str(uuid.uuid4())
    }).warning("Message with prefix and extra fields")
    log_ctx.withFields({'error_code': 404}).error("Page not found")
    log_ctx.critical("System error")

    log.debug("Base logger has not been changed")
