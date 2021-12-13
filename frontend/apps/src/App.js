import "./App.css";
import React from "react";
import Homepage from "./components/HomePage/HomePage";
import { useSelector } from "react-redux";
import Loginpage from "./components/Login/LoginPage";
import { Route, Routes } from "react-router-dom";

const App = () => {
  const isSignedIn = useSelector((state) => state.auth.isSignedIn);

  return (
    <div className="App">
      {isSignedIn ? (
        <Routes>
          <Route path="/" exact element={<Homepage />} />
        </Routes>
      ) : (
        <Loginpage />
      )}
    </div>
  );
};

export default App;
