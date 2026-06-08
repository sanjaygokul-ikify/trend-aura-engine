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
    def __init__(self, persistence_layer: PersistenceLayer):
        self.persistence_layer = persistence_layer
        self.reasoning_results: Dict[str, ReasoningResult] = {}

    def process_request(self, request: Request) -> ReasoningResult:
        try:
            request_json = json.dumps(request.to_dict())
            reasoning_result = self.persistence_layer.get_result(request_json)
            if reasoning_result is None:
                # Perform complex reasoning logic
                reasoning_result = self._perform_reasoning(request)
                self.persistence_layer.store_result(request_json, reasoning_result)
            return reasoning_result
        except Exception as e:
            logger.error(f'Error processing request: {e}')
            raise ReasoningException('Failed to process request')

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
            result = self._process_task(task)
            results.append(result)
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
        result = defaultdict(dict)
        result['task_id'] = task.task_id
        result['result'] = 'success'
        return Result(result)

    def get_result(self, request_json: str) -> Optional[ReasoningResult]:
        return self.persistence_layer.get_result(request_json)

    def store_result(self, request_json: str, reasoning_result: ReasoningResult):
        self.persistence_layer.store_result(request_json, reasoning_result)
