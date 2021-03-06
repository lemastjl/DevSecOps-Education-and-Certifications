

let userInput = prompt('What would you like to do?');
const todos = ['Go to store', 'Clean house'];
while (userInput !== 'quit' && userInput !== 'q') {
    if (userInput === 'list') {
        console.log('*********');
        for (let i = 0; i < todos.length; i++) {
            console.log(`${i}: ${todos[i]}`);
        }
        console.log('*********');
    } else if (userInput === 'new') {
        const newTodo = prompt('Enter new todo:');
        todos.push(newTodo);
        console.log(`"${newTodo}" added to the list.`);
    } else if (userInput === 'delete') {
        const deleteIndex = parseInt(prompt('Enter an index to delete:'));
        if (!Number.isNaN(deleteIndex)) {
            const itemDeleted = todos.splice(deleteIndex, 1);
            console.log(`Deleted list item "${itemDeleted[0]}".`);
        } else {
            console.log('Unknown index.');
        }
    }
    userInput = prompt('What would you like to do?');
}
console.log('YOU QUIT THE APP!');