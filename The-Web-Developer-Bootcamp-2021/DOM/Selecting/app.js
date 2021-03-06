// const allImages = document.getElementsByTagName('img');

// for (let img of allImages) {
//     img.src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Partridge_Silkie_hen.jpg/900px-Partridge_Silkie_hen.jpg'
// }

const squareImages = document.getElementsByClassName('square');
for (const img of squareImages) {
    img.src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Partridge_Silkie_hen.jpg/900px-Partridge_Silkie_hen.jpg';
}

const javaLink = document.querySelector('a[title="Java"]');

const secondImage = document.querySelector('img:nth-of-type(2)');

const allImages = document.querySelectorAll('img');

const links = document.querySelectorAll('p a');

for (let link of links) {
    console.log(link.href)
}