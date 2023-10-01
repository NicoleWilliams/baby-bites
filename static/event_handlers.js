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
// input to try date, get user id, when clicked update tried to true

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

// Step 1: User types in a a food they're searching for ==> form.input.value 
//    (we need to get this value when user submits on click submit) DONE
// Step 2: Once you grab the value, search against your json data to match on
//    either Object.keys(jsonData) ==> list of all your jsonData keys 

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

  // console.log(externalIds)
})




// Step 3: If filtering for matching keys, iterate through list of keys 
//    and grab the values in the jsonData for the external ids => DONE

// EX.  
// const jsonData = {
//   'apple': {name: 'Apple', externalId: 'apple'},
//   'apple-pie': {name: 'Apple Pie', externalId: 'apple-pie'},
//   'banana': {name: 'Banana', externalId: 'banana'},
//   'banana-apple': {name: 'Banana Apple', externalId: 'banana-apple'},
// }

// user search input value: "Apple"

// filter Object.keys(jsonData) that match "Apple" regex ==> return a list of filter 
//      jsonData keys DONE
// iterate through the list of filtered jsonData keys to match keys in jsonData 
//      to get the value ==> {..., externalId: ...} DONE
//***** */
// return list of externalIds and iterate through each one to filter <li> elements 
//      that match on li#externalId ==> list of <li> elements ==> return <li> elements 
//      to the dom to display







// function appendNodes(filteredFoods) {
//   let container = document.getElementById('searched-food');
//   if (filteredFoods != "no results"){
//        container.innerText = ""
//        filteredFoods.map((food) => {
//           let p = document.createElement("P")
//           p.innerText = food
//           container.appendChild(p)
//        })
//    } else {
//        container.innerText = "no results"
//    }
// }

// document.addEventListener("DOMContentLoaded", () => {
//   appendNodes(foodNames)
// });

// function onKeyUp(event) {
//   let str = event.target.value.toLowerCase().substring(0, 3)
//   let filteredArr = foodNames.filter((x) => {
//     let xSub = x.substring(0,3).toLowerCase()
//       return x.toLowerCase().includes(str) || checkName(xSub, str)
//   })
//   if (filteredArr.length > 0){
//       appendNodes(filteredArr)
//   } else {
//       appendNodes("no results")
//   }
// }

// function checkName(name, str) {
//   let pattern = str.split("").map((x) => {
//       return `(?=.*${x})`
//   }).join("");
//   let regex = new RegExp(`${pattern}`, "g")
//   return name.match(regex);
// }