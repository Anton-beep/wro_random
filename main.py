import os

from flask import Flask, render_template, request

from data import make_image
from data import random_org

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some_secret_key'

API_TEMPLATE = 'https://www.random.org/'

NUM_TO_ROOM = {
    0: 'yellow room',
    1: 'red room',
    2: 'green room',
    3: 'blue room'
}


@app.route('/')
def main():
    # make_image.init_resources()
    # generate markers

    markers = random_org.get_random_range(0, 3)

    # green markers 2 first

    # print(f'GREEN markers: {[NUM_TO_ROOM[marker] for marker in markers[:2]]}')
    # print(f'WHITE markers: {[NUM_TO_ROOM[marker] for marker in markers[2:]]}')

    # generate frames

    frames = random_org.get_random_range(0, 2)

    NUM_TO_COL = {
        0: 'black',
        1: 'red',
        2: 'yellow',
        3: 'null'
    }

    # print(f'FRAMES: {[NUM_TO_COL[frame] for frame in frames]}')

    # generate cubes

    cubes = random_org.get_random_range(0, 3)

    # print(
    #     f'CUBES: {[(NUM_TO_ROOM[el[0]], el[1]) for el in (enumerate([NUM_TO_COL[cube] for cube in cubes]))]}')

    make_image.create_field(markers, frames, cubes)

    return render_template('index.html')


if __name__ == '__main__':
    # port = int(os.environ.get("PORT", 7700))
    # app.run(host='0.0.0.0', port=port)
    app.run()
