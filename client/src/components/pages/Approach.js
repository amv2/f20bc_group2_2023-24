import React, { useEffect } from "react";
import "../../App.css";
import "../HeroSection.css";
import "../Cards.css";
import "./Approach.css";
import { Button } from "../Button";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCircleRight } from "@fortawesome/free-solid-svg-icons";

export default function Approach() {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <div>
      <div className="hero-container">
        <video src="/videos/video-2.mp4" autoPlay loop muted />
        <h1>To Infinity and Beyond</h1>
      </div>
      <div className="cards">
        <div className="cards__container">
          <div className="cards__wrapper">
            <p>
              As Robotics students, we knew our experience in code creation,
              especially on the frontend would be less than our competitors from
              Computer Science or even Master students. While most would see a
              setback, we saw opportunity. An opportunity to create something
              bigger and badder than anything ever seen before.
            </p>
            <p>
              It all started with the server-side. Rather than creating the
              implementation files and interface files together in a single
              directory, we decided to abstract the two into Client-side and
              Server-side.
            </p>
            <p>
              This approach requires significantly more intricacies as opposed
              to coding locally. But diamonds are forged under pressure, and we
              wanted diamonds.
            </p>
            <p>
              And the result is truly incredible. A beautiful and responsive
              interface that reacts to any screen size. Lively animations
              fashion the entire interface to come to life and absolutely
              stunning to look at.
            </p>
          </div>
          <div>
            <div className="hero-btns">
              <Button
                className="btns"
                buttonStyle="btn--primary"
                buttonSize="btn--large"
                onClick={console.log("hey")}
                linkTo="/regular"
              >
                See it in Action <FontAwesomeIcon icon={faCircleRight} />
              </Button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
