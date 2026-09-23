from models import StandardPackage, ExpressPackage, RefrigeratedPackage
from typing import Any
import exceptions

class PackageFactory:
    """The package factory"""

    @staticmethod
    def create_package(type: str, **kwargs) -> Any:
        """Creates a package based on its type """
        match type.lower():
            case "standard":
                return StandardPackage(**kwargs)
            case "express":
                return ExpressPackage(**kwargs)
            case "refrigerated":
                return RefrigeratedPackage(**kwargs)
            case _:
                raise exceptions.NonExistinPackageType(exceptions.NonExistinPackageType.__doc__)
