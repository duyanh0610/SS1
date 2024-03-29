var basedUrl = "http://localhost:3000";


function getData() {
  
  // GET Request.
  fetch("http://localhost:3000/api/list")
    // Handle success
    .then((response) => response.json()) // convert to json
    .then((data) => {
      
      //remove all item from list
      let list = document.querySelector(".todo-list");
      list.innerHTML = "";

      for (const item of data) {
        appendToList(item);
      }
    }) //print data to console
    .catch((err) => console.log("Get All Item Failed", err)); // Catch errors
}

window.onload = function () {
  getData();
};

function addItem(e) {
  // if enter key is pressed on the form input, add new item
  // which and keyCode are used to support different browsers
  if (e.which === 13 || e.keyCode === 13) {
    let item = document.querySelector(".new-todo");
    value = item.value
    if (value.replace(/\s/g, '') == "") {
      alert("Data must not be blank!!!")
    }
    else {
    let url ="http://localhost:3000/api/add";
    fetch(url, {
      method: "post",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        itemDescription: item.value
      })
    })
      .then((response) => response.json()) // convert to json
      .then((responseText) => {
        console.log(responseText);
        // empty form input once a response is received
        item.value = "";
        getData();
      })
      .catch((err) => console.log("Add Item Failed", err)); // Catch errors
    }
  }
}

function updateItem(itemID) {
  let url = "http://localhost:3000/api/update?id=" + itemID;
  // GET Request.
  fetch(url)
    // Handle success
    .then((response) => response.json()) // convert to json
    .then((responseText) => {
      console.log(responseText);
      getData();
    })
    .catch((err) => console.log("Update Item Failed", err)); // Catch errors
}

function deleteItem(itemID) {
  let url = "http://localhost:3000/api/delete?id=" + itemID;
  // GET Request.
  fetch(url)
    // Handle success
    .then((response) => response.json()) // convert to json
    .then((responseText) => {
      console.log(responseText);
      getData();
    })
    .catch((err) => console.log("Delete Item Failed", err)); // Catch errors
}

function appendToList(item) {
  let html = `
  <li id="${item.id}">
    <div class="view">`;
  if (item.status === "Done") {
    html += `<input class="toggle" type="checkbox" checked itemStatus="${item.status}"
              itemID="${item.id}" onclick="updateItem('${item.id}')">`;
  } else {
    html += `<input class="toggle" type="checkbox" itemStatus="${item.status}"
              itemID="${item.id}" onclick="updateItem('${item.id}')">`;
  }
  html += `
      <label>${item.description}</label>
      <button class="destroy" onclick="deleteItem('${item.id}')"></button>
    </div>
  </li>`;
  let list = document.querySelector(".todo-list");
  list.innerHTML += html;
}
