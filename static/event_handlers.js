'use strict';

console.log('js is working')

const addToScheduleButton = document.querySelectorAll('.add-to-schedule-button');
// function handleClick(evt) {
//   alert('Added to schedule.');
//   console.log(evt)
//   console.log(evt.target)
// }
addToScheduleButton.forEach(button => button.addEventListener('click', event => {
alert(event.target.getAttribute("data-name"));
}));

// addToScheduleButton.addEventListener('click', handleClick);

