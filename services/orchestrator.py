from packages.core.types import Request, Task, Result, ReasoningResult
from packages.core.engine import Engine


class Orchestrator:
    def __init__(self, engine: Engine):
        self.engine = engine

    def process_request(self, request: Request) -> ReasoningResult:
        return self.engine.process_request(request)

    def _perform_reasoning(self, request: Request) -> ReasoningResult:
        # This method is not needed here as it is already part of the Engine class
        pass