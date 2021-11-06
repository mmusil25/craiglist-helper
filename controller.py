from view import the_gui


def hello_world():
    the_gui()
    print('Exiting Program')
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    hello_world()