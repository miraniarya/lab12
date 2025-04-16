//Kimaya Checked file 5 Edits
const baseURL = "http://localhost:8000";

// Edit 1: Fixed wrong HTTP method for deletion (changed POST to DELETE)
async function deleteItem(id) {
  await fetch(`${baseURL}/items/${id}`, { method: "DELETE" });
  loadItems(document.getElementById("search").value); 
}

// Edit 2: Fixed wrong Content-Type (changed application/html to application/json)
document.getElementById("itemForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = document.getElementById("name").value;
  const description = document.getElementById("description").value;
  await fetch(`${baseURL}/items`, {
    method: "POST",
    headers: { "Content-Type": "application/json" }, // Edit here
    body: JSON.stringify({ name, description })
  });
  e.target.reset();
  loadItems(document.getElementById("search").value);
});

// Edit 3: Added event listener for search functionality
document.getElementById("search").addEventListener("input", (e) => {
  loadItems(e.target.value); 
});

// Edit 4: DOM query safety assumed since we fixed HTML
async function loadItems(searchTerm = "") {
  const res = await fetch(`${baseURL}/items`);
  const data = await res.json();
  const list = document.getElementById("itemList");
  list.innerHTML = "";

  const filteredItems = data.filter(item =>
    item.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  document.getElementById("itemCount").textContent = `Total items: ${filteredItems.length}`;

  filteredItems.forEach(item => {
    const li = document.createElement("li");
    li.textContent = `${item.name}: ${item.description}`;
    const del = document.createElement("button");
    del.textContent = "Delete";
    del.onclick = () => deleteItem(item._id);
    li.appendChild(del);
    list.appendChild(li);
  });
}

//Edit 5: Call loadItems when page loads
loadItems();
