const allLinks = document.querySelectorAll('a');

// for (let link of allLinks) {
//     link.innerText = 'I AM A LINK!!!!'
// }


for (let link of allLinks) {
    link.style.color = 'rgb(0, 108, 134)';
    link.style.textDecorationColor = 'magenta';
    link.style.textDecorationStyle = 'wavy'
}




document.querySelector('h1').innerHTML = '<i>first change</i>'

document.querySelector('h1').innerHTML += '<b> add on</b>'

document.querySelector('#banner').id = 'whoops'

document.querySelector('#whoops').id = 'banner'


const firstLink = document.querySelector('a')
//"http://127.0.0.1:5500/wiki/List_of_chicken_breeds"
firstLink.getAttribute('href')
//"/wiki/List_of_chicken_breeds"
firstLink.getAttribute('title')
//"List of chicken breeds"

firstLink.setAttribute('href', 'https://www.google.com')
firstLink.href
//"https://www.google.com/"


const input = document.querySelector('input[type="text"]')
input.type
//"text"
input.type = 'password'
//"password"
input.setAttribute('type', 'text')
//"text"


const h1 = document.querySelector('h1');

h1.style.color
//""
h1.style.color = 'magenta'
h1.style.color
//"magenta"
h1.style.fontSize = '3em'
//"3em"
h1.style.border = '2px solid pink'
//"2px solid pink"

window.getComputedStyle(h1).color
//"rgb(255, 0, 255)"

window.getComputedStyle(h1).fontSize
//"48px"

const h2 = document.querySelector('h2')
h2.classList
//""
h2.classList.add('purple')
h2.classList.add('border')
// h2.classList.remove('border')

h2.classList.toggle('border')
//off
h2.classList.toggle('border')
//back on


const squareImg = document.querySelector('.square');
squareImg.parentElement
//body
squareImg.nextSibling
//text nodes
squareImg.nextElementSibling
//next element
//properties "value" "parentElement" "children" "nextSibling" "previousSibling"

