import React from "react";
import "./Cards.css";
import CardItem from "./CardItem";

function Cards() {
  return (
    <div className="cards">
      <div className="cards__container">
        <div className="cards__wrapper">
          <ul className="cards__items">
            <CardItem
              src="images/img-runcode.jpg"
              text="Run the Code for Yourself in a Beautifully Desiged Interface"
              path="/regular"
            />
            <CardItem
              src="images/img-team.jpg"
              text="Meet the Team behind this Remarkable Venture"
              path="/meet-team"
            />
            <CardItem
              src="images/img-approach.jpg"
              text="Our Approach to Going Above and Beyond"
              path="/approach"
            />
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Cards;
