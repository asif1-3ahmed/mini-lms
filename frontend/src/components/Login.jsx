import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Login.css";

export default function Login() {
  const [formData, setFormData] = useState({ username: "", password: "" });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("https://mini-lms-crh4.onrender.com/api/auth/login/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok) {
        // Save username or token if needed
        localStorage.setItem("username", formData.username);

        // ✅ Redirect to Course Management Page
        navigate("/courses");
      } else {
        alert(data.message || "Invalid credentials");
      }
    } catch {
      alert("Backend not reachable!");
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
        <button type="submit">Login</button>
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
