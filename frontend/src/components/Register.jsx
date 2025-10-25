import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import API from "../api";
import "./Login.css";

export default function Register() {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
  });
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState(""); // 👈 show user-friendly errors
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (formData.password !== formData.confirmPassword) {
      setErrorMsg("Passwords do not match!");
      return;
    }

    setLoading(true);
    setErrorMsg("");

    try {
      const response = await API.post("/register/", {
        username: formData.username,
        email: formData.email || "",
        password: formData.password,
      });

      if (response.status === 201) {
        navigate("/login");
      }
    } catch (error) {
      console.error("Registration error:", error);

      let message = "Registration failed. Please check your input.";

      // Try to read backend JSON error
      if (error.response?.data) {
        if (typeof error.response.data === "object") {
          message = Object.values(error.response.data).flat().join(" ");
        } else if (typeof error.response.data === "string") {
          message = error.response.data;
        }
      }

      // Prevent HTML 400 page from showing
      if (message.includes("<!doctype html")) {
        message = "Invalid data. Please fill out all required fields correctly.";
      }

      setErrorMsg(message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">
      <h1>Create Account</h1>

      {errorMsg && <p className="error-message">{errorMsg}</p>} {/* 👈 visible error */}

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
          type="email"
          name="email"
          placeholder="Email (optional)"
          value={formData.email}
          onChange={handleChange}
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
