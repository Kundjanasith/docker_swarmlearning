import server
import sys

x = sys.argv[1]

server.start_server(x,config={"num_rounds": 10})