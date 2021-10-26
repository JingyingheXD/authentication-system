import React from "react";
import { BrowserRouter, Route, Redirect } from "react-router-dom";
import "./App.css";
import Login from "./components/login";
import Register from "./components/register";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Route exact path="/">
          <Redirect to="/sign-in"></Redirect>
        </Route>
        <Route exact path="/sign-in" component={Login} />
        <Route exact path="/sign-up" component={Register} />
      </BrowserRouter>
    </div>
  );
}

// <Route exact path="/register" component={Login} />
// <Login />
export default App;
