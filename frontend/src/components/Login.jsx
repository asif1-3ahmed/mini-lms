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
    const response = await API.post("/login/", formData); // using your axios API instance
    const data = response.data;

    if (response.status === 200) {
      localStorage.setItem("token", data.token);  // save token
      localStorage.setItem("username", data.username);
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
