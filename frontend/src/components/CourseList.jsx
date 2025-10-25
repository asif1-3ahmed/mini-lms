import React, { useEffect, useState } from "react";
import CourseItem from "./CourseItem";
import API from "../api";
import "./CourseManagement.css";

const CourseList = ({ onEdit, onAdd }) => {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await API.get("/courses/");
        setCourses(response.data);
      } catch (error) {
        console.error("Fetch courses error:", error);
        alert("Failed to load courses.");
      } finally {
        setLoading(false);
      }
    };
    fetchCourses();
  }, []);

  const handleDeleteCourse = (id) => {
    setCourses((prev) => prev.filter((course) => course.id !== id));
  };

  if (loading) return <p>Loading courses...</p>;

  return (
    <div className="course-list-page">
      <div className="list-header">
        <h1>Course Management</h1>
        <button className="btn btn-primary" onClick={onAdd}>
          + Add New Course
        </button>
      </div>
      <div className="course-cards-container">
        {courses.length ? (
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
