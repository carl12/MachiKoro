
import webapp2
import jinja2
import os

# template_dir = os.path.join(os.path.dirname(__file__),'templates')
template_dir = os.path.dirname(__file__)
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape=True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a,**kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(**params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        self.render("MachiKoro.html")

# class MainPage(webapp2.RequestHandler):
#     def get(self):
#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.write('Hello, World!2')


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)


# class FrontPage(Handler):
#     def get(self):
#         self.render("MachiKoro.html")





# front_page = [('/', FrontPage)]

# app = webapp2.WSGIApplication(front_page, debug=True)
