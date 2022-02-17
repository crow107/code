// console.log("Hello i")

let a = document.createElement("div");
let c = document.createElement("h1")
let b = document.createTextNode("Hello");

c.appendChild(b);
a.appendChild(c);
c.setAttribute('style','margin:0; background-color:cyan;color:white; padding:50px;');

a.style.textAlign = 'center';



let elem1 = document.createElement("div");
let elem2 = document.createElement("p");
let elem4 = document.createTextNode("Lorem ipsum dolor, sit amet consectetur adipisicing elit. Cum alias soluta, omnis voluptatibus provident dolore reiciendis itaque veniam. Sed vel perferendis eum, dolorum totam, facere accusamus ab necessitatibus, voluptate dicta iste? Unde laudantium molestiae, pariatur vero nesciunt obcaecati minus ad illo nam, suscipit necessitatibus, odio maxime quaerat! Odit voluptatum eaque, labore maxime explicabo neque commodi nihil amet nulla asperiores dolores ratione molestiae modi ullam nemo, magni facilis cumque a ducimus nisi laudantium quisquam ipsam eius nostrum. Amet consectetur temporibus unde? Accusantium, repellendus. Alias veniam similique vel atque itaque fugit repellat facere officiis quos animi distinctio cumque, placeat eos molestias illum.");
elem2.appendChild(elem4);
elem1.appendChild(elem2);


let elem3 = document.body;
elem3.style.margin = '0';
elem3.appendChild(a);
elem3.appendChild(elem1);