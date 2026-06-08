import unittest
from packages.core.types import Request, Task, Result, ReasoningResult
from packages.core.engine import Engine


class TestCore(unittest.TestCase):
    def test_process_request(self):
        engine = Engine(None)
        request = Request('123', [Task('1', 1, 1)])
        result = engine.process_request(request)
        self.assertIsInstance(result, ReasoningResult)

    def test_perform_reasoning(self):
        engine = Engine(None)
        request = Request('123', [Task('1', 1, 1)])
        result = engine._perform_reasoning(request)
        self.assertIsInstance(result, ReasoningResult)

if __name__ == '__main__':
    unittest.main()