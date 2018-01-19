from pathlib import Path

FILE = './log_reader.config'


def config_save(path: str):
    with open(FILE, 'w') as f:
        f.write(path)


def config_load():
    try:
        with open(FILE, 'r') as f:
            path = Path(f.readline())

        return str(path) if path.is_file() else None
    except FileNotFoundError:
        return None


class Average:
    value = count = 0.0

    """ Search for first number in a string and add to averaged value"""
    def add_from_string(self, val_str:str, separator:str=" "):
        for substr in val_str.split(separator):
            try:
                self.value += float(substr)
                self.count += 1
                break
            except:
                pass

    def get(self, decimals=2) -> float:
        return round(self.value/max(self.count, 1), decimals)

