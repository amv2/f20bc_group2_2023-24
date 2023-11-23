import React, { useEffect } from "react";
import "./MeetTeam.css";
import PersonCard from "../PersonCard";

export default function MeetTeam() {
  const title1 = "Tanisha Kasar";
  const title2 = "Moses Varghese";
  const description1 =
    "Tanisha is a 4th year student specializing in Robotics, Autonomous and Interactive Systems with experience working in several successful businesses.";
  const description2 =
    "Moses is in the software business industry, while also studying Robotics, Autonomous and Interactive Systems as a 4th year student.";

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

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
              <PersonCard
                src="images/img-tanisha.jpg"
                title={title1}
                text={description1}
                path="/meet-team"
              />
              <PersonCard
                src="images/img-moses.jpg"
                title={title2}
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
