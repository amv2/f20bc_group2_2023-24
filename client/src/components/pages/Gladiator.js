// import React from "react";
// import "../../App.css";

// export default function Gladiator() {
//   return <h1 className="sign-up">GLADIATOR</h1>;
// }

// SEPARATOR: adjusting all the values, limits, and positions

import React, { useState, useEffect } from "react";
import "./SignUp.css";

const DataComponent = ({ data }) => {
  return (
    <div>
      <h2>Data from Server:</h2>
      <p>{data}</p>
    </div>
  );
};

const DisplayValue = ({ value }) => {
  return <div>{value ? value : "0.0"}</div>;
};

const ResultsDisplay = ({ accuracy, fitness, loss }) => {
  return (
    <div>
      <h2>Results</h2>
      <div>
        <p>Accuracy: </p>
        <DisplayValue value={accuracy} />
      </div>
      <div>
        <p>Fitness: </p>
        <DisplayValue value={fitness} />
      </div>
      <div>
        <p>Loss: </p>
        <DisplayValue value={loss} />
      </div>
    </div>
  );
};

export default function Gladiator() {
  const [intValue1, setIntValue1] = useState(5); // number of layers
  const [intValue2, setIntValue2] = useState(4); // number of nodes per layer
  const [intValue3, setIntValue3] = useState(25); // swarm size
  const [intValue4, setIntValue4] = useState(25); // max iterations
  const [intValue5, setIntValue5] = useState(10); // number of informants
  const [floatValue1, setFloatValue1] = useState(0.9); // alpha
  const [floatValue2, setFloatValue2] = useState(0.8); // beta
  const [floatValue3, setFloatValue3] = useState(0.7); // gamma
  const [floatValue4, setFloatValue4] = useState(0.6); // delta
  const [floatValue5, setFloatValue5] = useState(0.1); // jump size

  const [fetchedData, setFetchedData] = useState(null); // data

  const [accuracy, setAccuracy] = useState(null);
  const [fitness, setFitness] = useState(null);
  const [loss, setLoss] = useState(null);

  const handleIntChange1 = (event) => {
    setIntValue1(parseInt(event.target.value, 10));
  };

  const handleIntChange2 = (event) => {
    setIntValue2(parseInt(event.target.value, 10));
  };

  const handleIntChange3 = (event) => {
    setIntValue3(parseInt(event.target.value, 10));
  };

  const handleIntChange4 = (event) => {
    setIntValue4(parseInt(event.target.value, 10));
  };

  const handleIntChange5 = (event) => {
    setIntValue5(parseInt(event.target.value, 10));
  };

  const handleFloatChange1 = (event) => {
    setFloatValue1(parseFloat(event.target.value));
  };

  const handleFloatChange2 = (event) => {
    setFloatValue2(parseFloat(event.target.value));
  };

  const handleFloatChange3 = (event) => {
    setFloatValue3(parseFloat(event.target.value));
  };

  const handleFloatChange4 = (event) => {
    setFloatValue4(parseFloat(event.target.value));
  };

  const handleFloatChange5 = (event) => {
    setFloatValue5(parseFloat(event.target.value));
  };

  const sendDataToServer = () => {
    // Prepare data object with slider values and file path
    const data = {
      // filePath,
      intValue1,
      intValue2,
      intValue3,
      intValue4,
      intValue5,
      // Add all other values from sliders
      floatValue1,
      floatValue2,
      floatValue3,
      floatValue4,
      floatValue5,
      // Add all other float values
    };

    // Send a POST request to your Flask server
    return fetch("/receive_data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (response.ok) {
          return response.json(); // Parse the JSON response
        }
        throw new Error("Network response was not ok.");
      })
      .then((data) => {
        // Access the response data here
        const [accuracy, fitness, loss] = data;
        console.log("Accuracy:", accuracy);
        console.log("Fitness:", fitness);
        console.log("Loss:", loss);

        setAccuracy(accuracy);
        setFitness(fitness);
        setLoss(loss);

        // Now you can use these values in your frontend as needed
      })
      .catch((error) => {
        console.error("Error sending data:", error);
        throw error;
      });
  };

  const handleClick = () => {
    sendDataToServer()
      .then((dataFromServer) => {
        console.log("Data received:", dataFromServer);
        setFetchedData(dataFromServer);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <div className="container">
      {/* number of layers */}
      <div className="slider-card">
        <label htmlFor="intSlider1">Number of Layers</label>
        <input
          type="range"
          id="intSlider1"
          min={3}
          max={20}
          value={intValue1}
          onChange={handleIntChange1}
        />
        <p>Value: {intValue1}</p>
      </div>
      {/* Number of nodes per layer */}
      <div className="slider-card">
        <label htmlFor="intSlider2">Number of Nodes per layer</label>
        <input
          type="range"
          id="intSlider2"
          min={4}
          max={30}
          value={intValue2}
          onChange={handleIntChange2}
        />
        <p>Value: {intValue2}</p>
      </div>
      {/* Swarm size */}
      <div className="slider-card">
        <label htmlFor="intSlider3">Swarm Size</label>
        <input
          type="range"
          id="intSlider3"
          min={10}
          max={100}
          value={intValue3}
          onChange={handleIntChange3}
        />
        <p>Value: {intValue3}</p>
      </div>
      {/* Alpha value */}
      <div className="slider-card">
        <label htmlFor="floatSlider1">Alpha</label>
        <input
          type="range"
          id="floatSlider1"
          min={0.1}
          max={0.9}
          step={0.01}
          value={floatValue1}
          onChange={handleFloatChange1}
        />
        <p>Value: {floatValue1.toFixed(2)}</p>
      </div>
      {/* Beta value */}
      <div className="slider-card">
        <label htmlFor="floatSlider2">Beta</label>
        <input
          type="range"
          id="floatSlider2"
          min={0.1}
          max={0.9}
          step={0.01}
          value={floatValue2}
          onChange={handleFloatChange2}
        />
        <p>Value: {floatValue2.toFixed(2)}</p>
      </div>
      {/* Gamma value */}
      <div className="slider-card">
        <label htmlFor="floatSlider3">Gamma</label>
        <input
          type="range"
          id="floatSlider3"
          min={0.1}
          max={0.9}
          step={0.01}
          value={floatValue3}
          onChange={handleFloatChange3}
        />
        <p>Value: {floatValue3.toFixed(2)}</p>
      </div>
      {/* Delta value */}
      <div className="slider-card">
        <label htmlFor="floatSlider4">Delta</label>
        <input
          type="range"
          id="floatSlider4"
          min={0.1}
          max={0.9}
          step={0.01}
          value={floatValue4}
          onChange={handleFloatChange4}
        />
        <p>Value: {floatValue4.toFixed(2)}</p>
      </div>
      {/* Jump size */}
      <div className="slider-card">
        <label htmlFor="floatSlider5">Jump Size</label>
        <input
          type="range"
          id="floatSlider5"
          min={0.1}
          max={0.9}
          step={0.01}
          value={floatValue5}
          onChange={handleFloatChange5}
        />
        <p>Value: {floatValue5.toFixed(2)}</p>
      </div>
      {/* Max iterations */}
      <div className="slider-card">
        <label htmlFor="intSlider4">Max Iterations</label>
        <input
          type="range"
          id="intSlider4"
          min={10}
          max={100}
          value={intValue4}
          onChange={handleIntChange4}
        />
        <p>Value: {intValue4}</p>
      </div>
      {/* Number of informants */}
      <div className="slider-card">
        <label htmlFor="intSlider5">Number of Informants</label>
        <input
          type="range"
          id="intSlider5"
          min={5}
          max={70}
          value={intValue5}
          onChange={handleIntChange5}
        />
        <p>Value: {intValue5}</p>
      </div>
      <>
        <button onClick={handleClick}>Send Data</button>
      </>
      <div>
        <h1>Frontend App</h1>
        {fetchedData && <DataComponent data={fetchedData} />}
        {/* {fetchedData && <>{fetchedData}</>} */}
      </div>
      <div>
        <ResultsDisplay accuracy={accuracy} fitness={fitness} loss={loss} />
        {/* Other components and UI elements */}
      </div>
    </div>
  );
}
