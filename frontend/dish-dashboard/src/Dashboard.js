import React, { useEffect, useState } from 'react';
import axios from 'axios';
import DishComponent from './components/DishComponent';
import io from 'socket.io-client';

const socket = io('http://localhost:8000'); // Backend URL

function Dashboard() {
  const [dishes, setDishes] = useState([]);

  useEffect(() => {
    fetchDishes();
    socket.on('dish_updated', fetchDishes);
    return () => {
      socket.off('dish_updated', fetchDishes);
    };
  }, []);

  const fetchDishes = async () => {
    try {
      const response = await axios.get('http://localhost:8000/dishes/');
      setDishes(response.data);
    } catch (error) {
      console.error('Error fetching dishes:', error);
    }
  };

  const togglePublish = async (dishId) => {
    try {
      await axios.post(`http://localhost:8000/dishes/${dishId}/toggle_publish/`);
      fetchDishes();
    } catch (error) {
      console.error('Error toggling publish status:', error);
    }
  };

  return (
    <div>
      {dishes.map(dish => (
        <DishComponent key={dish.dishId} dish={dish} togglePublish={togglePublish} />
      ))}
    </div>
  );
}

export default Dashboard;
