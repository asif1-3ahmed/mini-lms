import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Register from "./components/Register";
import Login from "./components/Login";
import Welcome from "./components/Welcome";
import CourseManagementPage from "./components/CourseManagementPage";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/courses" element={<CourseManagementPage />} />
      </Routes>
    </Router>
  );
}
