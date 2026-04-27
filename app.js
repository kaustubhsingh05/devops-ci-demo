const showMessageBtn = document.getElementById('show-message-btn');
const message = document.getElementById('message');
const incrementBtn = document.getElementById('increment-btn');
const counter = document.getElementById('counter');
const textInput = document.getElementById('text-input');
const displayTextBtn = document.getElementById('display-text-btn');
const displayedText = document.getElementById('displayed-text');
const toggleThemeBtn = document.getElementById('toggle-theme-btn');

let count = 0;

showMessageBtn.addEventListener('click', () => {
  message.textContent = 'Hello from the DevOps CI Demo web app!';
});

incrementBtn.addEventListener('click', () => {
  count++;
  counter.textContent = `Counter: ${count}`;
});

displayTextBtn.addEventListener('click', () => {
  const text = textInput.value;
  displayedText.textContent = text ? `You entered: ${text}` : 'Please enter some text.';
});

toggleThemeBtn.addEventListener('click', () => {
  document.body.classList.toggle('dark');
});

// Calculator
const num1 = document.getElementById('num1');
const num2 = document.getElementById('num2');
const addBtn = document.getElementById('add-btn');
const result = document.getElementById('result');

addBtn.addEventListener('click', () => {
  const n1 = parseFloat(num1.value);
  const n2 = parseFloat(num2.value);
  if (!isNaN(n1) && !isNaN(n2)) {
    result.textContent = `Result: ${n1 + n2}`;
  } else {
    result.textContent = 'Please enter valid numbers.';
  }
});

// Todo List
const todoInput = document.getElementById('todo-input');
const addTodoBtn = document.getElementById('add-todo-btn');
const todoList = document.getElementById('todo-list');

addTodoBtn.addEventListener('click', () => {
  const todoText = todoInput.value.trim();
  if (todoText) {
    const li = document.createElement('li');
    li.textContent = todoText;
    const removeBtn = document.createElement('button');
    removeBtn.textContent = 'Remove';
    removeBtn.addEventListener('click', () => {
      todoList.removeChild(li);
    });
    li.appendChild(removeBtn);
    todoList.appendChild(li);
    todoInput.value = '';
  }
});

// Random Color Generator
const randomColorBtn = document.getElementById('random-color-btn');
const colorDisplay = document.getElementById('color-display');

randomColorBtn.addEventListener('click', () => {
  const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
  colorDisplay.textContent = `Generated color: ${randomColor}`;
  colorDisplay.style.color = randomColor;
});
