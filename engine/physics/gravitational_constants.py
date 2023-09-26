# File: gravitational_constants.py
# Description: Defines gravitational constants for different dimensions.

class GravitationalConstants:
    @staticmethod
    def get_gravity_constant(dimension):
        if dimension == 2:
            return 9.8  # Standard Earth gravity for 2D
        elif dimension == 3:
            return 9.8  # Standard Earth gravity for 3D
        elif dimension == 4:
            return 9.8  # Hypothetical gravity constant for 4D
        elif dimension == 5:
            return 9.8  # Hypothetical gravity constant for 5D
        elif dimension == 6:
            return 9.8  # Hypothetical gravity constant for 6D
        elif dimension == 7:
            return 9.8  # Hypothetical gravity constant for 7D
        elif dimension == 9999:
            return 9.8  # Hypothetical gravity constant for 9999D
        else:
            raise ValueError("Unsupported dimension")

# Usage example:
# gravity_3d = GravitationalConstants.get_gravity_constant(3)
# print(f"Gravity in 3D world: {gravity_3d} m/s^2")
