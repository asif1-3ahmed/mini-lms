import React, { useState, useEffect } from 'react';
import CourseList from './CourseList';
import CourseForm from './CourseForm';
import './CourseManagement.css'; 

const CourseManagementPage = () => {
  const [courses, setCourses] = useState([]);
  const [view, setView] = useState('list');
  const [courseToEdit, setCourseToEdit] = useState(null);
  const [user, setUser] = useState(null); // store logged-in user

  // Fetch logged-in user
  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await fetch('/api/profile/', {
          credentials: 'include', // important for session-based auth
        });
        if (response.ok) {
          const data = await response.json();
          setUser(data);
        } else {
          setUser(null); // not logged in
        }
      } catch (error) {
        console.error('Error fetching profile:', error);
      }
    };

    fetchUser();
  }, []);

  // Fetch courses from backend
  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await fetch('/api/courses/', {
          credentials: 'include',
        });
        if (response.ok) {
          const data = await response.json();
          setCourses(data);
        } else {
          console.error('Failed to fetch courses');
        }
      } catch (error) {
        console.error('Error fetching courses:', error);
      }
    };

    fetchCourses();
  }, []);

  // Add new course
  const handleAddCourse = async (newCourseData) => {
    try {
      const response = await fetch('/api/courses/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify(newCourseData),
      });
      if (response.ok) {
        const data = await response.json();
        setCourses(prev => [...prev, data]);
        setView('list');
      } else {
        console.error('Failed to add course');
      }
    } catch (error) {
      console.error('Error adding course:', error);
    }
  };

  // Edit existing course
  const handleEditCourse = async (updatedCourseData) => {
    try {
      const response = await fetch(`/api/courses/${updatedCourseData.id}/`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify(updatedCourseData),
      });
      if (response.ok) {
        const data = await response.json();
        setCourses(prev => prev.map(c => (c.id === data.id ? data : c)));
        setView('list');
        setCourseToEdit(null);
      } else {
        console.error('Failed to update course');
      }
    } catch (error) {
      console.error('Error updating course:', error);
    }
  };

  // Delete course
  const handleDeleteCourse = async (id) => {
    if (!window.confirm('Are you sure you want to delete this course? This action cannot be undone.')) return;

    try {
      const response = await fetch(`/api/courses/${id}/`, {
        method: 'DELETE',
        credentials: 'include',
      });
      if (response.ok) {
        setCourses(prev => prev.filter(c => c.id !== id));
      } else {
        console.error('Failed to delete course');
      }
    } catch (error) {
      console.error('Error deleting course:', error);
    }
  };

  const renderContent = () => {
    if (view === 'add') return <CourseForm onSubmit={handleAddCourse} onCancel={() => setView('list')} />;
    if (view === 'edit' && courseToEdit) return <CourseForm course={courseToEdit} onSubmit={handleEditCourse} onCancel={() => setView('list')} />;
    return (
      <CourseList
        courses={courses}
        onAdd={() => setView('add')}
        onEdit={(course) => { setCourseToEdit(course); setView('edit'); }}
        onDelete={handleDeleteCourse}
      />
    );
  };

  return (
    <>
      {/* Floating Profile */}
      <div className="floating-profile">
        {user ? (
          <>
            {user.avatar && <img src={user.avatar} alt="avatar" className="avatar" />}
            <span className="username">{user.username}</span>
            <button className="profile-btn">Profile</button>
          </>
        ) : (
          <span className="username">Not logged in</span>
        )}
      </div>

      <div className="container">
        {renderContent()}
      </div>
    </>
  );
};

export default CourseManagementPage;
