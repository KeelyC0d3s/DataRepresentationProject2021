# DataRepresentationProject2021

## Installation Guide

### Setting up the database
1. Login to MySQL client
2. Run the following commands 
   1. `source scripts/1_create_database.sql`
   2. `source scripts/2_create_tables.sql`
   3. `source scripts/3_create_data.sql`

Please update the values in dbconfig.py with your own database username and password

### Setting up the server

#### virtual environment
1. Creating a virtual environment`pip3 -m venv venv`
2. Activating virtual environment `source venv/bin/activate`
3. Deactivating virtual environment`deactivate`

#### Install dependencies
`pip3 install -r requirements.txt`

#### Running the server
`python3 server.py`

### References

#### Libraries
1. [Bcrypt](https://zetcode.com/python/bcrypt/)
2. [Bootstrap Docs](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
3. [jq](https://shapeshed.com/jq-json/)
4. [jquery](https://code.jquery.com/)
5. [flask-login](https://flask-login.readthedocs.io/en/latest/#configuring-your-application)

#### Guides
1. https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask
2. https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
3. https://flask.palletsprojects.com/en/2.0.x/tutorial/views/
4. https://stackabuse.com/how-to-get-and-parse-http-post-body-in-flask-json-and-form-data/
5. https://getbootstrap.com/docs/5.0/examples/
6. https://getbootstrap.com/docs/4.0/utilities/display/
7. https://getbootstrap.com/docs/5.0/forms/overview/
8. https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/6
9. https://flask-login.readthedocs.io/en/latest/#configuring-your-application
10. https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions
11. https://css-tricks.com/scale-svg/
12. https://www.w3schools.com/sql/sql_update.asp

#### Troubleshooting
1. https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html
2. https://stackoverflow.com/questions/26701538/how-to-filter-an-array-of-objects-based-on-values-in-an-inner-array-with-jq
3. https://stackoverflow.com/questions/68146903/importing-multi-level-json-arrays-into-rdms-by-using-jq-to-create-sql-insert-sta
4. https://superuser.com/questions/1506499/surround-field-from-json-with-quotes
5. https://dev.mysql.com/doc/refman/8.0/en/insert-on-duplicate.html
6. https://stackoverflow.com/questions/171027/add-table-row-in-jquery
7. https://careerkarma.com/blog/javascript-string-interpolation/
8. https://stackoverflow.com/questions/6763006/how-to-get-the-tbody-element-of-a-table-using-jquery/6763036
9. https://stackoverflow.com/questions/25594893/how-to-enable-cors-in-flask
10. https://stackoverflow.com/questions/30011170/flask-application-how-to-link-a-javascript-file-to-website
11. https://stackoverflow.com/questions/42871046/using-flask-url-for-in-button-onclick-location-href-redirect-leads-to-method-no
12. https://stackoverflow.com/questions/5570747/jquery-posting-json
13. https://stackoverflow.com/questions/10931836/should-i-use-done-and-fail-for-new-jquery-ajax-code-instead-of-success-and
14. https://stackoverflow.com/questions/61966894/flask-problem-runtimeerror-the-session-is-unavailable-because-no-secret-key-wa
15. https://stackoverflow.com/questions/19532372/whats-the-point-of-the-is-authenticated-method-used-in-flask-login
16. https://stackoverflow.com/questions/19302122/how-to-put-a-text-beside-the-image
17. https://stackoverflow.com/questions/30056622/how-to-iterate-over-a-list-of-list-in-jinja
18. https://stackoverflow.com/questions/45149420/pass-variable-from-python-flask-to-html-in-render-template
19. https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
20. https://stackoverflow.com/questions/5191503/how-to-select-the-last-record-of-a-table-in-sql

### Possible future improvements
1. https://towardsdatascience.com/protect-your-api-via-input-validation-in-python-3-data-class-edefa5e280df
2. https://medium.com/@joegoosebass/easy-authentication-with-flask-267c35b803dd
3. https://realpython.com/token-based-authentication-with-flask/#jwt-setup
4. https://jwt.io/introduction/
