import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Register.css"; // Ensure the path is correct

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
        body: JSON.stringify(formData),  // Ensure you are sending the correct fields: username, email, password
      });

      const data = await response.json();

      if (response.ok) {
        setStatus({
          message: "🟢 Registration successful! Redirecting...",
          type: "success",
        });
        setTimeout(() => navigate("/login"), 1500); // Redirect after 1.5 seconds
      } else {
        // Handle backend response errors
        console.log("Backend response:", data); // Log full response to debug
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
    } catch (error) {
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
          value={formData.username}
          onChange={handleChange}
          required
        />
        <input
          type="email"
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
        <button type="submit">Register</button>
      </form>

      {/* Display status messages */}
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
