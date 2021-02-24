window.onload = function() { //executes this code after the DOM loads
    //--- this is the selector element
    const vids = document.getElementsByTagName("video")

    //--- Now we loop over all of the selected elements and add event listeners
    for (let i = 0; i < vids.length; i++) {
        vids[i].addEventListener("mouseover", function(e) {
            vids[i].play()
        })
        vids[i].addEventListener("mouseout", function(e) {
            vids[i].pause()
        })
    }
}