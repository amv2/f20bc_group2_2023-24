import React from "react";
import Navbar from "./components/Navbar";
import "./App.css";
import Home from "./components/pages/Home";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Regular from "./components/pages/Regular";
import MeetTeam from "./components/pages/MeetTeam";
import Approach from "./components/pages/Approach";
import Footer from "./components/Footer";

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/regular" component={Regular} />
          <Route path="/meet-team" component={MeetTeam} />
          <Route path="/approach" component={Approach} />
        </Switch>
        <Footer />
      </Router>
    </>
  );
}

export default App;
