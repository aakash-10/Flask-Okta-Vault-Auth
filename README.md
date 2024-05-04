# Flask Authentication App with Okta and HashiCorp Vault

This Flask web application uses OpenID Connect (OIDC) for authentication with Okta and securely manages secrets using HashiCorp Vault. It demonstrates a basic implementation of user authentication flow within a Flask application.

## Features

- **User Authentication**: Uses Okta as the identity provider for authenticating users.
- **Secrets Management**: Utilizes HashiCorp Vault to securely store and access sensitive data such as client IDs and client secrets.

## Prerequisites

Before you begin, make sure you have the following installed:
- Python 3.8 or higher
- Flask
- Authlib
- hvac (HashiCorp Vault API client)
- A running instance of HashiCorp Vault
- An Okta Developer account

## Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aakash-10/Flask-Okta-Vault-Auth
   cd your-repository

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Configure environment variables**:
   ```bash
   FLASK_APP=app.py
   FLASK_ENV=development
   VAULT_URL=http://127.0.0.1:8200
   VAULT_TOKEN=your_vault_token_here

3. **Run the Flask Application**:
   ```bash
   flask run / python app.py
  
## Usage

After starting the application, navigate to http://localhost:5000 to access the main page. Click on the login link to authenticate via Okta. The application will handle the OAuth flow and redirect to the callback URL where the access token will be shown.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

Thanks to Okta for identity management and authentication.
Thanks to HashiCorp for the Vault product that securely manages secrets.



  


