'use strict';

console.log('js is working')

const addToScheduleButton = document.querySelectorAll('.add-to-schedule-button');

addToScheduleButton.forEach(button => button.addEventListener('click', event => {
  let foodName = event.target.getAttribute("data-name")
  let foodId = event.target.getAttribute("data-id")
  let tryDate = document.querySelector(`#try-date-${foodId}`).value
  
  console.log(tryDate)

  const data = {
    id: foodId, 
    name: foodName,
    date: tryDate
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

const triedCheckbox = document.querySelectorAll('.tried-checkbox');

triedCheckbox.forEach(checkbox => checkbox.addEventListener('click', event => {
  let tried = event.target.getAttribute("data-tried");
  let foodId = event.target.getAttribute("data-food-id");

  const data = {
    tried: tried,
    foodId: foodId
  }

  console.log('successfully clicked!')

  fetch('/create-rating', {
    method: 'POST',
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  })
  .then((response) => response.json())
  .then((data) => console.log(data)) 

  window.location.href = `/foods/${foodId}`;
}));



