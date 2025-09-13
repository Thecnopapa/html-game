





async function renderRPGMap(mapName, mapContainer=undefined){
    let mapData = await fetch("/rpg/map",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({mapName:mapName}),
        }
    );
    console.log(mapData);
    if (mapContainer === undefined){
        mapContainer = document.getElementsByClassName("rpg-map")[0];
    }
    [...mapContainer.children].forEach(c => {if (!c.classList.contains("template")){c.remove();}});


}









renderRPGMap("test-map");