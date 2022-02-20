function yo(){
    var elem2 = document.getElementById("span2")
    if (elem2.style.display =='block'){
        
        let elem = document.getElementById("span1")
        
        elem.style.transform = "rotate(45deg) translate(4px, 10px)"
        

        elem2.style.display = "none";
        
        let elem3 = document.getElementById("span3")
        elem3.style.transform = "rotate(-45deg) translate(0px,-5px)"
        
}
    else{
        let elem = document.getElementById("span1")
        elem.style.transform = "rotate(0) translate(0, 0)"

        let elem2 = document.getElementById("span2")
        elem2.style.display = "block";
    
        let elem3 = document.getElementById("span3")
        elem3.style.transform = "rotate(0) translate(0)"
    }
}