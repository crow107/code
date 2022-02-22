console.log("hello")
let btn = document.getElementById("ButtonSave");

btn.addEventListener("click",function(e){  
    let text = document.getElementById("text");
    let notes = localStorage.getItem("notes");
    if(notes == null){
        var notesobj = []
    }
    else{
        notes = JSON.parse(notes);
    }

    notesobj.push(text.value);
    localStorage.setItem('notes', JSON.stringify(notesobj));
    text.value = ''
    console.log(notesobj)
} )
