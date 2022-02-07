import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Redirect } from "react-router-dom";
import "./App.css";
import Login from "./components/login";
import Register from "./components/register";
import MovieList from "./components/movie-list";
import MovieDetails from "./components/movie-details";

// function App() {
//   return (
//     <div className="App">
//       <BrowserRouter>
//         <Route exact path="/">
//           <Redirect to="/sign-in"></Redirect>
//         </Route>
//         <Route exact path="/sign-in" component={Login} />
//         <Route exact path="/sign-up" component={Register} />
//       </BrowserRouter>
//     </div>
//   );
// }

function App() {
  const [movies, setMovie] = useState([]);
  const [selectedMovie, setSelectedMovie] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/movies/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token ebfb149ef3361f9006321dc54a723b485b0b2dee",
      },
    })
      .then((resp) => resp.json())
      .then((resp) => setMovie(resp))
      .catch((error) => console.log(error));
  }, []);

  const movieClicked = (movie) => {
    setSelectedMovie(movie);
  };

  // this funciton will trigger when we pass information
  const loadMovie = (movie) => {
    setSelectedMovie(movie);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Movie Rater</h1>
      </header>
      <div className="layout">
        <MovieList movies={movies} movieClicked={movieClicked} />
        <MovieDetails movie={selectedMovie} updateMovie={loadMovie} />
      </div>
    </div>
  );
}

// <Route exact path="/register" component={Login} />
// <Login />
export default App;
