





async function renderRPGMap(mapName, mapContainer=undefined){
    let mapData = await fetch("/rpg/map",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({mapName:mapName}),
        }
    ).then(response => {return response.json()});

    if (mapContainer === undefined){
        mapContainer = document.getElementsByClassName("rpg-map")[0];
    }
    [...mapContainer.children].forEach(c => {if (!c.classList.contains("template")){c.remove();}});
    let tileSize = 30;

    mapContainer.style.height = String(Number(mapData["size"][0]) * tileSize) + "px";
    mapContainer.style.width = String(Number(mapData["size"][1]) * tileSize) + "px";




    let templateTile = mapContainer.getElementsByClassName("template-tile")[0];
    let newTiles = [];
    let newTextures = mapData["tileTextures"];
    console.log(mapData);
    for (let [col, row] of Object.entries(newTextures)){
        console.log(col,row);
        row.forEach(tilePath => {
            let newTile = templateTile.cloneNode(true);
            newTile.className = "rpg-tile";
            newTile.style.backgroundImage = "url(" + tilePath +")";
            mapContainer.appendChild(newTile);
            newTiles.push(newTile);

        });
    }
    console.log(newTiles);
    console.log(await Promise.all(newTextures));
}







renderRPGMap("test-map");