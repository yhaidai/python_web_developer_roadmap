const roadmapItems = document.getElementsByClassName("roadmap-item");
const collapse = document.getElementById("roadmap-item-collapse")
const addRoadmapItemButton = document.getElementById("add-roadmap-item-button");
const collapseToggleButtons = Array.from(roadmapItems).concat([addRoadmapItemButton])
const nameInput = document.getElementById("name-input")
let isCollapseShown = false;
let formMethod = null
let formActionUrl = null

/* Change text of the button on collapse toggling */
addRoadmapItemButton.addEventListener("click", () => {
    isCollapseShown = !isCollapseShown;

    if (isCollapseShown) {
        formMethod = "POST"
        formActionUrl = `${location.protocol}//${location.host}/api/roadmap/`;
    } else {
        simplemde.value("")
        nameInput.value = ""
    }
})

for (let collapseToggleButton of collapseToggleButtons) {
    collapseToggleButton.addEventListener("click", () => {
        // TODO: fix caption logic
        if (isCollapseShown) {
            addRoadmapItemButton.innerText = "Hide";
        } else {
            addRoadmapItemButton.innerText = "Add new Roadmap Item";
        }
    })
}


for (let roadmap_item of roadmapItems) {
    const nameHeader = roadmap_item.querySelector(".name-header");

    roadmap_item.addEventListener("click", () => {
        // submitting the form after opening one of the roadmap items should "update" instead of "create"
        const roadmapItemUUID = roadmap_item.querySelector(".uuid-input").value;
        formMethod = "PATCH"
        formActionUrl = `${location.protocol}//${location.host}/api/roadmap/${roadmapItemUUID}/`;

        const apiUrl = `${formActionUrl}description`;
        fetch(apiUrl)
            .then((response) => response.json())
            .then((data) => {
                nameInput.value = nameHeader.innerText;
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

    fetch(formActionUrl, {
        method: formMethod,
        body: data,
        headers: {
            'X-CSRFToken': document.getElementsByName("csrfmiddlewaretoken")[0].value
        },
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            window.location.replace("");
        })
        .catch(error => {
            console.log(error)
        });
})
