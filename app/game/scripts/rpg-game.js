

function movePlayer(direction) {
    let player = document.getElementById("player");
    console.log(direction);
    console.log(player.style.left, player.style.bottom);
    if (direction === "ArrowLeft") {
        player.style.left = String(Number(player.style.left.replace("px", "")) - tileSize) + "px";
    } else if (direction === "ArrowRight") {
        player.style.left = String(Number(player.style.left.replace("px", "")) + tileSize) + "px";
    } else if (direction === "ArrowUp") {
        player.style.bottom = String(Number(player.style.bottom.replace("px", "")) + tileSize) + "px";
    } else if (direction === "ArrowDown") {
        player.style.bottom = String(Number(player.style.bottom.replace("px", "")) - tileSize) + "px";
    }
}