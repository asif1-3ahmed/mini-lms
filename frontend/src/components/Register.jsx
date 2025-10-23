import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./register.css";

export default function Register() {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
  });
  const [status, setStatus] = useState({ message: "", type: "" });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus({ message: "🔵 Checking user availability...", type: "info" });

    try {
      const response = await fetch("https://mini-lms-crh4.onrender.com/api/auth/register/", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(formData),
});

      });

      const data = await response.json();

      if (response.ok) {
        // Simulate checking if the user already exists
        if (data.exists) {
          setStatus({
            message: "🔴 Username already exists. Please try another.",
            type: "error",
          });
        } else {
          setStatus({
            message: "🟢 Registration successful! Redirecting...",
            type: "success",
          });
          setTimeout(() => navigate("/login"), 1500);
        }
      } else {
        // Handles duplicate username/email from backend response
        if (data.message?.toLowerCase().includes("exists")) {
          setStatus({
            message: "🔴 Username or email already registered!",
            type: "error",
          });
        } else {
          setStatus({
            message: "🔴 Registration failed. Please try again.",
            type: "error",
          });
        }
      }
    } catch {
      setStatus({
        message: "⚠️ Server unreachable. Please try again later.",
        type: "error",
      });
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
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={handleChange}
          required
        />
        <button type="submit">Register</button>
      </form>

      {status.message && (
        <div className={`status-message ${status.type}`}>
          {status.message}
        </div>
      )}

      <p>
        Already have an account?{" "}
        <Link to="/login" className="link">
          Login
        </Link>
      </p>
    </div>
  );
}
