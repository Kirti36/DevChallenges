function Change() {
    document.getElementById("h1").innerHTML = "Magic Bro!";
    document.body.style.backgroundColor = 'black';
    let im = document.getElementById("Imd");
    if (im.style.display === "none") {
        im.style.display = "block"; // Show the image
    } else {
        im.style.display = "none"; // Hide the image
    }
    console.log(im);
    // }),

    // Call the Change function
    Change();









}