from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import hvac
import os
from dotenv import load_dotenv
load_dotenv()  

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET_KEY'

# Initialize Vault client
vault_client = hvac.Client(url=os.getenv('VAULT_URL'))
vault_client.token = os.getenv('VAULT_TOKEN')
okta_credentials = vault_client.secrets.kv.read_secret_version(path='okta_auth')['data']['data']
client_id = okta_credentials['client_id']
client_secret = okta_credentials['client_secret']

# OAuth setup
oauth = OAuth(app)
okta = oauth.register(
    'okta',
    client_id=client_id,
    client_secret=client_secret,
    authorize_url='https://dev-00169682.okta.com/oauth2/default/v1/authorize',
    authorize_params=None,
    access_token_url='https://dev-00169682.okta.com/oauth2/default/v1/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='http://localhost:5000/callback',
    server_metadata_url='https://dev-00169682.okta.com/oauth2/default/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid profile email'}
)

@app.route('/')
def hello():
    return 'Welcome! <a href="/login">Login</a>'

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return okta.authorize_redirect(redirect_uri)

@app.route('/callback')
def authorize():
    token = okta.authorize_access_token()
    # you can save this token and the user info to the session
    session['token'] = token
    return 'Authorization complete. Access token saved.'

if __name__ == '__main__':
    app.run(debug=True)
