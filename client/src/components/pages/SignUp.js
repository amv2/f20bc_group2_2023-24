import React from "react";
import "../../App.css";

export default function SignUp() {
  return <h1 className="sign-up">LIKE & SUBSCRIBE</h1>;
}

// SEPARATOR: Integer and Float sliders

// import React, { useState } from "react";
// import "./SignUp.css";

// export default function SignUp() {
//   const [intValue, setIntValue] = useState(1);
//   const [floatValue, setFloatValue] = useState(1.0);

//   const handleIntChange = (event) => {
//     setIntValue(parseInt(event.target.value, 10));
//   };

//   const handleFloatChange = (event) => {
//     setFloatValue(parseFloat(event.target.value));
//   };

//   return (
//     <div className="slider-container">
//       <div className="slider-card">
//         <label htmlFor="integerSlider">Integer Slider</label>
//         <input
//           type="range"
//           id="integerSlider"
//           min={1}
//           max={10}
//           value={intValue}
//           onChange={handleIntChange}
//         />
//         <p>Value: {intValue}</p>
//       </div>
//       <div className="slider-card">
//         <label htmlFor="floatSlider">Float Slider</label>
//         <input
//           type="range"
//           id="floatSlider"
//           min={1}
//           max={10}
//           step={0.1}
//           value={floatValue}
//           onChange={handleFloatChange}
//         />
//         <p>Value: {floatValue.toFixed(2)}</p>
//       </div>
//     </div>
//   );
// }

// SEPARATOR: CSV file selector

// import React, { useState } from "react";

// export default function SignUp() {
//   const [selectedFile, setSelectedFile] = useState(null);

//   const handleFileChange = (event) => {
//     const file = event.target.files[0];

//     if (file && file.type === "text/csv") {
//       setSelectedFile(file.path); // Store the path in the state
//     } else {
//       alert("Please choose a valid CSV file.");
//     }
//   };

//   return (
//     <div>
//       <input type="file" accept=".csv" onChange={handleFileChange} />
//       <p>Selected File: {selectedFile || "None"}</p>
//     </div>
//   );
// }
