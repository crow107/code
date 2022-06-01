class book{
    constructor(username,bookname,Date){
        this.username = username;
        this.bookname = bookname;
        this.Date = Date;
    }
    AddDataTolist(){
        let alldata = document.getElementById("dataToTable");
        let text = `<tr>
                <td>${this.username}</td>
                <td>${this.bookname}</td>
                <td>${this.Date}</td>
                <td><button class="btn btn-primary" delete-book-btn type="button">Delete</button></td>
                </tr>`

        alldata.innerHTML += text;

        
    }
    DeleteEntry(){
        let delbtn = document.querySelectorAll("[delete-book-btn]");
        delbtn.addEventListener("click",todelete(this));  
    }
}


var addbookbtn = document.querySelector("[add-book-btn]");

addbookbtn.addEventListener("click",addbook);

function addbook(){
    var bookname = document.getElementById("Bookname"); 
    var username = document.getElementById("username"); 
    var Date = document.getElementById("Date");
    let book1 = new book(username.value,bookname.value,Date.value);
    book1.AddDataTolist();
    bookname.value =''
    username.value =''
    Date.value =''
}

