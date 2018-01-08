## What is it?
- Simple utility to interpret data from [xmr-stak](https://github.com/fireice-uk/xmr-stak) miner log files
- Designed to group logged data into "sessions"
- One "session" is single xmr-stak.exe run (for now, this may change)

## Works (what it outputs so far):
- Session start time
- Session duration
- Session avarage H/s

## Todo:
- UI
- Merge sessions within certain time span

## Usage:
1. download log_reader.exe
2. run
3. when asked for file, point to xmr-stak log file


## How it looks like?
Below is the result of feeding it with log.txt (example log file available in this repo)

![](screenshot.JPG)
