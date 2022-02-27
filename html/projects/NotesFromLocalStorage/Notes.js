


console.log("hello")
let btn = document.getElementById("ButtonSave");

btn.addEventListener("click",function(e){  
    let text = document.getElementById("text");
    let notes = localStorage.getItem("notes");
    if(notes == null){
        var notesobj = []
    }
    else{
        notesobj = JSON.parse(notes);
    }

    notesobj.push(text.value);
    localStorage.setItem('notes', JSON.stringify(notesobj));
    text.value = ''
    showNotes()
} )

function showNotes(){
    let notes = localStorage.getItem("notes");
    if (notes== null){
        notesobj=[];
    }
    else {
        notesobj = JSON.parse(notes);
    }
    let html ='';
    notesobj.forEach(function(element,index) {
        html+= element +'with'+index;
        
    });
    let noteitem = document.getElementById("Notes");
    if(notesobj.length != 0){
    noteitem.innerHTML = html;}
    else{
        noteitem.innerHTML = "nothing"
    }
}



 
