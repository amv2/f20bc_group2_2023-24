import React from "react";
import "./Slider.css";

function Slider(props) {
  return (
    <>
      <li className="cards__item">
        <div className="cards__item__link">
          <div className="cards__item__info">
            <div className="slider-card">
              <label>{props.name}</label>
              <input
                type="range"
                id={`slider${props.label}`}
                min={props.min}
                max={props.max}
                step={props.step}
                value={props.numValue}
                onChange={props.handleNumChange}
              />
              <p>Value: {props.numValue}</p>
            </div>
          </div>
        </div>
      </li>
    </>
  );
}

export default Slider;
