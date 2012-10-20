autoaddtorrents to Transmission
===============================

If you download a large number of torrents and sort them into the appropriate directories (file system organization is the best media library), you will eventually end up your torrent files centrally located, but with your media scattered. This is all okay, until you reinstall. Suddenly, you realize that you have to readd all of those torrents, finding which directory they are in, and then choosing that directory when you add them.

Very time-consuming. But you really should do it, since seeding is good.

This program basically just automates that process, specifically for transmission. Just enable the remote interface in Transmission, then feed autoaddtorrents a bunch of torrent files and where to look for the data.

Installation
------------

The script is just python, and should definitely work on OSX and Linux. Theoretically, it should work on Windows if you can figure out how to install `find`. All paths and such are OS-independent.

### Prerequisites

The script requires Python >= 2.7 (Not Python 3 yet), bencode, and transmission. The last two I recommend you install via [pip](http://www.pip-installer.org/en/latest/installing.html). Just `pip install bencode transmissionrpc`.

Tips
----

* Check your permissions. The script needs read permission for both the torrents and the data directory (and sub-directories). Whatever user transmission is running as needs write permission.
* I strongly suggest using `--paused`, if nothing else so that you can easily distinguish the added torrents. Transmission will verify the data, at which point you can start them safely.
* There is no problem with feeding it all the torrents at once except it will take a bit longer. Easiest way is to use -c/--copy to move the errored torrents to a new directory and then feed the script that.

Options
-------

There are a number of options, all available via ./autoaddtorrents.py -h, and copied here for easy access:

    usage: autoaddtorrents.py [-h] [-d DIRECTORY] [-c COPY] [-u USER]
                              [-p PASSWORD] [-v] [--port PORT] [--host HOST]
                              [--paused] [--debug]
                              torrents [torrents ...]

    Add torrents to transmission automatically

    positional arguments:
      torrents              Some torrent files

    optional arguments:
      -h, --help            show this help message and exit
      -d DIRECTORY, --directory DIRECTORY
                            directory to scan for media
      -c COPY, --copy COPY  directory to copy errored files to
      -u USER, --user USER  username for transmission
      -p PASSWORD, --password PASSWORD
                            password for transmission
      -v, --verbose         increase output verbosity
      --port PORT           port to connect to transmission
      --host HOST           host to connect to
      --paused              add torrents as paused
      --debug               all info

NOTE: I can't guarantee that this won't destroy your data or anything, but all it really does is read in the torrents, search using `find`, then adds them to transmission. I suppose it could pollute your transmission database, but it only adds, and if you add `--paused`, shouldn't be an issue.
