const button = document.getElementById('show-message-btn');
const message = document.getElementById('message');

button.addEventListener('click', () => {
  message.textContent = 'Hello from the DevOps CI Demo web app!';
});
