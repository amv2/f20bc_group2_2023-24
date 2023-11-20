import React from "react";
import Navbar from "./components/Navbar";
import "./App.css";
import Home from "./components/pages/Home";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Services from "./components/pages/Services";
import Products from "./components/pages/Products";
import SignUp from "./components/pages/SignUp";
import Gladiator from "./components/pages/Gladiator";
import MeetTeam from "./components/pages/MeetTeam";
import Learn from "./components/pages/Learn";

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/services" component={Services} />
          <Route path="/products" component={Products} />
          <Route path="/sign-up" component={SignUp} />
          <Route path="/gladiator" component={Gladiator} />
          <Route path="/meet-team" component={MeetTeam} />
          <Route path="/learn" component={Learn} />
        </Switch>
      </Router>
    </>
  );
}

export default App;
