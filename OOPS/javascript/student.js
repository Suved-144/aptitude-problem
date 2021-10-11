const fetchData = async () => {
    let display = document.getElementById('showData');
    const data = await fetch('./data.json')
        .then((data) => data.json())
        .then((data) => {
            data.forEach(element => {
                display.innerHTML += `
                    <tr>
                        <td>${element.name}</td>
                        <td>${element.age}</td>
                        <td>${element.gender}</td>
                    </tr>
                `
            });
        })
        .catch(err => console.log("the error is " + err))
}

fetchData();