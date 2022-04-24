import os
from PIL import Image

PATH_IMG = 'static/img/field_res/'

MARKERS_NUM_TO_PIX_COORDS = {
    0: (439, 364),
    1: (1854, 364),
    2: (1854, 728),
    3: (439, 728)
}

MARKER_SIZE = (31, 31)

CUBES_NUM_TO_PIX_COORDS = {
    0: (405, 276),
    1: (1887, 276),
    2: (1887, 817),
    3: (405, 817)
}

CUBE_SIZE = (31, 31)

FRAMES_NUM_TO_PIX_COORDS = {
    0: (1019, 988),
    1: (1123, 988),
    2: (1227, 988)
}

FRAME_SIZE = (78, 78)

MEN_NUM_TO_PIX_COORDS = {
    0: (575, 135),
    1: (889, 275),
    2: (1380, 451),
    3: (1689, 118),
    4: (596, 864),
    5: (929, 775),
    6: (1429, 805),
    7: (1674, 1040)
}

MAN_SIZE = (45, 14)


def init_resources():
    # cubes
    cube_red = Image.open(PATH_IMG + 'cubes/cube_red.png')
    cube_yellow = Image.open(PATH_IMG + 'cubes/cube_yellow.png')
    cube_black = Image.open(PATH_IMG + 'cubes/cube_black.png')

    cube_red.thumbnail(CUBE_SIZE)
    cube_yellow.thumbnail(CUBE_SIZE)
    cube_black.thumbnail(CUBE_SIZE)

    cube_red.save(PATH_IMG + 'cubes/cube_red.png')
    cube_yellow.save(PATH_IMG + 'cubes/cube_yellow.png')
    cube_black.save(PATH_IMG + 'cubes/cube_black.png')

    # markers
    marker_green = Image.open(PATH_IMG + 'markers/marker_green.png')
    marker_white = Image.open(PATH_IMG + 'markers/marker_white.png')

    marker_green.thumbnail(MARKER_SIZE)
    marker_white.thumbnail(MARKER_SIZE)

    marker_green.save(PATH_IMG + 'markers/marker_green.png')
    marker_white.save(PATH_IMG + 'markers/marker_white.png')

    # frames
    frame_red = Image.open(PATH_IMG + 'frames/frame_red.png')
    frame_yellow = Image.open(PATH_IMG + 'frames/frame_yellow.png')
    frame_black = Image.open(PATH_IMG + 'frames/frame_black.png')

    frame_red.thumbnail(FRAME_SIZE)
    frame_yellow.thumbnail(FRAME_SIZE)
    frame_black.thumbnail(FRAME_SIZE)

    frame_red.save(PATH_IMG + 'frames/frame_red.png')
    frame_yellow.save(PATH_IMG + 'frames/frame_yellow.png')
    frame_black.save(PATH_IMG + 'frames/frame_black.png')

    # men
    man_black = Image.open(PATH_IMG + 'men/man_black.png')
    man_blue = Image.open(PATH_IMG + 'men/man_blue.png')
    man_green = Image.open(PATH_IMG + 'men/man_green.png')
    man_red = Image.open(PATH_IMG + 'men/man_red.png')
    man_white = Image.open(PATH_IMG + 'men/man_white.png')
    man_yellow = Image.open(PATH_IMG + 'men/man_yellow.png')

    man_black.thumbnail(MAN_SIZE)
    man_blue.thumbnail(MAN_SIZE)
    man_green.thumbnail(MAN_SIZE)
    man_red.thumbnail(MAN_SIZE)
    man_white.thumbnail(MAN_SIZE)
    man_yellow.thumbnail(MAN_SIZE)

    man_black.save(PATH_IMG + 'men/man_black.png')
    man_blue.save(PATH_IMG + 'men/man_blue.png')
    man_green.save(PATH_IMG + 'men/man_green.png')
    man_red.save(PATH_IMG + 'men/man_red.png')
    man_white.save(PATH_IMG + 'men/man_white.png')
    man_yellow.save(PATH_IMG + 'men/man_yellow.png')


def create_field(markers, frames, cubes, men) -> str:
    """returns path to image"""

    # cubes
    cube_red = Image.open(PATH_IMG + 'cubes/cube_red.png')
    cube_yellow = Image.open(PATH_IMG + 'cubes/cube_yellow.png')
    cube_black = Image.open(PATH_IMG + 'cubes/cube_black.png')

    NUM_TO_CUBES = {
        0: cube_black,
        1: cube_red,
        2: cube_yellow,
        3: None
    }

    # markers
    marker_green = Image.open(PATH_IMG + 'markers/marker_green.png')
    marker_white = Image.open(PATH_IMG + 'markers/marker_white.png')

    # frames
    frame_red = Image.open(PATH_IMG + 'frames/frame_red.png')
    frame_yellow = Image.open(PATH_IMG + 'frames/frame_yellow.png')
    frame_black = Image.open(PATH_IMG + 'frames/frame_black.png')

    # men
    man_black = Image.open(PATH_IMG + 'men/man_black.png')
    man_blue = Image.open(PATH_IMG + 'men/man_blue.png')
    man_green = Image.open(PATH_IMG + 'men/man_green.png')
    man_red = Image.open(PATH_IMG + 'men/man_red.png')
    man_white = Image.open(PATH_IMG + 'men/man_white.png')
    man_yellow = Image.open(PATH_IMG + 'men/man_yellow.png')

    NUM_TO_FRAMES = {
        0: frame_black,
        1: frame_red,
        2: frame_yellow
    }

    with Image.open(PATH_IMG + 'wro_default.png') as img_field:
        # markers
        img_field.paste(marker_green, MARKERS_NUM_TO_PIX_COORDS[markers[0]])
        img_field.paste(marker_green, MARKERS_NUM_TO_PIX_COORDS[markers[1]])

        img_field.paste(marker_white, MARKERS_NUM_TO_PIX_COORDS[markers[2]])
        img_field.paste(marker_white, MARKERS_NUM_TO_PIX_COORDS[markers[3]])

        # frames
        for ind, frame in enumerate(frames):
            img_field.paste(NUM_TO_FRAMES[frame], FRAMES_NUM_TO_PIX_COORDS[ind])

        # cubes
        for ind, cube in enumerate(cubes):
            if NUM_TO_CUBES[cube]:
                img_field.paste(NUM_TO_CUBES[cube], CUBES_NUM_TO_PIX_COORDS[ind])

        # men
        men_img = [man_black, man_blue, man_green, man_red, man_white, man_yellow]
        for pos, img_man in zip(men[2:], men_img):
            img_field.paste(img_man, MEN_NUM_TO_PIX_COORDS[pos])

        img_field.save(PATH_IMG + 'img_res.png')
