import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import API from "../api"; // centralized axios instance
import "./Login.css";

export default function Login() {
  const [formData, setFormData] = useState({ username: "", password: "" });
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      // Explicitly send username and password as JSON
      const response = await API.post("/login/", {
        username: formData.username,
        password: formData.password,
      }, {
        headers: { "Content-Type": "application/json" },
      });

      // If login successful
      if (response.status === 200) {
        const data = response.data;
        localStorage.setItem("token", data.token);
        localStorage.setItem("username", data.username);
        localStorage.setItem("role", data.role || "student");

        navigate("/courses"); // redirect to courses page
      }
    } catch (error) {
      // DRF usually returns detailed error messages
      console.error("Login error:", error);
      if (error.response && error.response.data) {
        const msg = error.response.data.detail || error.response.data.message || "Invalid credentials.";
        alert(msg);
      } else {
        alert("Login failed. Server unreachable.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">
      <h1>Welcome Back</h1>
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
        <button type="submit" disabled={loading}>
          {loading ? "Logging in..." : "Login"}
        </button>
      </form>

      <p>
        Don’t have an account?{" "}
        <Link to="/register" className="link">
          Register
        </Link>
      </p>
    </div>
  );
}
