#!/usr/bin/env python
import transmissionrpc, bencode, sys, subprocess, os, argparse

parser = argparse.ArgumentParser(description="Add torrents to transmission automatically")
parser.add_argument('torrents', nargs='+', help="Some torrent files")
parser.add_argument('-d', '--directory', help="directory to scan for media", action="store", default=os.getcwd())
parser.add_argument('-u', '--user', help="username for transmission", action="store", default=None)
parser.add_argument('-p', '--password', help="password for transmission", action="store", default=None)
parser.add_argument('-v', '--verbose', help="increase output verbosity", action="store_true")
parser.add_argument('--port', help="port to connect to transmission", action="store", type=int, default=9091)
parser.add_argument('--host', help="host to connect to", action="store", default="localhost")
parser.add_argument('--paused', help="add torrents as paused", action="store_true", default=False)
args = parser.parse_args()

try:
  trans = transmissionrpc.Client(args.host, args.port)
except transmissionrpc.TransmissionError:
  print "Could not connect to transmission."
  sys.exit(1)

error = False
for torrent in args.torrents:
  nicename = os.path.basename(torrent)
  try:
    torrentfile = open(torrent, "rb")
  except IOError:
    print "Torrent %s could not be accessed" % nicename
    error = True
    continue
  try:
    metadata = bencode.bdecode(torrentfile.read()) # Torrent is base64 encoded.
  except bencode.BTFailure:
    print "%s does not appear to be a valid torrent" % nicename
    error = True
    continue
  if args.verbose: print "Torrent %s loaded" % torrent

  ftype = 'f'
  if 'files' in metadata['info'].keys():
    ftype = 'd'
  try:
    results = subprocess.check_output(['find', args.directory, '-type', ftype, '-name', metadata['info']['name']])
  except subprocess.CalledProcessError:
    error = True
    print "Error finding files. Probably not a valid search directory."
    continue

  if args.verbose: print "Search results: \n%s" % results

  list = results.split("\n")[:-1]
  if len(list) == 1:
    try:
      trans.add_uri(os.path.join(os.getcwd(), torrent),download_dir=os.path.dirname(list[0]),paused=args.paused)
    except transmissionrpc.TransmissionError:
      print "Error adding %s. Perhaps it is already added." % nicename
  elif len(list) == 0:
    print "No results found for torrent %s" % nicename
    error = True
  else:
    print "Multiple possibilities found for %s:" % nicename
    for loc in list:
      print "- " + loc
    error = True

if error: exit(2)

