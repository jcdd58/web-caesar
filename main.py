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

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">Caesar</a>
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""



class MainHandler(webapp2.RequestHandler):
    def get(self):
        encrypted = self.request.get("encrypted")

        ceasar_form = """
            <form method="POST">
                <label for="rot">Rotation: </label>
                <input type="text" name="rot" id="rot"><br><br>
                <label for="text">Text to encrypt:</label><br>
                <textarea name="text" id="text" style="height:200px;width:400px;">{}</textarea><br><br>
                <input type="submit" value="Submit">
            </form>
        """.format(encrypted)

        self.response.write(page_header + ceasar_form + page_footer)

    def post(self):
        def alphabet_position(char):
        	if char.isupper():
        		return ord(char) - 65
        	if char.islower():
        		return ord(char) - 97

        def rotate_character(char, rot):
        	if not char.isalpha():
        		return char
        	if char.isupper():
        		return chr(((alphabet_position(char) + rot) % 26) + 65)
        	if char.islower():
        		return chr(((alphabet_position(char) + rot) % 26) + 97)

        def encrypt(text,rot):
        	encrypted_text = ""
        	for char in text:
        		if char == " ":
        			encrypted_text += char
        		else: encrypted_text += rotate_character(char,int(rot))
        	return encrypted_text

        rot = self.request.get("rot")
        text = self.request.get("text")

        encrypted_text = encrypt(text, rot)

        self.redirect("/?encrypted={}".format(encrypted_text))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
