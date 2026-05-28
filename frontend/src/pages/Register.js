import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Auth.css";

const Register = () => {

  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    fullname: "",
    email: "",
    company: "",
    role: "",
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

    // ================= API CALL =================
    // axios.post("http://localhost:5000/register", formData)

    alert("Registration Successful ✅");

    // Redirect to Login Page
    navigate("/");
  };

  return (
    <div className="auth-container">

      <div className="auth-card register-card">

        {/* ===== LOGO SECTION ===== */}

        <div className="logo-section">
          <h1> ESG Register</h1>
          <p>Create your smart ESG analytics account</p>
        </div>

        {/* ===== REGISTER FORM ===== */}

        <form onSubmit={handleSubmit}>

          {/* FULL NAME */}

          <div className="input-group">
            <input
              type="text"
              name="fullname"
              placeholder="Enter Full Name"
              onChange={handleChange}
              required
            />
          </div>

          {/* EMAIL */}

          <div className="input-group">
            <input
              type="email"
              name="email"
              placeholder="Enter Email Address"
              onChange={handleChange}
              required
            />
          </div>

          {/* COMPANY */}

          <div className="input-group">
            <input
              type="text"
              name="company"
              placeholder="Enter Company Name"
              onChange={handleChange}
              required
            />
          </div>

          {/* ROLE */}

          <div className="input-group">
            <select
              name="role"
              onChange={handleChange}
              required
            >
              <option value="">
                Select Your Role
              </option>

              <option value="Analyst">
                ESG Analyst
              </option>

              <option value="Manager">
                Sustainability Manager
              </option>

              <option value="Admin">
                Administrator
              </option>
            </select>
          </div>

          {/* PASSWORD */}

          <div className="input-group">
            <input
              type="password"
              name="password"
              placeholder="Create Strong Password"
              onChange={handleChange}
              required
            />
          </div>

          {/* REGISTER BUTTON */}

          <button
            type="submit"
            className="auth-btn"
          >
            Create Account
          </button>

        </form>

        {/* ===== LOGIN LINK ===== */}

        <div className="bottom-text">

          Already have an account?

          <Link
            to="/"
            className="auth-link"
          >
            Login
          </Link>

        </div>

      </div>

    </div>
  );
};

export default Register;