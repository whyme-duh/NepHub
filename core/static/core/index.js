function navFunction(){
    var nav = document.getElementById("navLinks");
    if(nav.className === "nav-links"){
        nav.className += " responsive";
    }else{
        nav.className = "nav-links";
    }
}