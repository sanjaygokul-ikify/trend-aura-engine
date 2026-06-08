import argparse
from packages.core.types import Request, Task, Result, ReasoningResult
from packages.core.engine import Engine
from packages.utils.logging import logger


def main():
    parser = argparse.ArgumentParser(description='Distributed Autonomous Reasoning Engine CLI')
    parser.add_argument('--request_id', type=str, help='The ID of the request')
    parser.add_argument('--tasks', type=str, nargs='+', help='A list of tasks to process')
    args = parser.parse_args()

    # Create a Request object
    request = Request(args.request_id, [])
    for task_id in args.tasks:
        task = Task(task_id, 1, 1)
        request.tasks.append(task)

    engine = Engine(None)
    try:
        result = engine.process_request(request)
        logger.info(f'Result: {result.to_dict()}')
    except Exception as e:
        logger.error(f'Error processing request: {e}')