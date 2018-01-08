from datetime import datetime


def interpret_groups(groups):
    for group in groups:
        for line in group:
            # find first date in group
            date_start = line.find("[")
            date_end = line.find("]")
            if date_start > -1 and date_end > -1:
                session_start = datetime.strptime(line[date_start+1:date_end], '%Y-%m-%d %H:%M:%S')
                break

        for line in reversed(group):
            # find first date in group
            date_start = line.find("[")
            date_end = line.find("]")
            if date_start > -1 and date_end > -1:
                session_last = datetime.strptime(line[date_start + 1:date_end], '%Y-%m-%d %H:%M:%S')
                break

        duration = session_last - session_start
        print(duration)


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
    log = "log.txt"
    with open(log) as file:
        lines = [l.strip() for l in file]

    groups = group_lines(lines)

    interpret_groups(groups)


if __name__ == "__main__":
    main()
