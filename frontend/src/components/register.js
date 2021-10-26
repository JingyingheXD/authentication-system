import React, { Component } from "react";

class Register extends Component {
  state = {
    credentials: {
      username: "",
      password: "",
    },
  };

  register = (event) => {
    const { username, password } = this.state.credentials;
    fetch("http://127.0.0.1:8000/api/sign-up/", {
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
        if (resp["id"]) {
          alert("Success register!");
        } else {
          if (resp["username"]) {
            console.error("username error", resp["username"]);
            alert(resp["username"]);
          }
          if (resp["password"]) {
            console.error("password error", resp["password"]);
            alert(resp["password"]);
          }
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
        <h1>Sign up</h1>

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
        <button onClick={this.register}>Sign up</button>
      </div>
    );
  }
}

export default Register;
