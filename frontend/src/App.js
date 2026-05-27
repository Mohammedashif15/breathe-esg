import React from "react";
import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";

import Navbar from "./components/Navbar";

import Dashboard from "./pages/Dashboard";
import Upload from "./pages/Upload";
import Emissions from "./pages/Emissions";
import Reviews from "./pages/Reviews";

import "./App.css";

function App() {

    return (

        <BrowserRouter>

            <Navbar />

            <div className="container">

                <Routes>

                    <Route
                        path="/"
                        element={<Dashboard />}
                    />

                    <Route
                        path="/upload"
                        element={<Upload />}
                    />

                    <Route
                        path="/emissions"
                        element={<Emissions />}
                    />

                    <Route
                        path="/reviews"
                        element={<Reviews />}
                    />

                </Routes>

            </div>

        </BrowserRouter>
    );
}

export default App;