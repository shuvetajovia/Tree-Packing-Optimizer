from geometry import (
    create_tree_polygon,
    rotate_polygon,
    move_polygon,
    overlaps
)


def pack_trees(
    n,
    rotations=None,
    spacing=0.15
):
    """
    Packs n trees without overlap using a grid-based heuristic.

    Args:
        n (int): Number of trees
        rotations (list): Rotation hints in degrees
        spacing (float): Gap between trees

    Returns:
        polygons (list): List of tree polygons
        placements (list): List of (x, y, rotation)
    """

    placed_polygons = []
    placements = []

    grid_size = int(n ** 0.5) + 1
    step = 1.5 + spacing

    if rotations is None:
        rotations = [0.0] * n

    tree_id = 0

    for i in range(grid_size):
        for j in range(grid_size):

            if tree_id >= n:
                return placed_polygons, placements

            base_tree = create_tree_polygon()

            rotation_candidates = [
                rotations[tree_id],
                rotations[tree_id] + 30,
                rotations[tree_id] - 30,
                0.0,
                60.0,
                120.0
            ]

            placed = False

            for angle in rotation_candidates:
                rotated = rotate_polygon(base_tree, angle)

                x = i * step
                y = j * step

                moved = move_polygon(rotated, x, y)

                collision = False
                for p in placed_polygons:
                    if overlaps(moved, p):
                        collision = True
                        break

                if not collision:
                    placed_polygons.append(moved)
                    placements.append((x, y, angle))
                    placed = True
                    break

            if not placed:
                raise RuntimeError(f"Failed to place tree {tree_id}")

            tree_id += 1

    return placed_polygons, placements
