from collections import namedtuple
from datetime import datetime
from tkinter import Tk, filedialog


class Avarage:
    value = count = 0.0

    """ Search for floats in string and add to value"""
    def add_from_string(self, val_str:str, separator:str=" ", first_only=True):

        substrings = val_str.split(separator)
        for substr in substrings:
            o = 1 #TODO continue here
        # self.value += float(add_value)
        self.count += 1

    def get(self, decimals=2) -> float:
        if self.count < 0: self.count += 1
        return round(self.value/self.count, decimals)




def interpret_groups(groups):
    for group in groups:
        session_start = session_end = None

        # find first date in group
        for line in group:
            date_start = line.find('[')
            date_end = line.find(']')
            if date_start > -1 and date_end > -1:
                session_start = datetime.strptime(line[date_start+1:date_end], '%Y-%m-%d %H:%M:%S')
                break

        # find last date in group
        for line in reversed(group):
            # consider only 'Result accepted' lines as the ones that finish session
            if 'Result accepted by the pool' not in line:
                continue

            date_start = line.find('[')
            date_end = line.find(']')
            if date_start > -1 and date_end > -1:
                session_end = datetime.strptime(line[date_start + 1:date_end], '%Y-%m-%d %H:%M:%S')
                break

        # find avg hash rates
        avg = Avarage()
        for line in group:
            if 'Totals:' in line:
                print(line.split(' '))

        # avghr = round(avghr, 2)
        #
        # duration = session_end - session_start if (session_start and session_end) else "info not found"
        #
        # print('--> Started at:', session_start, '  Session Duration: ', duration, '  Avg H/s:', avghr)

        #TODO: merge sessions when within X minutes scope


def group_lines(lines):
    # group lines by content

    split_on = 'Pool logged in'
    split_idxes = []

    for idx, line in enumerate(lines):
        if split_on in line:
            split_idxes.append(idx)

    split_idxes.append(len(lines))

    groups = []
    for x in range(0, len(split_idxes)-1):
        start, end = split_idxes[x], split_idxes[x+1]
        groups.append(lines[start:end])

    return groups


def main():
    Tk().withdraw() # hide TK window
    log = filedialog.askopenfile().name

    with open(log) as file:
        lines = [l.strip() for l in file]

    groups = group_lines(lines)

    interpret_groups(groups)

    input() # keep console from closing


if __name__ == "__main__":
    main()
