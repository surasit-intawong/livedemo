document.addEventListener("DOMContentLoaded", function () {
    fetch("https://gasprice.kapook.com/gasprice.php")  // สมมติว่ามี API ให้เรียก
        .then(response => response.json())  // แปลง JSON (ต้องใช้ API จริง)
        .then(data => {
            document.getElementById("update-time").textContent = data.update_time;
            
            const prices = {
                "ดีเซล B7": [data.ptt_b7, data.bcp_b7, data.shell_b7, data.esso_b7, data.caltex_b7],
                "ดีเซลพรีเมียม": [data.ptt_premium, data.bcp_premium, data.shell_premium, data.esso_premium, data.caltex_premium]
            };

            let tableBody = document.getElementById("fuel-prices");
            tableBody.innerHTML = "";
            for (let fuelType in prices) {
                let row = `<tr>
                    <td>${fuelType}</td>
                    <td>${prices[fuelType][0]}</td>
                    <td>${prices[fuelType][1]}</td>
                    <td>${prices[fuelType][2]}</td>
                    <td>${prices[fuelType][3]}</td>
                    <td>${prices[fuelType][4]}</td>
                </tr>`;
                tableBody.innerHTML += row;
            }
        })
        .catch(error => console.error("Error fetching data:", error));
});

document.addEventListener("DOMContentLoaded", function () {
    const fuelData = {
        "ดีเซล B7": [32.94, 32.94, 32.94, 32.94, 32.94],
        "ดีเซลพรีเมียม": [44.94, 47.14, 49.84, 47.14, 47.14]
    };

    let tableBody = document.getElementById("fuel-prices");
    for (let fuelType in fuelData) {
        let row = `<tr>
            <td>${fuelType}</td>
            <td>${fuelData[fuelType][0]}</td>
            <td>${fuelData[fuelType][1]}</td>
            <td>${fuelData[fuelType][2]}</td>
            <td>${fuelData[fuelType][3]}</td>
            <td>${fuelData[fuelType][4]}</td>
        </tr>`;
        tableBody.innerHTML += row;
    }
});