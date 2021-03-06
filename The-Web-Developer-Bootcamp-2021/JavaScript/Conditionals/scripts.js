// alert('Hello World!');
// alert(5 * 5);

// if (1 + 1 === 2) {
//     console.log('Math still works!');
// };

// console.log('After conditional');


// let num = Math.floor(Math.random() * 100)
// if (num % 2 === 0) {
//     alert('EVEN');
// } else {
//     alert('ODD');
// }


// const dayOfWeek = prompt('Enter a Day:');

// if (dayOfWeek === 'Monday') {
//     alert("I hate Mondays")
// } else if (dayOfWeek === 'Friday') {
//     alert("I love Fridays!")
// } else {
//     alert("Normal days")
// }

const password = prompt('Please enter a new password...');

if (password.length < 6) {
    alert('Error, password must be 6+ characters!')
} else if (password.length > password.trim().length) {
    alert('Error, no spaces allowed!')
} else {
    alert('New password accepted.')
}


