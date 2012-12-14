import os
from fb_download import *
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
  auth_vals = get_authvals_csv('auth_keys.csv')
  auth_url = fb_oauth_init(auth_vals)
  return redirect(auth_url)
  
@app.route('/stats/')
def stats():
  auth_vals = get_authvals_csv('auth_keys.csv')
  access_token = fb_oauth_final(auth_vals)
  write_authvals_csv(auth_vals,'auth_keys.csv')
  friends_data = get_friends_fql(auth_vals)
  fflist = filter_friends(friends_data)
  output_str, num = extract_age_sex_str(fflist)
  return output_str

if __name__ == '__main__':
  # Bind to PORT if defined, otherwise default to 5000.
  port = int(os.environ.get('PORT', 5000))
#  app.debug=False
  app.run(host='0.0.0.0', port=port)