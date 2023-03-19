Connexion - microservice boilerplate / starter project
==============

Quickstart project for a [Connexion](https://github.com/spec-first/connexion) based microservice (OpenAPI 3.0)

```bash
$ pip install -r requirements.txt
$ python microservice.py
```

Swagger UI available on: http://localhost:8080/openapi/ui/ 

For OAuth2, You must edit `openapi.yaml` and set `x-tokenInfoUrl` or `x-tokenInfoFunc`

```yaml
components:
  securitySchemes:
    oauth2:
      type: oauth2
      #      x-tokenInfoUrl: http://localhost:7979/tokeninfo
      #      or set TOKENINFO_URL environment variable

      #      x-tokenInfoFunc: api.auth.token_info
      #      or set TOKENINFO_FUNC environment variable
      flows:
        implicit:
          authorizationUrl: https://example.com/oauth2/dialog
          # the token info URL is hardcoded for our mock_tokeninfo.py script
          # you can also pass it as an environment variable TOKENINFO_URL
          scopes:
            uid: Unique identifier of the user accessing the service.
```


