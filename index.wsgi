def application(environ, start_response):
	start_response('200 ok', [('content-type', 'text/plain')])
	return ['<html><head><meta http-equiv=Content-Type content="text/html;charset=utf-8"><meta property="wb:webmaster" content="96ba2a53451a5423" /></head><body>Hello, welcome to weime</body></html>']
