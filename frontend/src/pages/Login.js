import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Auth.css";

const Login = () => {

  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log(formData);

    // ================= LOGIN API =================
    // axios.post("http://localhost:5000/login", formData)

    alert("Login Successful ✅");

    // Redirect to Dashboard
    navigate("/Dashboard");
  };

  return (
    <div className="auth-container">

      <div className="auth-card login-card">

        {/* ===== LOGO ===== */}

        <div className="logo-section">
          <h1>🌿 ESG Login</h1>
          <p>Access your sustainability dashboard</p>
        </div>

        {/* ===== LOGIN FORM ===== */}

        <form onSubmit={handleSubmit}>

          {/* EMAIL */}

          <div className="input-group">
            <input
              type="email"
              name="email"
              placeholder="Enter Email"
              onChange={handleChange}
              required
            />
          </div>

          {/* PASSWORD */}

          <div className="input-group">
            <input
              type="password"
              name="password"
              placeholder="Enter Password"
              onChange={handleChange}
              required
            />
          </div>

          {/* BUTTON */}

          <button
            type="submit"
            className="auth-btn"
          >
            Login
          </button>

        </form>

        {/* ===== REGISTER LINK ===== */}

        <div className="bottom-text">

          Don't have an account?

          <Link
            to="/register"
            className="auth-link"
          >
            Register
          </Link>

        </div>

      </div>

    </div>
  );
};

export default Login;