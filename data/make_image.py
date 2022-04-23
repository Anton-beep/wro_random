from PIL import Image

PATH_IMG = '../static/img/field_res/'

MARKERS_NUM_TO_PIX_COORDS = {
    0: (3513 // 8, 2919 // 8),
    1: (14832 // 8, 2919 // 8),
    2: (14832 // 8, 5831 // 8),
    3: (3513 // 8, 5831 // 8),
}

MARKER_SIZE = (249 // 8, 249 // 8)

CUBES_NUM_TO_PIX_COORDS = {
    0: (3247 // 8, 2212 // 8),
    1: (15102 // 8, 2212 // 8),
    2: (15102 // 8, 6539 // 8),
    3: (3247 // 8, 6540 // 8),
}

CUBE_SIZE = (249 // 8, 249 // 8)

FRAMES_NUM_TO_PIX_COORDS = {
    0: (8154 // 8, 7906 // 8),
    1: (8986 // 8, 7906 // 8),
    2: (9820 // 8, 7906 // 8)
}

FRAME_SIZE = (624 // 8, 624 // 8)


def init_resources():
    # cubes
    cube_red = Image.new('RGB', CUBE_SIZE, color='red')
    cube_yellow = Image.new('RGB', CUBE_SIZE, color='yellow')
    cube_black = Image.new('RGB', CUBE_SIZE, color='black')
    cube_red.save(PATH_IMG + 'cube_red.png')
    cube_yellow.save(PATH_IMG + 'cube_yellow.png')
    cube_black.save(PATH_IMG + 'cube_black.png')

    # markers
    marker_green = Image.new('RGB', MARKER_SIZE, color='green')
    marker_white = Image.new('RGB', MARKER_SIZE, color='white')
    marker_green.save(PATH_IMG + 'marker_green.png')
    marker_white.save(PATH_IMG + 'marker_white.png')

    # frames
    frame_red = Image.new('RGB', FRAME_SIZE, color='red')
    frame_yellow = Image.new('RGB', FRAME_SIZE, color='yellow')
    frame_black = Image.new('RGB', FRAME_SIZE, color='black')
    frame_red.save(PATH_IMG + 'frame_red.png')
    frame_yellow.save(PATH_IMG + 'frame_yellow.png')
    frame_black.save(PATH_IMG + 'frame_black.png')


def create_field(markers, frames, cubes) -> str:
    """returns path to image"""

    # cubes
    cube_red = Image.open(PATH_IMG + 'cube_red.png')
    cube_yellow = Image.open(PATH_IMG + 'cube_yellow.png')
    cube_black = Image.open(PATH_IMG + 'cube_black.png')

    NUM_TO_CUBES = {
        0: cube_black,
        1: cube_red,
        2: cube_yellow,
        3: None
    }

    # markers
    marker_green = Image.open(PATH_IMG + 'marker_green.png')
    marker_white = Image.open(PATH_IMG + 'marker_white.png')

    # frames
    frame_red = Image.open(PATH_IMG + 'frame_red.png')
    frame_yellow = Image.open(PATH_IMG + 'frame_yellow.png')
    frame_black = Image.open(PATH_IMG + 'frame_black.png')

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

        img_field.save(PATH_IMG + 'img_res.png')


