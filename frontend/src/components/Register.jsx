import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import API from "../api"; // centralized axios instance
import "./Login.css"; // reuse same styles

export default function Register() {
  const [formData, setFormData] = useState({
    username: "",
    email: "", // Added email field
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

    // Password validation
    if (formData.password !== formData.confirmPassword) {
      alert("Passwords do not match!");
      return;
    }

    setLoading(true);

    try {
      const response = await API.post(
        "/register/",
        {
          username: formData.username,
          email: formData.email,  // Sending email in the request
          password: formData.password,
        },
        {
          headers: { "Content-Type": "application/json" },
        }
      );

      if (response.status === 201) {
        alert("Registration successful! Please login.");
        navigate("/login");
      }
    } catch (error) {
      console.error("Registration error:", error);

      // Better error handling for DRF
      if (error.response && error.response.data) {
        const messages = error.response.data;
        let msg = "Registration failed.";
        if (messages.username) msg = `Username: ${messages.username.join(", ")}`;
        else if (messages.password) msg = `Password: ${messages.password.join(", ")}`;
        else if (messages.email) msg = `Email: ${messages.email.join(", ")}`;
        else if (messages.detail) msg = messages.detail;

        alert(msg);
      } else {
        alert("Registration failed. Server error.");
      }
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
          type="email"  // Email input
          name="email"
          placeholder="Email"
          value={formData.email}
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
