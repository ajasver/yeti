#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib/apiclient'))

import datetime
import webapp2
import jinja2
from apiclient import APIClient


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainPage(webapp2.RequestHandler):
    def get(self):
        
        weekend_str = self.this_weekend()
        
        template_values = {
            'weekend_str': weekend_str,
        }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

    def this_weekend(self):
        # return the date string for this weekend 
        # as "Month day - Month day" e.g. on 2/27/13
        # this_weekend returns "Mar 2 - Mar 3" 
        
        today = datetime.datetime.today()
        today_day = datetime.date.weekday(today)
        
        to_saturday = 5-today_day
        
        this_sat = today+datetime.timedelta(days=to_saturday)
        this_sat_str = "%s %s" % (this_sat.strftime("%b"), this_sat.day)
        
        this_sun = today+datetime.timedelta(days=to_saturday+1)
        this_sun_str = "%s %s" % (this_sun.strftime("%b"), this_sun.day)
        
        return "%s - %s" % (this_sat_str,this_sun_str)
        

app = webapp2.WSGIApplication([('/', MainPage)],
                                      debug=True)
        
        