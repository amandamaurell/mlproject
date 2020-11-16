# Import from standard library
import mlproject
from math import radians, cos, sin, asin, sqrt
# Import from our tools
from mlproject.tools import haversine
import pytest


def test_haversine():

    lat1, lon1 = 48.865070, 2.380009
    lat2, lon2 = -22.933950, -43.244590

    distance = haversine(lon1, lat1, lon2, lat2)

    assert distance == 9175.609429917933
