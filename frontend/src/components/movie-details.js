import React, { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faStar } from "@fortawesome/free-solid-svg-icons";

function MovieDetails(props) {
  const [highlighted, setHighlighted] = useState(-1);

  let mov = props.movie

  const highlightRate = (high) => {
    setHighlighted(high);
  };

  const rateClicked = (rate) => {
    fetch(`http://127.0.0.1:8000/api/movies/${mov.id}/rate_movie/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token ebfb149ef3361f9006321dc54a723b485b0b2dee",
      },
      body: JSON.stringify({ stars: rate + 1 }),
    })
      .then(() => getDetails())
      .catch((error) => console.log(error));
  };

  const getDetails = () => {
    fetch(`http://127.0.0.1:8000/api/movies/${mov.id}/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token ebfb149ef3361f9006321dc54a723b485b0b2dee",
      },
    })
      .then((resp) => resp.json())
      .then((resp) => props.updateMovie(resp))
      .catch((error) => console.log(error));
  };

  return (
    <React.Fragment>
      {mov ? (
        <div>
          <h1>{mov && mov.title}</h1>
          <p>{mov && mov.description}</p>
          <FontAwesomeIcon
            icon={faStar}
            className={mov.avg_ratings > 0 ? "orange" : ""}
          />
          <FontAwesomeIcon
            icon={faStar}
            className={mov.avg_ratings > 1 ? "orange" : ""}
          />
          <FontAwesomeIcon
            icon={faStar}
            className={mov.avg_ratings > 2 ? "orange" : ""}
          />
          <FontAwesomeIcon
            icon={faStar}
            className={mov.avg_ratings > 3 ? "orange" : ""}
          />
          <FontAwesomeIcon
            icon={faStar}
            className={mov.avg_ratings > 4 ? "orange" : ""}
          />
          ({mov.no_of_ratings})
          <div className="rate-container">
            <h2>Rate it</h2>
            {[...Array(5)].map((e, i) => {
              return (
                <FontAwesomeIcon
                  key={i}
                  icon={faStar}
                  className={highlighted > i - 1 ? "purple" : ""}
                  onMouseEnter={(evt) => highlightRate(i)}
                  onMouseLeave={(evt) => highlightRate(-1)}
                  onClick={(evt) => rateClicked(i)}
                />
              );
            })}
          </div>
        </div>
      ) : null}
    </React.Fragment>
  );
}

export default MovieDetails;
