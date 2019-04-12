#!/usr/bin/env python

import cv2


def rectangle_or_square(approximation):
    """Computes the aspect ratio to determine if shape is a square or rectangle.

    Usage (Example does not work...): 
    >>> _, contour, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    >>> epsilon = boundPercentage * cv2.arcLength(contour, True)
    >>> approximation = cv2.approxPolyDP(contour, epsilon, True)
    >>> recrangle_or_square(approximation)
	Get the approximation using 
    """
    (x, y, w, h) = cv2.boundingRect(approximation)
    aspectRatio = w / float(h)
    return 'square' if 0.95 <= aspectRatio <= 1.05 else 'rectangle'