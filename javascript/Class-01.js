class pen{
    constructor(color, price) {
        this.color = color;
        this.price = price;
        
    }
    showcolor(){
        return this.color;
    }
    showprice(){
        return this.price;
    }

}


class pens extends pen{
    constructor (color,price,quantity){
        super(color,price)
        this.quantity =quantity;
    }
    
    showQuantity(){
        return this.quantity;
    }
}

pen = new pens("red",100,3);
console.log(pen.showQuantity())

