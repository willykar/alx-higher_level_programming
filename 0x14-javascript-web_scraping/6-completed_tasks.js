#!/usr/bin/env node

const request = require('request');

const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasksByUser = countCompletedTasks(tasks);
    printUsersWithCompletedTasks(completedTasksByUser);
  }
});

function countCompletedTasks(tasks) {
  const completedByUser = {};
  for (const task of tasks) {
    if (task.completed) {
      const userId = task.userId;
      completedByUser[userId] = (completedByUser[userId] || 0) + 1;
    }
  }
  return completedByUser;
}

function printUsersWithCompletedTasks(completedByUser) {
  for (const userId in completedByUser) {
    if (completedByUser.hasOwnProperty(userId)) {
      const count = completedByUser[userId];
      console.log(`User ${userId} has ${count} completed tasks.`);
    }
  }
}
