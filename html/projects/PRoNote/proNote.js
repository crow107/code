function yo(){
    var elem2 = document.getElementById("span2")
    if (elem2.style.display =='block'){
        
        let elem = document.getElementById("span1")
        
        elem.style.transform = "rotate(45deg) translate(4px, 10px)"
        

        elem2.style.display = "none";
        
        let elem3 = document.getElementById("span3")
        elem3.style.transform = "rotate(-45deg) translate(0px,-5px)"
        var men = document.getElementById("menbar")
        men.style.display= 'block';
        
}
    else{
        let elem = document.getElementById("span1")
        elem.style.transform = "rotate(0) translate(0, 0)"

        let elem2 = document.getElementById("span2")
        elem2.style.display = "block";
    
        let elem3 = document.getElementById("span3")
        elem3.style.transform = "rotate(0) translate(0)"
        var men = document.getElementById("menbar")
        men.style.display = 'none';
    }
}


function addData(){
    let text = document.getElementById("textarea1");
    let notes = localStorage.getItem("notes");

    if(notes==null){
        var noteobj =[];
    }
    else{
        noteobj = JSON.parse(notes);
    }
    noteobj.push(text.value);
    text.value = ''
    localStorage.setItem("notes" ,JSON.stringify(noteobj));
    showNotes() 

}






showNotes();
function showNotes() {
  let notes = localStorage.getItem("notes");
  if (notes == null) {
    notesObj = [];
  } else {
    notesObj = JSON.parse(notes);
  }
  let html = "";
  notesObj.forEach(function(element, index) {
    html +=  `<span class="notebox1">
    <p id="note2">Notes ${index+1}</p>
    <textarea id="textarea" cols="30" rows="10">${element}</textarea>
    <input type="button" value="Delete" onclick="deleteNote(this.id)" id="btn">
    </span>`;
  });
  let notesElm = document.getElementById("newdiv");
  if (notesObj.length != 0) {
    notesElm.innerHTML = html;
  } else {
    notesElm.innerHTML = `<p id= "nothing"> Add using Submit button</p>`;
  }
}

function deleteNote(index) {

  let notes = localStorage.getItem("notes");
  if (notes == null) {
    notesObj = [];
  } else {
    notesObj = JSON.parse(notes);
  }

  notesObj.splice(index, 1);
  localStorage.setItem("notes", JSON.stringify(notesObj));
  showNotes();
}


let search = document.getElementById('searchTxt');
search.addEventListener("input", function(){

    let inputVal = search.value.toLowerCase();
    let noteCards = document.getElementsByClassName('noteCard');
    Array.from(noteCards).forEach(function(element){
        let cardTxt = element.getElementsByTagName("p")[0].innerText;
        if(cardTxt.includes(inputVal)){
            element.style.display = "block";
        }
        else{
            element.style.display = "none";
        }
    })
})
 


 
 
