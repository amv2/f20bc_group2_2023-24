// SEPARATOR: adjusting all the values, limits, and positions

import React, { useState } from "react";
import "./SignUp.css";
import Slider from "../Slider";
import MultiSelect from "../MultiSelect";
import "../Cards.css";

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

const ResultsDisplay = ({ accuracy, fitness, loss, time }) => {
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
      <div>
        <p>Elapsed Time (seconds): </p>
        <DisplayValue value={time} />
      </div>
    </div>
  );
};

export default function Regular() {
  const [intValue1, setIntValue1] = useState(5); // number of layers
  const [intValue2, setIntValue2] = useState(6); // number of nodes per layer
  const [intValue3, setIntValue3] = useState(25); // swarm size
  const [intValue4, setIntValue4] = useState(25); // max iterations
  const [intValue5, setIntValue5] = useState(15); // number of informants
  const [floatValue1, setFloatValue1] = useState(0.9); // alpha
  const [floatValue2, setFloatValue2] = useState(0.8); // beta
  const [floatValue3, setFloatValue3] = useState(0.7); // gamma
  const [floatValue4, setFloatValue4] = useState(0.6); // delta
  const [floatValue5, setFloatValue5] = useState(0.2); // jump size

  const [intValue6, setIntValue6] = useState(2); // activation function
  const [intValue7, setIntValue7] = useState(1); // loss function

  const [stringValue1, setStringValue1] = useState("ReLU"); // activation function chosen
  const [stringValue2, setStringValue2] = useState("BinaryCrossEntropy"); // loss function chosen

  const [fetchedData, setFetchedData] = useState(null); // data

  const [accuracy, setAccuracy] = useState(null);
  const [fitness, setFitness] = useState(null);
  const [loss, setLoss] = useState(null);
  const [time, setTime] = useState(null);

  const activationFuncs = [
    { name: "None", value: 1 },
    { name: "ReLU", value: 2 },
    { name: "Sigmoid", value: 3 },
    { name: "Tanh", value: 4 },
    { name: "LeakyReLU", value: 5 },
    { name: "Swish", value: 6 },
    { name: "Softmax", value: 7 },
    { name: "GELU", value: 8 },
    { name: "None", value: 9 },
  ];

  const lossFuncs = [
    { name: "None", value: 1 },
    { name: "Mse", value: 2 },
    { name: "BinaryCrossEntropy", value: 3 },
    { name: "Hinge", value: 4 },
    { name: "None", value: 5 },
  ];

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

  const handleIntChange6 = (event) => {
    setIntValue6(parseInt(event.target.value, 10));
    setStringValue1(activationFuncs[intValue6].name.toString());
  };

  const handleIntChange7 = (event) => {
    setIntValue7(parseInt(event.target.value, 10));
    // console.log(activationFuncs[intValue7].name);
    setStringValue2(lossFuncs[intValue7].name);
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
    const data = {
      intValue1,
      intValue2,
      intValue3,
      intValue4,
      intValue5,
      intValue6,
      intValue7,
      floatValue1,
      floatValue2,
      floatValue3,
      floatValue4,
      floatValue5,
    };

    // Send a POST request to Flask server
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
        // Access the response data
        const [accuracy, fitness, loss, time] = data;
        console.log("Accuracy:", accuracy);
        console.log("Fitness:", fitness);
        console.log("Loss:", loss);
        console.log("Elapsed Time:", time);

        setAccuracy(accuracy);
        setFitness(fitness);
        setLoss(loss);
        setTime(Number(time).toFixed(2));
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
      <div className="cards__container">
        <div className="cards__wrapper">
          <ul className="cards__items">
            <Slider
              src="images/img-1.jpg"
              name="Number of Layers"
              min={3}
              max={20}
              numValue={intValue1}
              handleNumChange={handleIntChange1}
            />
            <Slider
              src="images/img-2.jpg"
              name="Number of Nodes per Layer"
              min={4}
              max={30}
              numValue={intValue2}
              handleNumChange={handleIntChange2}
            />
          </ul>
          <ul className="cards__items">
            <MultiSelect
              src="images/img-2.jpg"
              name="Activation Function for each Layer"
              min={1}
              max={8}
              numValue={intValue6}
              handleNumChange={handleIntChange6}
              selectionText="Selected"
              numName={stringValue1}
            />
            <MultiSelect
              src="images/img-2.jpg"
              name="Loss Function used"
              min={1}
              max={4}
              numValue={intValue7}
              handleNumChange={handleIntChange7}
              selectionText="Selected"
              numName={stringValue2}
            />
          </ul>
          <ul className="cards__items">
            <Slider
              src="images/img-4.jpg"
              name="Alpha Value"
              min={0.1}
              max={0.9}
              numValue={floatValue1}
              step={0.01}
              handleNumChange={handleFloatChange1}
            />
            <Slider
              src="images/img-5.jpg"
              name="Beta Value"
              min={0.1}
              max={0.9}
              numValue={floatValue2}
              step={0.01}
              handleNumChange={handleFloatChange2}
            />
            <Slider
              src="images/img-6.jpg"
              name="Gamma Value"
              min={0.1}
              max={0.9}
              numValue={floatValue3}
              step={0.01}
              handleNumChange={handleFloatChange3}
            />
            <Slider
              src="images/img-7.jpg"
              name="Delta Value"
              min={0.1}
              max={0.9}
              numValue={floatValue4}
              step={0.01}
              handleNumChange={handleFloatChange4}
            />
          </ul>
          <ul className="cards__items">
            <Slider
              src="images/img-8.jpg"
              name="Jump Size"
              min={0.1}
              max={0.9}
              numValue={floatValue5}
              step={0.01}
              handleNumChange={handleFloatChange5}
            />
            <Slider
              src="images/img-3.jpg"
              name="Swarm Size"
              min={10}
              max={100}
              numValue={intValue3}
              handleNumChange={handleIntChange3}
            />
            <Slider
              src="images/img-10.jpg"
              name="Number of Informants"
              min={1}
              max={30}
              numValue={intValue5}
              handleNumChange={handleIntChange5}
            />
            <Slider
              src="images/img-9.jpg"
              name="Maximum Iterations"
              min={10}
              max={500}
              numValue={intValue4}
              handleNumChange={handleIntChange4}
            />
          </ul>
        </div>
      </div>
      <>
        <button onClick={handleClick}>Send Data</button>
      </>
      <div>
        <h1>Frontend App</h1>
        {fetchedData && <DataComponent data={fetchedData} />}
      </div>
      <div>
        <ResultsDisplay
          accuracy={accuracy}
          fitness={fitness}
          loss={loss}
          time={time}
        />
      </div>
    </div>
  );
}
