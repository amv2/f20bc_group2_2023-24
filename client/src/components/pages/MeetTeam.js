import React from "react";
import "./MeetTeam.css";
import CardItem from "../CardItem";

export default function MeetTeam() {
  const description1 =
    "Tanisha is a 4th year student specializing in Robotics, Autonomous and Interactive Systems with experience working in several successful businesses.";
  const description2 =
    "Moses is in the software business industry, while also studying Robotics, Autonomous and Interactive Systems as a 4th year student.";

  return (
    <div>
      <div className="hero-container">
        <video src="/videos/video-1.mp4" autoPlay loop muted />
        <h1>A Team that Exceeds Expectations</h1>
      </div>
      <div className="cards">
        <div className="cards__container">
          <div className="cards__wrapper">
            <ul className="cards__items">
              <CardItem
                src="images/img-tanisha.jpg"
                text={description1}
                path="/meet-team"
              />
              <CardItem
                src="images/img-moses.jpg"
                text={description2}
                path="/meet-team"
              />
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
