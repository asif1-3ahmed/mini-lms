import React from 'react';
import './CourseManagement.css';

const API_BASE = "https://mini-lms-crh4.onrender.com/api";

const CourseItem = ({ course, onEdit, onDelete }) => {
  // Handles deleting a course by calling the backend
  const handleDelete = async (id) => {
    if (!window.confirm("Are you sure you want to delete this course?")) return;

    try {
      const response = await fetch(`${API_BASE}/courses/${id}/`, {
        method: 'DELETE',
        credentials: 'include', // include cookies/session for authentication
      });

      if (response.ok || response.status === 204) {
        onDelete(id); // remove course from parent state
        alert('Course deleted successfully.');
      } else {
        const errorData = await response.json().catch(() => ({}));
        console.error('Delete failed:', errorData);
        alert('Failed to delete course.');
      }
    } catch (error) {
      console.error('Error deleting course:', error);
      alert('Error deleting course.');
    }
  };

  return (
    <div className="course-card">
      <h3>{course.title}</h3>
      <p><strong>Instructor:</strong> {course.instructor}</p>
      <p className="course-description">
        {course.description.length > 150
          ? course.description.substring(0, 150) + '...'
          : course.description}
      </p>
      <div className="course-actions">
        <button className="btn btn-primary" onClick={() => onEdit(course)}>
          Edit
        </button>
        <button className="btn btn-danger" onClick={() => handleDelete(course.id)}>
          Delete
        </button>
      </div>
    </div>
  );
};

export default CourseItem;
