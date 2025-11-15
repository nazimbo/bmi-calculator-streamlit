"""Logging configuration for BMI Calculator.

This module provides a singleton logger configuration to prevent
handler accumulation issues that occur with Streamlit reruns.
"""

import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional

from ..core.constants import (
    LOG_FILE_NAME,
    LOG_FILE_MAX_BYTES,
    LOG_FILE_BACKUP_COUNT,
    LOG_FORMAT,
)

# Global logger instance to prevent reconfiguration
_logger_instance: Optional[logging.Logger] = None
_configured: bool = False


def get_logger(name: str = __name__) -> logging.Logger:
    """Get or create a configured logger instance.

    This function ensures logging is configured only once, even across
    Streamlit reruns, preventing handler accumulation and file handle leaks.

    Args:
        name: Logger name (usually __name__ from calling module)

    Returns:
        Configured logger instance
    """
    global _logger_instance, _configured

    # Get logger for this module
    logger = logging.getLogger(name)

    # Only configure once globally
    if not _configured:
        # Set base logger level
        logger.setLevel(logging.INFO)

        # Create formatters
        formatter = logging.Formatter(LOG_FORMAT)

        # File handler with rotation
        try:
            file_handler = RotatingFileHandler(
                LOG_FILE_NAME,
                maxBytes=LOG_FILE_MAX_BYTES,
                backupCount=LOG_FILE_BACKUP_COUNT,
            )
            file_handler.setLevel(logging.INFO)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except (IOError, OSError) as e:
            # If file logging fails (e.g., permissions), continue without it
            print(f"Warning: Could not create log file: {e}", file=sys.stderr)

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Prevent propagation to root logger
        logger.propagate = False

        # Mark as configured
        _configured = True
        _logger_instance = logger

        logger.info("Logging system initialized successfully")

    return logger


def reset_logger() -> None:
    """Reset logger configuration (primarily for testing)."""
    global _configured, _logger_instance

    if _logger_instance:
        # Remove all handlers
        for handler in _logger_instance.handlers[:]:
            handler.close()
            _logger_instance.removeHandler(handler)

    _configured = False
    _logger_instance = None
