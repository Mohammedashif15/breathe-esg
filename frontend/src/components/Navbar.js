import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";

function Navbar() {

    return (
        <nav className="navbar">

            <h2>Breathe ESG</h2>

            <div className="nav-links">

                <Link to="/">
                    Dashboard
                </Link>

                <Link to="/upload">
                    Upload
                </Link>

                <Link to="/emissions">
                    Emissions
                </Link>

                <Link to="/reviews">
                    Reviews
                </Link>

            </div>
        </nav>
    );
}

export default Navbar;