document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];

    let elem=document.getElementsByClassName('filename');
    if (elem.length>0)
        {
    elements = Array.from(elem);
    elements.forEach(function(element) {
        element.remove();
    });
    }

    const div=document.createElement('div')
    div.setAttribute('class','filename')
    div.innerHTML=file.name
    const uploaded=document.getElementById('uploder').appendChild(div)

    console.log(file.name)
    
});
