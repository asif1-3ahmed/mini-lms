import React from "react";
import API from "../api";
import "./CourseManagement.css";

const CourseItem = ({ course, onEdit, onDelete }) => {
  const handleDelete = async () => {
    if (!window.confirm("Are you sure you want to delete this course?")) return;

    try {
      await API.delete(`/courses/${course.id}/`);
      onDelete(course.id);
      alert("Course deleted successfully.");
    } catch (error) {
      console.error("Delete course error:", error);
      alert("Failed to delete course.");
    }
  };

  return (
    <div className="course-card">
      <h3>{course.title}</h3>
      <p><strong>Instructor:</strong> {course.instructor}</p>
      <p className="course-description">
        {course.description.length > 150
          ? course.description.substring(0, 150) + "..."
          : course.description}
      </p>
      <div className="course-actions">
        <button className="btn btn-primary" onClick={() => onEdit(course)}>
          Edit
        </button>
        <button className="btn btn-danger" onClick={handleDelete}>
          Delete
        </button>
      </div>
    </div>
  );
};

export default CourseItem;
