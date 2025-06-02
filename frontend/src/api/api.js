import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NODE_ENV === 'production'
    ? '/api'
    : 'http://localhost:8000/api',
});

export default {
  async getTasks() {
    const response = await api.get('/tasks');
    return response.data;
  },
  async addTask(task) {
    const response = await api.post('/tasks', task);
    return response.data;
  },
  async deleteTask(id) {
    await api.delete(`/tasks/${id}`);
  }
}