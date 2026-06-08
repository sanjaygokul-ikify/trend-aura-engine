from __future__ import annotations
import logging
from typing import Dict, List, Optional
from ..core.types import Request, ReasoningResult
from ..core.exceptions import ReasoningException
from ..core.engine import Engine

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine

    def execute_request(self, request: Request) -> ReasoningResult:
        try:
            reasoning_result = self.engine.process_request(request)
            return reasoning_result
        except ReasoningException as e:
            logger.error(f'Error executing request: {e}')
            raise
