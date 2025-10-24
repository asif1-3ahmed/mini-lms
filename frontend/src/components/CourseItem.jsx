import React from 'react';
import './CourseManagement.css';

const CourseItem = ({ course, onEdit, onDelete }) => {
  return (
    <div className="course-card">
      <h3>{course.title}</h3>
      <p><strong>Instructor:</strong> {course.instructor}</p>
      <p className="course-description">
        {course.description.substring(0, 150)}{course.description.length > 150 ? '...' : ''}
      </p>
      <div className="course-actions">
        <button className="btn btn-primary" onClick={() => onEdit(course)}>
          Edit
        </button>
        <button className="btn btn-danger" onClick={() => onDelete(course.id)}>
          Delete
        </button>
      </div>
    </div>
  );
};

export default CourseItem;
