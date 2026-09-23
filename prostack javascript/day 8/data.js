let employees = [
    { eid: 101, ename: 'rg', esal: 45000 },
    { eid: 102, ename: 'sg', esal: 55000 },
    { eid: 103, ename: 'pg', esal: 65000 }
];

function display_data() {

    let rows = "";

    for (let emp of employees) {

        rows = rows + `
            <tr>
                <td>${emp.eid}</td>
                <td>${emp.ename}</td>
                <td>${emp.esal}</td>
            </tr>
        `;
    }

    document.getElementsByTagName('tbody')[0].innerHTML = rows;
}