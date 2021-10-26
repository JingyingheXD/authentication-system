# API Documentation

This API documentation of authentication system includes Sign up and Sign in with emails and paswords.

## 1. Sign Up

Users register with `username` and `password`, and generate `auth_token`.

`username` should be an email format.

`password` should contain at least 8 characters including at least 1 alphabet, and should not be common password, such as 'a12345678'.

`auth_token` is generated when a new user is created, and used for authentication.

### Request

| Method | URL           |
| ------ | ------------- |
| POST   | /api/sign-up/ |

| Type | Params   | Values |
| ---- | -------- | ------ |
| POST | username | string |
| POST | password | string |

### Response

| Status          | Response                                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 201 CREATED     | {"id": \<id>, "username": \<username>} <br> \<id>(int) - user ID <br>                                                                                                                                                                                                                                                                                                       |
| 400 BAD_REQUEST | {"username":["This field may not be blank.", "A user with that username already exists.", "Enter a valid email address."] <br> "password":[ "This field may not be blank.", "['This password is too short. It must contain at least 8 characters.']", "['This password is entirely numeric.']", "['This password is too short. It must contain at least 8 characters.']" ]} |

<br></br>

## 2. Sign In

Authenticate the user with `username` and `password`, and obtain `auth_token`.

### Request

| Method | URL    |
| ------ | ------ |
| POST   | /auth/ |

| Type | Params   | Values |
| ---- | -------- | ------ |
| POST | username | string |
| POST | password | string |

### Response

| Status          | Response                                                                                       |
| --------------- | ---------------------------------------------------------------------------------------------- |
| 200 OK          | { "token": \<token> } <br> \<token>(string) - user token <br>                                  |
| 400 BAD_REQUEST | { "username": ["This field may not be blank."], "password": ["This field may not be blank."] } |
| 400 BAD_REQUEST | { "non_field_errors": ["Unable to log in with provided credentials."] }                        |
