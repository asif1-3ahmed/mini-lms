import React, { useEffect, useState } from 'react';
import CourseItem from './CourseItem';
import './CourseManagement.css';

const API_BASE = "https://mini-lms-crh4.onrender.com/api";

const CourseList = ({ onEdit, onAdd }) => {
  const [courses, setCourses] = useState([]);

  // Fetch courses from backend
  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await fetch(`${API_BASE}/courses/`, {
          credentials: 'include', // for session-based auth
        });
        if (response.ok) {
          const data = await response.json();
          setCourses(data);
        } else {
          console.error('Failed to fetch courses', response.status);
        }
      } catch (error) {
        console.error('Error fetching courses:', error);
      }
    };

    fetchCourses();
  }, []);

  // Handle deleting a course
  const handleDeleteCourse = async (id) => {
    if (!window.confirm('Are you sure you want to delete this course?')) return;

    try {
      const response = await fetch(`${API_BASE}/courses/${id}/`, {
        method: 'DELETE',
        credentials: 'include',
      });

      if (response.ok || response.status === 204) {
        setCourses((prev) => prev.filter((course) => course.id !== id));
        alert('Course deleted successfully.');
      } else {
        const errorData = await response.json().catch(() => ({}));
        console.error('Failed to delete course:', errorData);
        alert('Failed to delete course.');
      }
    } catch (error) {
      console.error('Error deleting course:', error);
      alert('Error deleting course.');
    }
  };

  return (
    <div className="course-list-page">
      <div className="list-header">
        <h1>Course Management</h1>
        <button className="btn btn-primary" onClick={onAdd}>
          + Add New Course
        </button>
      </div>
      <div className="course-cards-container">
        {courses.length > 0 ? (
          courses.map((course) => (
            <CourseItem
              key={course.id}
              course={course}
              onEdit={onEdit}
              onDelete={handleDeleteCourse}
            />
          ))
        ) : (
          <p>No courses found. Click "Add New Course" to begin.</p>
        )}
      </div>
    </div>
  );
};

export default CourseList;
