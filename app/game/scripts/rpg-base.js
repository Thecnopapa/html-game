
let tileSize = 32;

let mapContainers = document.getElementsByClassName("rpg-map");


async function renderRPGMap(mapName, mapContainer=undefined){
    if (mapContainer === undefined){
        mapContainer = mapContainers[0]
    }
    let tileContainer = mapContainer.getElementsByClassName("tile-container")[0];
    let mapData = await fetch("/rpg/map",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({mapName:mapName}),
        }
    ).then(response => {return response.json()});


    [...tileContainer.children].forEach(c => {if (!c.classList.contains("template")){c.remove();}});


    let templateTile = tileContainer.getElementsByClassName("template-tile")[0];

    console.log(tileSize);


    tileContainer.style.height = String(Number(mapData["size"][0]) * tileSize) + "px";
    tileContainer.style.width = String(Number(mapData["size"][1]) * tileSize) + "px";


    let newTiles = [];
    let newTextures = mapData["tileTextures"];
    console.log(mapData);
    for (let [col, row] of Object.entries(newTextures)){
        //console.log(col,row);
        row.forEach(tilePath => {
            let newTile = templateTile.cloneNode(true);
            newTile.className = "rpg-tile";
            newTile.style.backgroundImage = "url(" + tilePath +")";
            tileContainer.appendChild(newTile);
            newTiles.push(newTile);

        });
    }
}




async function spawnPlayer(x, y, mapContainer=undefined) {
    if (mapContainer === undefined){
        mapContainer = mapContainers[0]
    }
    let player = document.createElement("div");
    player.id = "player";
    player.style.left = x + "px";
    player.style.bottom = y + "px";
    let playerData = await fetch("/rpg/player",{
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    }).then(response => {return response.json()});
    player.style.backgroundImage = "url(" + playerData["texture"] + ")";
    mapContainer.appendChild(player);
    window.addEventListener("keydown", detectMoveDirection);

}

function detectMoveDirection(event){
    let key = event.key;
    movePlayer(key);
}















renderRPGMap("test-map");
spawnPlayer(0,0)