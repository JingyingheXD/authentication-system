import React, { Component } from "react";

class Login extends Component {
  state = {
    credentials: {
      username: "",
      password: "",
    },
  };

  login = (event) => {
    // console.log(this.state.credentials);
    const { username, password } = this.state.credentials;
    fetch("http://127.0.0.1:8000/auth/", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify({
        username: username,
        password: password,
      }),
    })
      .then((resp) => resp.json())
      .then((resp) => {
        // resp = resp.json();
        // console.log("resp", resp);
        if (resp["token"]) {
          alert("Success login!");
        } else if (resp["non_field_errors"]) {
          alert("Wrong password");
        } else if (resp["username"] && resp["password"]) {
          console.error("username error", resp["username"]);
          console.error("password error", resp["password"]);
          alert("Please input username and password!");
        } else if (resp["username"]) {
          console.error("username error", resp["username"]);
          alert("Please input username!");
        } else if (resp["password"]) {
          console.error("password error", resp["password"]);
          alert("Please input password!");
        }
      })
      .catch((error) => {
        console.error(error);
      });
  };

  inputChanged = (event) => {
    const cred = this.state.credentials;
    cred[event.target.name] = event.target.value;
    this.setState({ credentials: cred });
  };

  render() {
    return (
      <div>
        <h1>Sign in</h1>

        <label>
          Username:
          <input
            type="text"
            name="username"
            value={this.state.credentials.username}
            onChange={this.inputChanged}
          />
        </label>
        <br />
        <label>
          Password:
          <input
            type="password"
            name="password"
            value={this.state.credentials.password}
            onChange={this.inputChanged}
          />
        </label>
        <br />
        <button onClick={this.login}>Sign in</button>
        <a href="../sign-up">Go to Sign Up</a>
      </div>
    );
  }
}

export default Login;
