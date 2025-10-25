import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import API from "../api"; // centralized axios instance
import "./Login.css"; // reuse the same styles
import axios from "axios";


export default function Register() {
  const [formData, setFormData] = useState({
    username: "",
    password: "",
    confirmPassword: "",
  });
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (formData.password !== formData.confirmPassword) {
      alert("Passwords do not match!");
      return;
    }

    setLoading(true);

    try {
      const response = await API.post("/register/", {
        username: formData.username,
        password: formData.password,
      });

      if (response.status === 201) {
        alert("Registration successful! Please login.");
        navigate("/login");
      }
    } catch (error) {
      console.error("Registration error:", error);
      alert(
        error.response?.data?.message ||
          "Registration failed. Username might already exist."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">
      <h1>Create Account</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="confirmPassword"
          placeholder="Confirm Password"
          value={formData.confirmPassword}
          onChange={handleChange}
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? "Registering..." : "Register"}
        </button>
      </form>

      <p>
        Already have an account?{" "}
        <Link to="/login" className="link">
          Login
        </Link>
      </p>
    </div>
  );
}
