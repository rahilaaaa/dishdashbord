// src/components/DishList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './DishList.css';

const DishList = () => {
  const [dishes, setDishes] = useState([]);

  useEffect(() => {
    fetchDishes();
  }, []);

  const fetchDishes = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/dishes/');
      setDishes(response.data);
    } catch (error) {
      console.error('Error fetching dishes:', error);
    }
  };

  const handleTogglePublish = async (dishId) => {
    try {
      await axios.post(`http://localhost:8000/api/dishes/${dishId}/toggle_publish/`);
      fetchDishes();
    } catch (error) {
      console.error('Error toggling publish status:', error);
    }
  };

  return (
    <div className="dish-container">
      {dishes.map((dish) => (
        <div key={dish.dishId} className="dish-card">
          <img src={dish.imageUrl} alt={dish.dishName} className="dish-image" />
          <h3 className="dish-name">{dish.dishName}</h3>
          <p className="dish-published">Published: {dish.isPublished.toString()}</p>
          <button className="toggle-button" onClick={() => handleTogglePublish(dish.dishId)}>
            Toggle Publish
          </button>
        </div>
      ))}
    </div>
  );
};

export default DishList;
