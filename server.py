import argparse
from app.Controllers.Server import Server

parser = argparse.ArgumentParser(description='Start the server')
parser.add_argument('start', help='Start server instance on this machine')

args = parser.parse_args()
if args.start == 'start':
    print("[STARTING] server is starting...")
    init = Server()
    init.start()
else:
    print("Unkown argument passed as argument")
