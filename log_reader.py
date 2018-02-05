from datetime import datetime, timedelta
from tkinter import Tk, filedialog

import ui
import utils
from utils import Average


class Session:
    date_start = date_end = hashrate = duration = None

    def __init__(self, lines):
        # find first date in group
        for line in lines:
            date_start = line.find('[')
            date_end = line.find(']')
            if date_start > -1 and date_end > -1:
                self.date_start = datetime.strptime(line[date_start + 1:date_end], '%Y-%m-%d %H:%M:%S')
                break

        # find last date in group
        for line in reversed(lines):
            # consider only 'Result accepted' lines as the ones that finish session
            if 'Result accepted by the pool' not in line:
                continue

            date_start = line.find('[')
            date_end = line.find(']')
            if date_start > -1 and date_end > -1:
                self.date_end = datetime.strptime(line[date_start + 1:date_end], '%Y-%m-%d %H:%M:%S')
                break

        # find avg hash rates
        avg = Average()
        for line in lines:
            if 'Totals:' in line:
                avg.add_from_string(line)
        self.hashrate = avg.get()

        self.duration = self.date_end - self.date_start if (self.date_start and self.date_end) else "---"

    def __str__(self):
        return "    ".join([str(v) for v in [self.date_start, self.duration, self.hashrate]])


def get_sessions(lines):
    split_on = 'Pool logged in'
    split_idxes = []

    for idx, line in enumerate(lines):
        if split_on in line:
            split_idxes.append(idx)

    split_idxes.append(len(lines))

    sessions_lines = []
    for x in range(0, len(split_idxes)-1):
        start, end = split_idxes[x], split_idxes[x+1]
        sessions_lines.append(lines[start:end])

    sessions = [Session(lines) for lines in sessions_lines]

    return sessions

def main():
    log = utils.config_load()

    if not log:
        Tk().withdraw()  # hide TK window
        log = filedialog.askopenfile().name
        utils.config_save(log)

    with open(log) as file:
        log_lines = [l.strip() for l in file]
        sessions = get_sessions(log_lines)

    for session in sessions:
        print(session)


    sum = timedelta()
    for session in sessions:
        sum += session.duration

    print('summed duration:', sum)



    ui.show(sessions)

    input()  # keep console from closing




if __name__ == "__main__":
    main()
