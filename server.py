from waitress import serve

from suorganizer.wsgi import application

if __name__ == '__main__':
	serve(application, port='8080')