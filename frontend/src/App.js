import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Redirect } from "react-router-dom";
import "./App.css";
import Login from "./components/login";
import Register from "./components/register";
import MovieList from "./components/movie-list";
import MovieDetails from "./components/movie-details";
import MovieForm from "./components/movie-form";

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
  const [editedMovie, setEditedMovie] = useState(null);

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

  // this funciton will trigger when we pass information
  const loadMovie = (movie) => {
    setSelectedMovie(movie);
    setEditedMovie(null);
  };

  const editClicked = (movie) => {
    setEditedMovie(movie);
    setSelectedMovie(null);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Movie Rater</h1>
      </header>
      <div className="layout">
        <MovieList
          movies={movies}
          movieClicked={loadMovie}
          editClicked={editClicked}
        />
        <MovieDetails movie={selectedMovie} updateMovie={loadMovie} />
        <MovieForm movie={editedMovie} />
      </div>
    </div>
  );
}

// <Route exact path="/register" component={Login} />
// <Login />
export default App;
