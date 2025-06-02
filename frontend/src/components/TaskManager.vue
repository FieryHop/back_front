<template>
  <div class="container mx-auto px-4 py-8 max-w-md">
    <h1 class="text-3xl font-bold mb-6 text-center">Task Manager</h1>

    <!-- Форма добавления -->
    <form @submit.prevent="addTask" class="mb-8 p-4 bg-white rounded-lg shadow">
      <input
        v-model="newTask.title"
        placeholder="Task title"
        class="w-full px-4 py-2 mb-3 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      >
      <div class="flex items-center mb-4">
        <input
          type="checkbox"
          v-model="newTask.completed"
          class="mr-2 h-5 w-5 text-blue-600 rounded"
        >
        <label>Completed</label>
      </div>
      <button
        type="submit"
        class="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Add Task
      </button>
    </form>

    <!-- Список задач -->
    <div class="bg-white rounded-lg shadow">
      <div
        v-for="task in tasks"
        :key="task.id"
        class="flex items-center justify-between p-4 border-b"
      >
        <div>
          <h3 class="font-semibold" :class="{ 'line-through text-gray-500': task.completed }">
            {{ task.title }}
          </h3>
          <span class="text-sm text-gray-500">
            {{ task.completed ? 'Completed' : 'Pending' }}
          </span>
        </div>
        <button
          @click="deleteTask(task.id)"
          class="text-red-500 hover:text-red-700"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '@/api/api';

const tasks = ref([]);
const newTask = ref({
  title: '',
  completed: false
});

onMounted(async () => {
  await fetchTasks();
});

async function fetchTasks() {
  tasks.value = await api.getTasks();
}

async function addTask() {
  await api.addTask(newTask.value);
  newTask.value = { title: '', completed: false };
  await fetchTasks();
}

async function deleteTask(id) {
  await api.deleteTask(id);
  await fetchTasks();
}
</script>