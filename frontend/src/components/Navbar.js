import React from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Navbar.css";

function Navbar() {

    const navigate = useNavigate();

    // ================= LOGOUT FUNCTION =================

    const handleLogout = () => {

        // Remove login session
        localStorage.removeItem("isLoggedIn");

        alert("Logged Out Successfully ✅");

        // Redirect to login page
        navigate("/login");
    };

    return (

        <nav className="navbar">

            {/* ===== LOGO ===== */}

            <h2 className="logo">
                🌿 Breathe ESG
            </h2>

            {/* ===== NAVIGATION LINKS ===== */}

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

            {/* ===== LOGOUT BUTTON ===== */}

            <button
                className="logout-btn"
                onClick={handleLogout}
            >
                Logout
            </button>

        </nav>
    );
}

export default Navbar;
