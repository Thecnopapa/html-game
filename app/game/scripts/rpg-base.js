





async function renderRPGMap(mapName){
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
}









renderRPGMap("test-map");