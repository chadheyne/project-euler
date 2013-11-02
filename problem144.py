#!/usr/bin/env python
from math import sqrt


def find_slope_a(origin, new_point):
    (x_orig, y_orig), (x_new, y_new) = origin, new_point

    slope_a = (y_orig - y_new) / (x_orig - x_new)
    slope_tangent = -4 * (x_orig / y_orig)

    slope_b = find_slope_b(slope_a, slope_tangent)
    b_intercept = y_orig - slope_b * x_orig

    return slope_b, b_intercept


def find_slope_b(slope_a, slope_tangent):
    tan_a = (slope_a - slope_tangent) / (1 + slope_a * slope_tangent)
    slope_b = (slope_tangent - tan_a) / (1 + tan_a * slope_tangent)
    return slope_b


def calculate_points(slope_b, origin, b_intercept):
    x_orig, y_orig = origin

    a, b, c = (4 + slope_b ** 2,
               2 * slope_b * b_intercept,
               b_intercept ** 2 - 100)

    discriminant = sqrt(b ** 2 - 4 * a * c)

    pos_answer, neg_answer = ((-b + discriminant) / (2 * a),
                              (-b - discriminant) / (2 * a))

    return (pos_answer if abs(pos_answer - x_orig) > abs(neg_answer - x_orig)
            else neg_answer)


def calculate_intersections():
    (x_new, y_new), (x_orig, y_orig) = (0.0, 10.1), (1.4, -9.6)
    bounces = 0
    while x_orig > 0.01 or x_orig < -0.01 or y_orig < 0:
        slope_b, b_intercept = find_slope_a((x_orig, y_orig), (x_new, y_new))
        x_new, y_new = x_orig, y_orig
        quadratic_solution = calculate_points(slope_b, (x_orig, y_orig), b_intercept)
        x_orig, y_orig = quadratic_solution, slope_b * quadratic_solution + b_intercept
        bounces += 1

    return bounces


def main():
    num_bounces = calculate_intersections()
    print(num_bounces)


if __name__ == "__main__":
    main()
