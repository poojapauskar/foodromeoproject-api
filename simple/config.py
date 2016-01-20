# config.py

from authomatic.providers import oauth2, oauth1

CONFIG = {
    
    # 'tw': { # Your internal provider name
        
    #     # Provider class
    #     'class_': oauth1.Twitter,
        
    #     # Twitter is an AuthorizationProvider so we need to set several other properties too:
    #     'consumer_key': '########################',
    #     'consumer_secret': '########################',
    # },
    
    'fb': {
           
        'class_': oauth2.Facebook,
        
        # Facebook is an AuthorizationProvider too.
        'consumer_key': '552415814932341',
        'consumer_secret': '8d1fa735747302d7b8258e08f9f2fb2e',
        
        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream'],
    },
    
    # 'oi': {
           
    #     # OpenID provider dependent on the python-openid package.
    #     'class_': openid.OpenID,
    # }
}