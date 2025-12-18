from shapely.geometry import Polygon
from shapely.affinity import rotate, translate


def create_tree_polygon(scale=1.0):
    """
    Creates a simple triangular Christmas tree shape.

    Returns:
        shapely.geometry.Polygon
    """
    return Polygon([
        (0.0, 0.0),
        (1.0 * scale, 0.0),
        (0.5 * scale, 1.2 * scale)
    ])


def rotate_polygon(polygon, angle_deg):
    """
    Rotates a polygon around its centroid.

    Args:
        polygon (Polygon)
        angle_deg (float)

    Returns:
        Polygon
    """
    return rotate(
        polygon,
        angle_deg,
        origin="centroid",
        use_radians=False
    )


def move_polygon(polygon, x, y):
    """
    Translates a polygon.

    Args:
        polygon (Polygon)
        x (float)
        y (float)

    Returns:
        Polygon
    """
    return translate(polygon, xoff=x, yoff=y)


def overlaps(poly1, poly2):
    """
    Checks if two polygons overlap.
    """
    return poly1.intersects(poly2)


def bounding_square(polygons):
    """
    Computes the side length of the smallest square
    that bounds all polygons.

    Args:
        polygons (list of Polygon)

    Returns:
        float
    """

    minx, miny, maxx, maxy = polygons[0].bounds

    for p in polygons[1:]:
        bx = p.bounds
        minx = min(minx, bx[0])
        miny = min(miny, bx[1])
        maxx = max(maxx, bx[2])
        maxy = max(maxy, bx[3])

    side = max(maxx - minx, maxy - miny)
    return round(side, 4)
