## this toy app serves up an HTTP endpoint result as part of the quicknode infra assessment.
## all we need is flask and it's pretty self-documenting - thanks, python!

## to serve me manually rather than via the systemd service, use:
## flask run 

from flask import Flask, redirect

# grab us an instance
quicknode_endpoint = Flask(__name__)

## define two URIs to serve -- a request to / ends up at /test because it's tidy and why not
@quicknode_endpoint.route("/")
def root():
	return redirect('/test')

@quicknode_endpoint.route("/test")
def test():
	return "329d4feb-c5c0-4de5-b10c-701b44fbec4f"