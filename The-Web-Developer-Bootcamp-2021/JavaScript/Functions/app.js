

// function singSong() {
//     console.log('DO');
//     console.log('RE');
//     console.log('ME');
// }
// singSong();

// function greet(firstName, lastName) {
//     console.log(`Hi, ${firstName} ${lastName[0]}. !!!`);
// }
// greet('Bob', 'Tanner');

// function repeat(str, numTimes) {
//     let result = '';
//     for (let i = 0; i < numTimes; i++) {
//         result += str;
//     }
//     console.log(result);
// }

// function add(x, y) {
//     if (typeof x !== 'number' || typeof y !== 'number') {
//         return false;
//     }
//     return x + y;
// }

// let total = add(5, 5);
// alert(`The total is ${total}`);

const daysOfWeek = ['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];


function returnDay(num) {
    if (num >= 8 || num <= 0) {
        return null;
    } else {
        return daysOfWeek[num];
    }
}