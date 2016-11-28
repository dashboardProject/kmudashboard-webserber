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
import webapp2

from google.appengine.api import users
import configs
from utils.userNgroupQuery import selectUser
from controller.sign import Sign_Up, Manage_User_Data, test

class Main(webapp2.RequestHandler):
    # access mainpage
    def get(self):
        user = users.get_current_user()

        if user and selectUser(user.email()).count is 1:
            # add query and template data

            self.response.write(configs.JINJA_ENV.get_template(configs.MAIN_PAGE).render())

        else:
            self.response.write(configs.JINJA_ENV.get_template(configs.MAIN_PAGE).render())

    # sign-in request
    def post(self):
        user = users.get_current_user()

        if user and selectUser(user.user_id()).count is 0:
            self.response.write(configs.JINJA_ENV.get_template(Sign_Up).render())

        else:
            self.redirect(users.create_login_url(self.request.uri))


class Tutorial(webapp2.RequestHandler):
    # access mainpage
    def get(self):
        # add query and template data
        self.response.write(configs.JINJA_ENV.get_template(configs.TUTORIAL_PAGE).render())


class Management(webapp2.RequestHandler):
    # access mainpage
    def get(self):
        # add query and template data
        self.response.write(configs.JINJA_ENV.get_template(configs.MANAGEMENT_PAGE).render())

class ManagementGroup(webapp2.RequestHandler):
    # access mainpage
    def get(self):
        # add query and template data
        self.response.write(configs.JINJA_ENV.get_template(configs.MANAGEMENT_GROUP).render())


class ManagementDevice(webapp2.RequestHandler):
    # access mainpage
    def get(self):
        # add query and template data
        self.response.write(configs.JINJA_ENV.get_template(configs.MANAGEMENT_DEVICE).render())


class ManagementContents(webapp2.RequestHandler):
    # access mainpage
    def get(self):
        # add query and template data
        self.response.write(configs.JINJA_ENV.get_template(configs.MANAGEMENT_CONTENTS).render())


app = webapp2.WSGIApplication([webapp2.Route('/', Main, name='main'),
                               webapp2.Route('/signup', Sign_Up, name='signup'),
                               webapp2.Route('/updateuserinfo', Manage_User_Data),
                               webapp2.Route('/tutorial', Tutorial),
                               webapp2.Route('/management', Management),
                               webapp2.Route('/management/group', ManagementGroup),
                               webapp2.Route('/management/device', ManagementDevice),
                               webapp2.Route('/management/contents', ManagementContents),
                               ],debug=True)

