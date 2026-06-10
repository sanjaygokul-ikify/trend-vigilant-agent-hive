import argparse
from packages.core import RuntimeEngine, EventStreamProcessor, MLAnomalyDetector, ContainmentEngine, PolicyEnforcement
from packages.services import Orchestrator
from packages.utils import logging

logger = logging.get_logger(__name__)

parser = argparse.ArgumentParser(description='Vigilant Agent Hive CLI')
def main(args):
    logger.info('CLI running...')
    # create and run orchestrator
    engine = RuntimeEngine([])
    stream_processor = EventStreamProcessor(engine)
    anomaly_detector = MLAnomalyDetector('model_path')
    containment_engine = ContainmentEngine(PolicyEnforcement())
    orchestrator = Orchestrator(engine, stream_processor, anomaly_detector, containment_engine, PolicyEnforcement())
    orchestrator.run()