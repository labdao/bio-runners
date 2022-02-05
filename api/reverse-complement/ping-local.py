
#
# Reverse Complement
# - Call this like a normal API / serverless endpoint, with POST or GET (examples provided)
# - this is mostly for testing!
# - follow the async (index.py) use case for production
# 

from typing import Optional
from fastapi import FastAPI, File, Form
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests

from Bio.Seq import Seq
import json

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Input(BaseModel):
    sequence: str




# GET example
# curl -X GET http://localhost:4500/api/reverse-complement/ping
# curl -X GET http://localhost:4500/api/reverse-complement/ping?bountyId=rec5T6CoaPeTPoLyH

@app.get("/api/reverse-complement/ping-local")
async def ping(bountyId: str):
    if bountyId:
        r = requests.get('http://localhost:4502/api/v0/bounties/'+bountyId, verify=False)
    else:
        # r = requests.get('http://localhost:4502/api/v0/bounties/latest?workflow=reverse-complement')
        r = requests.get('http://localhost:4502/api/v0/bounties/latest?workflow=reverse-complement', verify=False)
    bounty = r.json()
    print('[Ping!]', bounty)
    settings = json.loads(bounty['Input'])
    sequence = settings['sequence']

    # actual thing
    seq = Seq(sequence)
    revcomp = str(seq.reverse_complement())

    # print('[Ping!] ----> sequence:', sequence)
    # print('[Ping!] ----> rev-comp:', revcomp)

    # post it as a submission
    output = { "Provider": 'reverse-complement-api', "Output": {"output":revcomp}, "Bounties": [bounty['Name']], "Notes": "Auto-submission by async endpoint" }

    headers = {"charset": "utf-8", "Content-Type": "application/json"}
    url = 'http://localhost:4502/api/v0/submissions/create'
    r = requests.post(url, json=output, headers=headers, verify=False)

    return {"msg": json.dumps(output)}









# implement IPFS in the future:

# import os
# from io import StringIO

# from http.server import BaseHTTPRequestHandler
# from http import HTTPStatus
# from urllib import parse
# from Bio.Seq import Seq
# import json
# import requests 
# from requests.structures import CaseInsensitiveDict

# from dotenv import load_dotenv
# load_dotenv()



# # https://gist.github.com/nitaku/10d0662536f37a087e1b

# def pin_JSON(jsondata):
#   url = os.getenv('ESTUARY_URL')

#   headers = CaseInsensitiveDict()
#   headers["Authorization"] = "Bearer " + os.getenv('ESTUARY_API')
#   headers["Accept"] = "application/json"
#   print('api:', os.getenv('ESTUARY_API'), 'url:', url, 'data:', jsondata)
#   files = {'data': ('file.json', jsondata)}

#   resp = requests.post(url, verify=False,
#     headers=headers, 
#     files=files
#     )

#   print('estuary response:', resp)
#   print('estuary response json:', resp.json())
#   return resp.json()


  



# class handler(BaseHTTPRequestHandler):
#   # Borrowing from https://gist.github.com/nitaku/10d0662536f37a087e1b
#   def _set_headers(self):
#       self.send_response(HTTPStatus.OK.value)
#       self.send_header('Content-type', 'application/json')
#       # Allow requests from any origin, so CORS policies don't
#       # prevent local development.
#       self.send_header('Access-Control-Allow-Origin', '*')
#       self.end_headers()
      

#   # cors / preflight
#   def do_OPTIONS(self):
#     self.send_response(200, "ok")
#     self.send_header('Access-Control-Allow-Credentials', 'true')
#     self.send_header('Access-Control-Allow-Origin', '*')
#     self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
#     self.send_header("Access-Control-Allow-Headers", "Accept, X-Requested-With, Content-type")
#     self.end_headers()



#   # def do_GET(self):
#   #   s = self.path
#   #   dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
#   #   self.send_response(200)
#   #   self.send_header('Content-type','text/plain')
#   #   self.send_header('Access-Control-Allow-Origin', '*')
#   #   self.end_headers()
#   #   if "name" in dic:
#   #       message = "Hello, " + dic["name"] + "!"
#   #   else:
#   #       message = "Hello, stranger!"
#   #   self.wfile.write(message.encode())
#   #   return



#   # POST echoes the message adding a JSON field
#   def do_POST(self):
#     length = int(self.headers.get('content-length'))
#     body = json.loads(self.rfile.read(length))
    
#     # add a property to the object, just to mess with data
#     seq = Seq(body['input'])
#     # print('input:', body, ' || seq:', seq, ' <> reverse: ', seq.reverse_complement(), ' translate: ', seq.translate())
#     body['output'] = str(seq.reverse_complement())

#     # pinres = pin_JSON(json.dumps(body).encode('utf-8'))
#     # body['pinres'] = pinres

#     # send the body back
#     self._set_headers()
#     self.wfile.write(json.dumps(body).encode('utf-8'))
    


