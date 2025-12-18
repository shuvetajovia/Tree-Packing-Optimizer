import random
from packer import pack_trees
from geometry import bounding_square


def optimize_packing(
    n,
    rotation_hints=None,
    trials=10
):
    """
    Runs multiple packing trials and selects the best one.

    Args:
        n (int): Number of trees
        rotation_hints (list or None): ML-suggested base rotations
        trials (int): Number of heuristic attempts

    Returns:
        dict: {
            "side": float,
            "placements": list of (x, y, rotation)
        }
    """

    best_solution = None
    best_side = float("inf")

    for _ in range(trials):

        # Generate rotations
        if rotation_hints:
            rotations = [
                rotation_hints[0] + random.uniform(-10, 10)
                for _ in range(n)
            ]
        else:
            rotations = [random.uniform(60, 150) for _ in range(n)]

        # Pack trees
        polygons, placements = pack_trees(n, rotations)

        # Compute bounding square
        side = bounding_square(polygons)

        # Keep best
        if side < best_side:
            best_side = side
            best_solution = {
                "side": round(best_side, 4),
                "placements": placements
            }

    return best_solution
