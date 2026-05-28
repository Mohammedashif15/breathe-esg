import React from "react";
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";

import Navbar from "./components/Navbar";

import Dashboard from "./pages/Dashboard";
import Upload from "./pages/Upload";
import Emissions from "./pages/Emissions";
import Reviews from "./pages/Reviews";

import Login from "./pages/Login";
import Register from "./pages/Register";

import "./App.css";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        {/* ================= LOGIN ================= */}

        <Route
          path="/"
          element={<Login />}
        />

        {/* ================= REGISTER ================= */}

        <Route
          path="/register"
          element={<Register />}
        />

        {/* ================= DASHBOARD ================= */}

        <Route
          path="/dashboard"
          element={
            <>
              <Navbar />
              <div className="container">
                <Dashboard />
              </div>
            </>
          }
        />

        {/* ================= UPLOAD ================= */}

        <Route
          path="/upload"
          element={
            <>
              <Navbar />
              <div className="container">
                <Upload />
              </div>
            </>
          }
        />

        {/* ================= EMISSIONS ================= */}

        <Route
          path="/emissions"
          element={
            <>
              <Navbar />
              <div className="container">
                <Emissions />
              </div>
            </>
          }
        />

        {/* ================= REVIEWS ================= */}

        <Route
          path="/reviews"
          element={
            <>
              <Navbar />
              <div className="container">
                <Reviews />
              </div>
            </>
          }
        />

        {/* ================= UNKNOWN ROUTE ================= */}

        <Route
          path="*"
          element={<Navigate to="/" />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;
