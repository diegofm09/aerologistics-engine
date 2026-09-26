class AerologisticsEngineError(Exception):
    """Base Aerologistics Engine Exception"""
    pass

class OverweightLimitError(AerologisticsEngineError):
    """The total weight is higher than the vehicle's capacity"""
    pass

class InvalidPackageError(AerologisticsEngineError):
    """The dimensions and weight of the packages must be > 0"""
    pass

class NonExistinPackageType(InvalidPackageError):
    """The package type must be either standard, express or refrigerated"""
    pass

class InvalidUrgencyLevel(InvalidPackageError):
    """The urgency level must be an integrer between 1 and 5"""
    pass

class InvalidTemperatureTarget(InvalidPackageError):
    """The temperature target must be between -50ºC and 5ºC"""
    pass

class RouteNotFoundError(AerologisticsEngineError):
    """This vehicle is not registered or has not been found"""
    pass

class PersistenceError(AerologisticsEngineError):
    """Error while opening files"""
    pass    

class VehicleWeightError(AerologisticsEngineError):
    """The vehicle weight capacity must be between 0.5 and 50000kg"""
    pass    

class InvalidShipping(AerologisticsEngineError):
    """The shipping km and kg must be higher than 0"""
    pass

