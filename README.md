autoaddtorrents to Transmission
===============================

If you download a large number of torrents and sort them into the appropriate directories (file system organization is the best media library), you will eventually end up your torrent files centrally located, but with your media scattered. This is all okay, until you reinstall. Suddenly, you realize that you have to readd all of those torrents, finding which directory they are in, and then choosing that directory when you add them.

Very time-consuming. But you really should do it, since seeding is good.

This program basically just automates that process, specifically for transmission. Just enable the remote interface in Transmission, then feed autoaddtorrents a bunch of torrent files and where to look for the data.

There are a number of options, all available via ./autoaddtorrents.py -h, and copied here for easy access:

    usage: autoaddtorrents.py [-h] [-d DIRECTORY] [-v] [-p PORT] [-c CONNECT]
                              [--paused]
                              torrents [torrents ...]

    Add torrents to transmission automatically

    positional arguments:
      torrents              Some torrent files

    optional arguments:
      -h, --help            show this help message and exit
      -d DIRECTORY, --directory DIRECTORY
                            directory to scan for media
      -v, --verbose         increase output verbosity
      -p PORT, --port PORT  port to connect to transmission
      -c CONNECT, --connect CONNECT
                            host to connect to
      --paused              add torrents as paused

NOTE: I can't guarantee that this won't destroy your data or anything, but all it really does is read in the torrents, search using `find`, then adds them to transmission. I suppose it could pollute your transmission database, but it only adds, and if you add `--paused`, shouldn't be an issue.
