from __future__ import annotations
import logging
from typing import Dict, List, Optional
from .types import ReasoningResult, Request
from .exceptions import ReasoningException, InvalidRequestException
import json
import heapq
from collections import defaultdict

logger = logging.getLogger(__name__)

class Engine:
    def __init__(self, persistence_layer: 'PersistenceLayer'):  # type: ignore
        self.persistence_layer = persistence_layer
        self.reasoning_results: Dict[str, ReasoningResult] = {}
        self.cache: Dict[str, ReasoningResult] = {}
        self.request_cache: Dict[str, Request] = {}

    def process_request(self, request: Request) -> ReasoningResult:
        try:
            if not request.tasks:
                raise InvalidRequestException('Request must contain at least one task')
            request_json = json.dumps(request.to_dict())
            if request_json in self.cache:
                return self.cache[request_json]
            if request.request_id in self.request_cache:
                return self._perform_reasoning(self.request_cache[request.request_id])
            self.request_cache[request.request_id] = request
            reasoning_result = self.persistence_layer.get_result(request_json)
            if reasoning_result is None:
                # Perform complex reasoning logic
                reasoning_result = self._perform_reasoning(request)
                self.persistence_layer.store_result(request_json, reasoning_result)
                self.cache[request_json] = reasoning_result
            return reasoning_result
        except Exception as e:
            logger.error(f'Error processing request: {e}')
            raise ReasoningException('Failed to process request') from e

    def _perform_reasoning(self, request: Request) -> ReasoningResult:
        # Simulate complex reasoning logic
        logger.info(f'Performing reasoning for request: {request}')
        # Create a priority queue to hold the reasoning tasks
        reasoning_tasks = []
        for task in request.tasks:
            # Calculate the priority of the task based on its importance and deadline
            priority = self._calculate_priority(task)
            heapq.heappush(reasoning_tasks, (priority, task))
        # Process the reasoning tasks in order of priority
        results = []
        while reasoning_tasks:
            _, task = heapq.heappop(reasoning_tasks)
            try:
                result = self._process_task(task)
                results.append(result)
            except Exception as e:
                logger.error(f'Error processing task: {task} - {e}')
                raise InvalidRequestException(f'Invalid request: {task} - {e}') from e
        return ReasoningResult(results)

    def _calculate_priority(self, task: Task) -> int:
        # Calculate the priority of the task based on its importance and deadline
        importance = task.importance
        deadline = task.deadline
        priority = importance * deadline
        return priority

    def _process_task(self, task: Task) -> Result:
        # Simulate the processing of the task
        logger.info(f'Processing task: {task}')
        # Create a dictionary to hold the results of the task
        result = {'task_id': task.task_id, 'result': 'success'}
        return Result(result)

    def get_result(self, request_json: str) -> Optional[ReasoningResult]:
        return self.persistence_layer.get_result(request_json)

    def store_result(self, request_json: str, reasoning_result: ReasoningResult):
        self.persistence_layer.store_result(request_json, reasoning_result)
