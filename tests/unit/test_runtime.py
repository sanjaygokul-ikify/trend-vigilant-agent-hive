from packages.core import RuntimeEngine, Event
import unittest

class TestRuntime(unittest.TestCase):
    def test_process_events(self):
        engine = RuntimeEngine([])
        events = [Event(1, 'type', 'data')]
        engine.process_events(events)

if __name__ == '__main__':
    unittest.main()