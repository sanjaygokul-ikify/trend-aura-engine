from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Request:
    request_id: str
    tasks: List['Task']

@dataclass
class Task:
    task_id: str
    importance: int
    deadline: int

@dataclass
class Result:
    result: Dict[str, str]

@dataclass
class ReasoningResult:
    results: List[Result]

    def to_dict(self) -> Dict[str, List[Dict[str, str]]]:
        return {'results': [result.result for result in self.results]}