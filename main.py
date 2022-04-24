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
    make_image.init_resources()
    # generate markers

    markers = random_org.get_random_range(0, 3)

    # 2 first are green markers positions
    # 2 second are white markers positions

    # generate frames

    frames = random_org.get_random_range(0, 2)

    # generate colors from 1 to 3 frame
    # 0 -> black
    # 1 -> red
    # 2 -> yellow

    # generate cubes

    cubes = random_org.get_random_range(0, 3)
    # generate cubes for yellow, red, green, blue room
    # numbers to colors:
    # 0 -> black
    # 1 -> red
    # 2 -> yellow
    # 3 -> null

    # generate men

    men = random_org.get_random_range(0, 7)
    # generates positions for null, null, yellow, green, red, blue, white, black

    make_image.create_field(markers, frames, cubes, men)

    return render_template('index.html')


if __name__ == '__main__':
    # port = int(os.environ.get("PORT", 7700))
    # app.run(host='0.0.0.0', port=port)
    app.run()
