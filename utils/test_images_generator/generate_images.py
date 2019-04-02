import cv2
import numpy as np
from pathlib import Path

# from config import PROJECT_ROOT, PATCH_SIZE

PROJECT_ROOT = Path(__file__).parent
PATCH_SIZE = 32

AVAILABLE_SHAPES_DICT = {
    'LINE': 'LINE',
    'TRIANGLE': 'TRIANGLE',
    'RECTANGLE': 'RECTANGLE',
    'CIRCLE': 'CIRCLE',
}

AVAILABLE_COLORS_DICT = {
    'RED': (0, 0, 255),
    'GREEN': (0, 255, 0),
    'BLUE': (255, 0, 0),
    'YELLOW': (0, 255, 255),
    'PURPLE': (255, 0, 255),
    'CYAN': (255, 255, 0)
}


def generate_patches_set(set_name, patch_size, count, target_width, target_height):
    images_path = PROJECT_ROOT / Path('assets/source-images/{}'.format(set_name))
    images_path.mkdir(parents=True, exist_ok=True)

    # ToDo generate full color patches
    # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.full.html

    # np.full((PATCH_SIZE, PATCH_SIZE, 3), _get_random_color())

    generated_patches = 0

    while generated_patches < count:
        generated_image = _generate_random_image(target_width, target_height)
        cv2.imshow('generated image', generated_image)
        cv2.waitKey(1)

        # ToDo remove break after implementing loop below
        break

        for y in range(0, target_height - patch_size, patch_size):
            for x in range(0, target_width - patch_size, patch_size):
                if generated_patches >= count:
                    continue

                # ToDo get patch from generated image
                # https://docs.scipy.org/doc/numpy-dev/user/quickstart.html

                is_patch_interesting = True

                # ToDo check if patch is not filled with one color

                if is_patch_interesting:
                    # ToDo save patch
                    generated_patches += 1

                    print('GENERATED {:04d} OF {} PATCHES'.format(generated_patches, count))

    cv2.waitKey(0)


def generate_target_image(image_name, width, height):
    generated_image = _generate_random_image(width, height)

    image_path = PROJECT_ROOT / Path('assets/{}'.format(image_name))

    cv2.imwrite(image_path.as_posix(), generated_image)

    cv2.imshow('generated image', generated_image)
    cv2.waitKey(0)


def _generate_random_image(width, height):
    generated_image = np.zeros((height, width, 3), dtype=np.uint8)
    # ToDo generate white image
    generated_image = np.full((height, width, 3), (255, 255, 255), dtype=np.uint8)

    # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.full.html

    # ToDo choose random number of shapes from AVAILABLE_SHAPES_DICT
    # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.choice.html

    shapes = np.array(list(AVAILABLE_SHAPES_DICT.values()))

    print(shapes)
    print(np.random.randint(4, size=10))

    # np.random.randint(2, size=10)
    chosen_shapes = shapes[np.random.randint(4, size=10)]


    for shape in chosen_shapes:
        if shape == AVAILABLE_SHAPES_DICT['LINE']:
            _draw_random_line(generated_image)
        elif shape == AVAILABLE_SHAPES_DICT['TRIANGLE']:
            _draw_random_triangle(generated_image)
        elif shape == AVAILABLE_SHAPES_DICT['RECTANGLE']:
            _draw_random_rectangle(generated_image)
        elif shape == AVAILABLE_SHAPES_DICT['CIRCLE']:
            _draw_random_circle(generated_image)

    return generated_image


def _draw_random_line(generated_image):
    # ToDo draw random line (use _generate_random_image_points and _get_random_color)
    # https://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html
    # https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html
    print(generated_image.shape)
    yy = np.random.choice(generated_image.shape[0], 2)
    xx = np.random.choice(generated_image.shape[1], 2)

    a_t = (xx[0], yy[0])
    b_t = (xx[1], yy[1])

    print(_get_random_color())
    cv2.line(generated_image, a_t, b_t, _get_random_color(), 5)

    return


def _draw_random_triangle(generated_image):
    # ToDo draw random triangle (use _generate_random_image_points and _get_random_color)
    # https://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html
    # https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html
    # format for triangle: reshape((-1, 1, 2)
    # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.reshape.html
    yy = np.random.choice(generated_image.shape[0], 3)
    xx = np.random.choice(generated_image.shape[1], 3)

    triangle = np.array([[xx[0],yy[0]],[xx[1],yy[1]],[xx[2],yy[2]]], np.int32)
    pts = triangle.reshape((-1, 1, 2))

    print(triangle)
    print(pts)

    # pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    # pts = pts.reshape((-1, 1, 2))

    # cv2.polylines(generated_image, [pts], True, _get_random_color())
    cv2.fillPoly(generated_image, [pts], _get_random_color())
    return


def _draw_random_rectangle(generated_image):
    # ToDo draw random line (use _generate_random_image_points and _get_random_color)
    # https://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html
    # https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html

    yy = np.random.choice(generated_image.shape[0], 2)
    xx = np.random.choice(generated_image.shape[1], 2)

    a_t = (xx[0], yy[0])
    b_t = (xx[1], yy[1])

    cv2.rectangle(generated_image, a_t, b_t, _get_random_color(), -1)
    return


def _draw_random_circle(generated_image):
    # ToDo draw random line (use _generate_random_image_points and _get_random_color)
    # https://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html
    # https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html
    yy = np.random.choice(generated_image.shape[0], 2)
    xx = np.random.choice(generated_image.shape[1], 2)

    a_t = (xx[0], yy[0])
    b_t = (xx[1], yy[1])

    cv2.circle(generated_image, a_t, np.random.randint(150, size=1)[0], _get_random_color(), -1)

    return


def _generate_random_image_points(image, count):
    widths = np.random.randint(0, image.shape[1], size=count)
    heights = np.random.randint(0, image.shape[0], size=count)
    return list(zip(widths, heights))


def _get_random_color():
    # ToDo choose random color from AVAILABLE_COLORS_DICT
    # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.choice.html

    # colors = np.array(list(AVAILABLE_COLORS_DICT.values()))
    # print(colors[np.random.choice(6, size=1)[0]])
    # return colors[np.random.choice(6, size=1)[0]]
    c = np.random.choice(256,3)
    return [int(x) for x in c]
    # return np.random.choice(256, 3)
    # random_color_tuple = tuple(random_color.reshape(1, -1)[0])
    # return random_color_tuple
    # return (0, 0, 0)


if __name__ == "__main__":
    # generate_patches_set('test', PATCH_SIZE, 300, 900, 500)
    generate_target_image('test-target.jpg', 900, 500)
