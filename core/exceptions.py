class AerologisticsEngineError(Exception):
    """Base Aerologistics Engine Exception"""
    pass

class OverweightLimitError(AerologisticsEngineError):
    """The total weight is higher than the trucks capacity"""
    pass

class InvalidPackageError(AerologisticsEngineError):
    """The dimensions and weight of the packages must be > 0"""
    pass

class InvalidUrgencyLevel(AerologisticsEngineError):
    """The urgency level must be an integrer between 1 and 5"""
    pass

class InvalidTemperatureTarget(AerologisticsEngineError):
    """The temperature target must be between -50ºC and 5ºC"""
    pass

class RouteNotFoundError(AerologisticsEngineError):
    """This vehicle is not registered or has not been found"""
    pass

class PersistenceError(AerologisticsEngineError):
    """Error while opening files"""
    pass    

class TruckWeightError(AerologisticsEngineError):
    """The truck weight capacity must be between 2500 and 50000kg"""
    pass    

