const myMath = {
    PI: 3.14159,
    square(num) {
        return num * num;
    },
    cube(num) {
        return num ** 3;
    }
}

const cat = {
    name: 'Blue',
    color: 'grey',
    breed: 'Scottish',
    meow() {
        console.log(`${this.name} says MEOWWWWW`);
    }

}