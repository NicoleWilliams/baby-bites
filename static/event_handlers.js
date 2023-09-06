'use strict';

console.log('js is working')

const addToScheduleButton = document.querySelectorAll('.add-to-schedule-button');

addToScheduleButton.forEach(button => button.addEventListener('click', event => {
  let foodName = event.target.getAttribute("data-name")
  let foodId = event.target.getAttribute("data-id")
  alert(foodName);

  const data = {
    id: foodId, 
    name: foodName,
  }

  fetch('/edit-calendar', { 
    method: 'POST',
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  })
  .then((response) => response.json())
  .then((data) => console.log(data))  
}));
// input to try date, get user id, when clicked update tried to true



