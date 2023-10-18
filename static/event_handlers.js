'use strict';

console.log('js is working')

const addToScheduleButton = document.querySelectorAll('.add-to-schedule-button');

addToScheduleButton.forEach(button => button.addEventListener('click', event => {
  let foodName = event.target.getAttribute('data-name')
  let foodId = event.target.getAttribute('data-id')
  let tryDate = document.querySelector(`#try-date-${foodId}`).value
  
  console.log(tryDate)

  const data = {
    id: foodId, 
    name: foodName,
    date: tryDate
  }

  fetch('/edit-calendar', { 
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  })
  .then((response) => response.json())
  .then((data) => console.log(data))  
}));

const triedCheckbox = document.querySelectorAll('.tried-checkbox');

triedCheckbox.forEach(checkbox => checkbox.addEventListener('click', event => {
  let tried = event.target.getAttribute('data-tried');
  let foodId = event.target.getAttribute('data-food-id');

  const data = {
    tried: tried,
    foodId: foodId
  }

  fetch('/mark-as-tried', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  })
  .then((response) => response.json())
  .then((data) => console.log(data)) 
  

  window.location.href = `/foods/${foodId}`;
}));


let foodData = {}

fetch('/create-food-dict')
  .then((response) => response.json())
  .then((data) => {foodData = data
    // console.log(foodData);
  }) 


document.querySelector('#search-form').addEventListener('submit', (evt) => {
  evt.preventDefault();
  const queryStr = document.querySelector('#food-name-search').value.toLowerCase();
  const filteredKeys = Object.keys(foodData).filter(k => k.includes(queryStr))
  // console.log(filteredKeys);
  const externalIds = []
  filteredKeys.forEach(key => {
    // console.log(key);
    externalIds.push(foodData[key]['external_id']);
  });

  
  const foodList = document.querySelector('#food-list')
  foodList.innerHTML=""
  console.log(filteredKeys)
  filteredKeys.forEach(key => {
    console.log(key)
    foodList.insertAdjacentHTML('beforeend', `<li id="${foodData[key]['external_id']}"> \
    <a href="/foods/${foodData[key]['food_id']}"> \
      ${foodData[key]['name']}</a> \
      <form type="submit" name="add-to-schedule-form" class="add-to-schedule-form"> \
        <input type="date" class="try-date" name="try-date" id="try-date-${foodData[key]['food_id']}"> \
        <button type="button" class="add-to-schedule-button" data-name="${foodData[key]['name']}" \
        data-id="${foodData[key]['food_id']}">Add To Schedule</button> \
      </form> \
    <p></p> \
  </li>`); 
    
  })

  const addToScheduleButton = document.querySelectorAll('.add-to-schedule-button');

  addToScheduleButton.forEach(button => button.addEventListener('click', event => {
    let foodName = event.target.getAttribute('data-name')
    let foodId = event.target.getAttribute('data-id')
    let tryDate = document.querySelector(`#try-date-${foodId}`).value
    
    console.log(tryDate)

    const data = {
      id: foodId, 
      name: foodName,
      date: tryDate
    }

    fetch('/edit-calendar', { 
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data)
    })
    .then((response) => response.json())
    .then((data) => console.log(data))  
  }));
  // console.log(externalIds)
})
