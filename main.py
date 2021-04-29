# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sanic import Sanic

app = Sanic("app")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
