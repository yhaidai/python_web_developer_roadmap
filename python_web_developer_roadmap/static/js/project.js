const roadmapItems = document.getElementsByClassName("roadmap-item");
const collapse = document.getElementById("roadmap-item-collapse")
const addRoadmapItemButton = document.getElementById("add-roadmap-item-button");
const collapseToggleButtons = Array.from(roadmapItems).concat([addRoadmapItemButton])
let isCollapseShown = false;

/* Change text of the button on collapse toggling */
addRoadmapItemButton.addEventListener("click", () => {
    isCollapseShown = !isCollapseShown;
})

for (let collapseToggleButton of collapseToggleButtons) {
    collapseToggleButton.addEventListener("click", () => {
        if (isCollapseShown) {
            addRoadmapItemButton.innerText = "Hide";
        } else {
            addRoadmapItemButton.innerText = "Add new Roadmap Item";
        }
    })
}


for (let roadmap_item of roadmapItems) {
    const roadmapItemUUID = roadmap_item.querySelector(".uuid-input").value;
    const apiUrl = `${location.protocol}//${location.host}/api/roadmap/${roadmapItemUUID}/`;
    const nameInput = document.getElementById("name-input")

    roadmap_item.addEventListener("click", () => {
        fetch(apiUrl)
            .then((response) => response.json())
            .then((data) => {
                nameInput.value = data["name"];
                simplemde.value(data["description"]);
            });

        // Always expand collapse on roadmap item selection
        collapse.classList.add("show")
        isCollapseShown = true;
    });
}

/* Redirect to the same page on form submission */
const roadmapItemForm = document.getElementById("roadmap-item-form");

roadmapItemForm.addEventListener("submit", (e) => {
    e.preventDefault()
    const data = new FormData(roadmapItemForm);

    fetch(roadmapItemForm.action, {
        method: "POST",
        credentials: "same-origin",
        headers: {
        },
        body: data,
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            window.location.replace("http://0.0.0.0:8000/roadmap/");
        })
        .catch(error => {
            console.log(error)
        });
})
