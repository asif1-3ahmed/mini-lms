import React, { useState, useEffect } from 'react';
import './CourseManagement.css';

const CourseForm = ({ course, onSubmit, onCancel }) => {
  const [formData, setFormData] = useState({
    id: course ? course.id : null,
    title: course ? course.title : '',
    instructor: course ? course.instructor : '',
    description: course ? course.description : '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const method = formData.id ? 'PUT' : 'POST';
    const url = formData.id ? `/api/courses/${formData.id}/` : '/api/courses/';

    try {
      const response = await fetch(url, {
        method: method,
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const updatedCourse = await response.json();
        onSubmit(updatedCourse);
        alert(`${formData.id ? 'Updated' : 'Created'} course successfully.`);
      } else {
        alert('Failed to submit course');
      }
    } catch (error) {
      console.error('Error submitting course:', error);
      alert('Error submitting course');
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
          ></textarea>
        </div>
        <div className="form-actions">
          <button type="submit" className="btn btn-primary">
            {isEditing ? 'Update Course' : 'Create Course'}
          </button>
          <button type="button" className="btn" onClick={onCancel} style={{ backgroundColor: '#ccc', color: '#333' }}>
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default CourseForm;
