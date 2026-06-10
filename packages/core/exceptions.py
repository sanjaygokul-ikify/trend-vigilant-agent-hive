class VigilantAgentHiveException(Exception):
    pass

class InvalidThreatFeedError(VigilantAgentHiveException):
    pass

class EventProcessingError(VigilantAgentHiveException):
    pass

class MitigationError(VigilantAgentHiveException):
    pass
