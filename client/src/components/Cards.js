import React from "react";
import "./Cards.css";
import CardItem from "./CardItem";

function Cards() {
  return (
    <div className="cards">
      <h1>Check out our Team's EPIC Features!</h1>
      <div className="cards__container">
        <div className="cards__wrapper">
          <ul className="cards__items">
            <CardItem
              src="images/img-9.jpg"
              text="Run the Code for Yourself in a Beautifully Desiged Interface"
              label="RUN CODE"
              path="/services"
            />
            <CardItem
              src="images/img-gladiator.jpg"
              text="Check the Exclusive New Release: GLADIATOR"
              label="GAME"
              path="/services"
            />
          </ul>
          <ul className="cards__items">
            <CardItem
              src="images/img-3.jpg"
              text="Set Sail in the Atlantic Ocean visiting Uncharted Waters"
              label="Mystery"
              path="/services"
            />
            <CardItem
              src="images/img-knowledge.jpg"
              text="Learn about the Intricacies behind ANNs and PSO"
              label="KNOWLEDGE"
              path="/products"
            />
            <CardItem
              src="images/img-team.jpg"
              text="Meet the Team behind this Incredible Project"
              label="WHO WE ARE"
              path="/sign-up"
            />
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Cards;
