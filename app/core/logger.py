"""Logger configuration for the AI idea validation system."""

import logging

logger = logging.getLogger("idea-validator")

if not logger.handlers:
    logging.basicConfig(level=logging.INFO)

logger.info("Logger initialized for AI system")
