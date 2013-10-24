import httplib

while(True):
	conn = httplib.HTTPConnection('localhost',5000)
	r1 = conn.request("POST", "/facebook/like/1")
	res = conn.getresponse()
	print res.status, res.reason
	r2 = conn.request("POST", "/facebook/comment/1")
	res = conn.getresponse()
	print res.status, res.reason
	r3 = conn.request("POST", "/facebook/share/1")
	res = conn.getresponse()
	print res.status, res.reason
	r4 = conn.request("POST", "/twitter/hashtag/1")
	res = conn.getresponse()
	print res.status, res.reason
	r5 = conn.request("POST", "/twitter/mention/1")
	res = conn.getresponse()
	print res.status, res.reason
	
	