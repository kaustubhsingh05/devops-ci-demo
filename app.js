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
