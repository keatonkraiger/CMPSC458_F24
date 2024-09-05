from graphics.engine import Engine

window_width = 800
window_height = 600

if __name__=='__main__':
    engine = Engine(width=window_width, height=window_height)
    engine.run()