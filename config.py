import configparser

FILE = 'log_reader.ini'

def save(path:str):
    cfg = configparser.ConfigParser()
    cfg['path'] = path

    with open(FILE, 'w') as f:
        cfg.write(f)

def load():
    # cfg.read(FILE)
    pass