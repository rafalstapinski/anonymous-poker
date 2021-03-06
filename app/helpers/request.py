import web
import helpers as Help

class Request:

    @staticmethod
    def new_route():
        web.header('Content-Type', 'text/html')
        web.header('Access-Control-Allow-Origin', '*')
        if web.cookies().get('api') is None:
            web.setcookie('api', Help.Config.get()['api']['url'])
