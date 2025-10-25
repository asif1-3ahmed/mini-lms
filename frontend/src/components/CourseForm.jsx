import React, { useState } from "react";
import API from "../api"; // import your centralized axios instance
import "./CourseManagement.css";

const CourseForm = ({ course, onSubmit, onCancel }) => {
  const [formData, setFormData] = useState({
    title: course?.title || "",
    instructor: course?.instructor || "",
    description: course?.description || "",
  });
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      let response;
      if (course) {
        response = await API.put(`/courses/${course.id}/`, formData);
      } else {
        response = await API.post("/courses/", formData);
      }

      onSubmit(response.data);
      alert(`${course ? "Updated" : "Created"} course successfully.`);
    } catch (error) {
      console.error("Course submit error:", error);
      alert("Failed to submit course. Check console for details.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="course-form-card">
      <h2>{course ? "Edit Course" : "Add New Course"}</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Course Title</label>
          <input
            name="title"
            value={formData.title}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Instructor</label>
          <input
            name="instructor"
            value={formData.instructor}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Description</label>
          <textarea
            name="description"
            rows="5"
            value={formData.description}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-actions">
          <button type="submit" className="btn btn-primary" disabled={loading}>
            {loading ? "Saving..." : course ? "Update Course" : "Create Course"}
          </button>
          <button type="button" className="btn" onClick={onCancel}>
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default CourseForm;
