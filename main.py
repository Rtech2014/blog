import webapp2
import cgi

months = ['Janurary',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']


month_abbvs = dict((m[:3].lower(), m) for m in months)


def valid_month(user_month):
    if user_month:
        short_month = user_month[:3].lower()
        return month_abbvs.get(short_month)
    return True


def valid_day(user_day):
    if user_day and user_day.isdigit():
        user_day = int(user_day)
        if user_day > 0 and user_day <= 31:
            return user_day
    return True


def valid_year(user_year):
    if user_year and user_year.isdigit():
        user_year = int(user_year)
        if user_year > 1900 and user_year < 2020:
            return user_year
    return True


def escape_html(s):
    return cgi.escape(s, quote=True)
    return True

form = """
<form method='POST'>
 <h1>What is your birthday?</h1>
 <br>
 <label>Month
 <input type="text" name="month" value="%(month)s">
 </label>

 <label>day
 <input type="text" name="day" value="%(day)s">
 </label>

 <label>year
 <input type="text" name="year" value="%(year)s">
 </label>
 <div style="color: red;">%(error)s</div>
 <input type="submit">
</form>
"""


class MainHandler(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.write(form % {"error": error,
                                    "month": escape_html(month),
                                    "day": escape_html(day),
                                    "year": escape_html(year)})

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and year and day):
            self.write_form("Please enter a valid credentials",
                            user_month, user_day, user_year)
        else:
            self.redirect("/thanks")


class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks for that")

app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/thanks', ThanksHandler)],
                              debug=True)
