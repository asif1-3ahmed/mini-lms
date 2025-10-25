import React, { useState } from 'react';
import './CourseManagement.css';

const CourseForm = ({ course, onSubmit, onCancel }) => {
  const [formData, setFormData] = useState({
    id: course ? course.id : null,
    title: course ? course.title : '',
    instructor: course ? course.instructor : '',
    description: course ? course.description : '',
  });

  // ✅ Set your API base — adjust if your backend URL changes
  const API_BASE = "https://mini-lms-crh4.onrender.com/api/auth";

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const isEditing = !!formData.id;
    const method = isEditing ? 'PUT' : 'POST';
    const url = isEditing
      ? `${API_BASE}/courses/${formData.id}/`
      : `${API_BASE}/courses/`;

    try {
      const response = await fetch(url, {
        method: method,
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include', // keep for CSRF/authenticated sessions
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const updatedCourse = await response.json();
        onSubmit(updatedCourse);
        alert(`${isEditing ? 'Updated' : 'Created'} course successfully.`);
      } else {
        const errorData = await response.json().catch(() => ({}));
        console.error("Failed response:", errorData);
        alert(`Failed to ${isEditing ? 'update' : 'create'} course.`);
      }
    } catch (error) {
      console.error('Error submitting course:', error);
      alert('Error submitting course. Check console for details.');
    }
  };

  const isEditing = !!course;

  return (
    <div className="course-form-card">
      <h2>{isEditing ? 'Edit Course' : 'Add New Course'}</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="title">Course Title</label>
          <input
            type="text"
            id="title"
            name="title"
            value={formData.title}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="instructor">Instructor</label>
          <input
            type="text"
            id="instructor"
            name="instructor"
            value={formData.instructor}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="description">Description</label>
          <textarea
            id="description"
            name="description"
            rows="5"
            value={formData.description}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-actions">
          <button type="submit" className="btn btn-primary">
            {isEditing ? 'Update Course' : 'Create Course'}
          </button>
          <button
            type="button"
            className="btn"
            onClick={onCancel}
            style={{ backgroundColor: '#ccc', color: '#333' }}
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default CourseForm;
