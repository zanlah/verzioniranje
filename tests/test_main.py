import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from naloga2 import konvolucija, filtriraj_z_gaussovim_jedrom, filtriraj_sobel_vertikalno, filtriraj_sobel_horizontalno

def test_konvolucija():
    test_image = np.array([[10, 20, 30, 40],
                           [50, 60, 70, 80],
                           [90, 100, 110, 120],
                           [130, 140, 150, 160]], dtype=np.float32)

    kernel = np.array([[1, 0, -1],
                       [2, 0, -2],
                       [1, 0, -1]], dtype=np.float32)

    expected_output = np.array([[-100,  -60,  -60,  130],
                                [-240,  -80,  -80,  280],
                                [-400,  -80,  -80,  440],
                                [-380,  -60,  -60,  410]], dtype=np.float32)

    result = konvolucija(test_image, kernel)
    np.testing.assert_array_almost_equal(result, expected_output)

def test_gaussian_filter():
    test_image = np.array([[10, 20, 30, 40],
                           [50, 60, 70, 80],
                           [90, 100, 110, 120],
                           [130, 140, 150, 160]], dtype=np.float32)
    sigma = 1.0
    result = filtriraj_z_gaussovim_jedrom(test_image, sigma)
    assert result.shape == test_image.shape 

def test_sobel_vertical():
    test_image = np.array([[10, 20, 30, 40],
                           [50, 60, 70, 80],
                           [90, 100, 110, 120],
                           [130, 140, 150, 160]], dtype=np.float32)

    expected_output = np.array([[ 160,  240,  280,  230],
                                [ 240,  320,  320,  240],
                                [ 240,  320,  320,  240],
                                [-280, -400, -440, -350]], dtype=np.float32)
    result = filtriraj_sobel_vertikalno(test_image)
    np.testing.assert_array_almost_equal(result, expected_output)

def test_sobel_horizontal():
    test_image = np.array([[10, 20, 30, 40],
                           [50, 60, 70, 80],
                           [90, 100, 110, 120],
                           [130, 140, 150, 160]], dtype=np.float32)

    expected_output = np.array([[ 100,   60,   60, -130],
                                [ 240,   80,   80, -280],
                                [ 400,   80,   80, -440],
                                [ 380,   60,   60, -410]], dtype=np.float32)
    result = filtriraj_sobel_horizontalno(test_image)
    np.testing.assert_array_almost_equal(result, expected_output)
