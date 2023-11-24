import React from "react";
import "./Slider.css";

function Results(props) {
  return (
    <>
      <li className="cards__item">
        <div className="cards__item__link">
          <div className="cards__item__info">
            <div className="slider-card">
              <div>
                <div>
                  <p>Accuracy: {props.accuracy} </p>
                </div>
                <div>
                  <p>Elapsed Time (s): {props.time}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>
    </>
  );
}

export default Results;
