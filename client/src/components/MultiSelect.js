import React from "react";
import "./Cards.css";

function MultiSelect(props) {
  return (
    <>
      <li className="cards__item">
        <div className="cards__item__link">
          <figure className="cards__item__pic-wrap" data-category={props.label}>
            <img
              className="cards__item__img"
              src={props.src}
              alt="Description"
            />
          </figure>
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
              <p>
                {props.selectionText}: {props.numName}
              </p>
            </div>
          </div>
        </div>
      </li>
    </>
  );
}

export default MultiSelect;
