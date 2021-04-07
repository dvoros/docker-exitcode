# Catching OS signals and exiting with specific exit code for some:
#   SIGINT(2)   => 0
#   SIGTERM(15) => 0
#   SIGUSR1(10) => 1
#   SIGUSR2(12) => 2
#   SIGALRM(14) => 137
# Based on https://stackabuse.com/handling-unix-signals-in-python/

import signal
import os
import time
import sys


def receiveSignal(signalNumber, frame):
    print('Received signal:', signalNumber)

    if signalNumber == 2:
        sys.exit(0)
    if signalNumber == 10:
        sys.exit(1)
    if signalNumber == 12:
        sys.exit(2)
    if signalNumber == 15:
        sys.exit(0)
    if signalNumber == 14:
        sys.exit(137)


if __name__ == '__main__':
    # register the signals to be caught
    signal.signal(signal.SIGHUP, receiveSignal)
    signal.signal(signal.SIGINT, receiveSignal)
    signal.signal(signal.SIGQUIT, receiveSignal)
    signal.signal(signal.SIGILL, receiveSignal)
    signal.signal(signal.SIGTRAP, receiveSignal)
    signal.signal(signal.SIGABRT, receiveSignal)
    signal.signal(signal.SIGBUS, receiveSignal)
    signal.signal(signal.SIGFPE, receiveSignal)
    signal.signal(signal.SIGUSR1, receiveSignal)
    signal.signal(signal.SIGSEGV, receiveSignal)
    signal.signal(signal.SIGUSR2, receiveSignal)
    signal.signal(signal.SIGPIPE, receiveSignal)
    signal.signal(signal.SIGALRM, receiveSignal)

    # output current process id
    print('My PID is:', os.getpid())

    # wait in an endless loop for signals
    while True:
        print('Waiting for signals...')
        time.sleep(3)
