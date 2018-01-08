from datetime import datetime
from tkinter import Tk, filedialog


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
            if line.find('Result accepted by the pool') < 0:
                continue

            date_start = line.find('[')
            date_end = line.find(']')
            if date_start > -1 and date_end > -1:
                session_end = datetime.strptime(line[date_start + 1:date_end], '%Y-%m-%d %H:%M:%S')
                break

        if session_start and session_end:
            duration = session_end - session_start
        else:
            duration = "info not found"

        print('--> Started at:', session_start, '  Session Duration: ', duration)

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
