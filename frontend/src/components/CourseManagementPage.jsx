import React, { useState } from "react";
import CourseList from "./CourseList";
import CourseForm from "./CourseForm";

const CourseManagementPage = () => {
  const [selectedCourse, setSelectedCourse] = useState(null);
  const [showForm, setShowForm] = useState(false);

  const handleAddCourse = () => {
    setSelectedCourse(null);
    setShowForm(true);
  };

  const handleEditCourse = (course) => {
    setSelectedCourse(course);
    setShowForm(true);
  };

  const handleFormSubmit = (course) => {
    setShowForm(false);
    // Optionally, refresh course list or update state here
  };

  const handleFormCancel = () => {
    setShowForm(false);
  };

  return (
    <div>
      {showForm ? (
        <CourseForm
          course={selectedCourse}
          onSubmit={handleFormSubmit}
          onCancel={handleFormCancel}
        />
      ) : (
        <CourseList onEdit={handleEditCourse} onAdd={handleAddCourse} />
      )}
    </div>
  );
};

export default CourseManagementPage;
